import argparse
import json
import os
import sys
from typing import List, Optional

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import AIMessage, ToolMessage
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

from backend.tmdb import get_backdrop
from backend.tools import search_movies, book_movie

# from tools import book_movie, search_movies

load_dotenv()


class Movie(BaseModel):
    title: str
    year: int
    genres: List[str]
    overview: str = Field(description="A short 1-2 sentence description")
    why_it_matches: List[str] = Field(
        description="2-4 short bullet-point fragments (under 8 words each), not full sentences"
    )
    match_score: float = Field(
        description="Relevance score returned by the search tool"
    )
    rating: float
    duration: int


class MovieRecommendations(BaseModel):
    summary: str = Field(description="Short 1-2 sentence summary")
    movies: List[Movie]


SYSTEM_PROMPT = """
You are a helpful movie recommendation and booking assistant.

Your responsibilities are:

- Always use the available tools whenever they can answer the user's request.
- Never make up movie information, release dates, genres, or booking confirmations.
- If the tools cannot provide enough information, clearly say that you don't know instead of guessing.

When recommending movies:
- Carefully identify every requirement in the user's request.
- Ensure each recommendation satisfies all of the user's stated requirements before including it.
- Do not recommend movies that only partially match the request.
- If only a few movies satisfy all requirements, return only those movies rather than weaker matches.
- Briefly explain why each recommended movie matches the user's request.
- Ensure you return the genres, release data, runtime exactly as they are from the database 

Examples of requirements include:
- genre (crime, comedy, sci-fi, etc.)
- themes (detectives, investigations, time travel, AI, etc.)
- release year or date
- similarity to another movie
- actors or directors
- duration
- rating

For booking requests:
- Use the booking tool only when the user explicitly wants to book or reserve a movie.
- Confirm the booking only after using the booking tool.

Be accurate, concise, and transparent about any limitations.

When users specify criteria like release year:
1. VERIFY each movie meets the stated criteria before recommending
2. If a movie doesn't match, exclude it from your response, even if you find another release date for the movie
3. Only recommend movies that satisfy ALL user requirements
"""

STRUCTURING_PROMPT = """
Convert the answer below into the required structured format.

Rules:
- Do not add, remove, or invent any movies that are not already present in the answer.
- Do not change any titles, years, genres, or facts.
- Only reorganize the existing content into the schema fields.
- Preserve the match_score exactly as provided by the search tool.
- Do not modify or estimate match scores.
- Do not modify ratings and durations

For each movie's why_it_matches:
- Return 2-4 SEPARATE bullet points, one reason per list item.
- Each bullet must be under 8 words.
- Use sentence fragments, not full sentences — no subject + verb needed (e.g. "Comedic take on the superhero genre" not "This movie features a comedic take on the superhero genre").
- Do NOT put more than one reason in a single list item.
- Do not copy the genres into why_it_matches.
- Base the reasons on the user's query and the movie description.

For each movie:

- Do not copy the genres into why_it_matches.
- Base the reasons on the user's query and the movie description.

Answer to convert:
{answer}
"""

# The agent handles tool-calling and reasoning. It is NOT asked to also
# self-report structured JSON here, since forcing a final structured tool
# call after a multi-turn tool loop is unreliable with Ollama models.
llm = ChatOllama(model=os.getenv('OLLAMA_MODEL'), base_url=os.getenv('OLLAMA_BASE_URL'))
tools = [search_movies, book_movie]
agent = create_agent(
    llm,
    tools,
    system_prompt=SYSTEM_PROMPT,
)

# A separate model call, constrained with Ollama's native `format` schema,
# does the structuring. This is a distinct step from tool-calling, so it
# doesn't depend on the flaky forced-tool-call behavior.
structuring_llm = ChatOllama(
    model=os.getenv('OLLAMA_MODEL'),
    base_url=os.getenv('OLLAMA_BASE_URL'),
).with_structured_output(MovieRecommendations, method="json_schema")


def _used_booking_tool(messages) -> bool:
    """Check whether book_movie was called during this turn.

    Booking confirmations don't fit the MovieRecommendations schema, so
    those responses are returned as plain text instead of being forced
    into a shape that doesn't match what happened.
    """
    for msg in messages:
        tool_calls = getattr(msg, "tool_calls", None)
        if tool_calls:
            for call in tool_calls:
                if call.get("name") == "book_movie":
                    return True
    return False


def _get_final_ai_message(messages) -> Optional[str]:
    final_message = next(
        (msg for msg in reversed(messages) if isinstance(msg, AIMessage)),
        None
    )
    return final_message.content if final_message else None


def _get_tool_results(messages, tool_name="search_movies"):
    """Pull the real, unmodified movie data out of the tool call results."""
    results = []
    for msg in messages:
        if isinstance(msg, ToolMessage) and msg.name == tool_name:
            content = msg.content
            try:
                parsed = json.loads(content) if isinstance(content, str) else content
                if isinstance(parsed, list):
                    results.extend(parsed)
            except (json.JSONDecodeError, TypeError):
                pass
    return results


def ask_movie_agent(message):
    response = agent.invoke({
        "messages": [("user", message)]
    })

    raw_answer = _get_final_ai_message(response["messages"])

    if raw_answer is None:
        return {"summary": "I don't know.", "movies": []}

    if _used_booking_tool(response["messages"]):
        return {"type": "booking", "message": raw_answer}

    # Step 2: structure the recommendation answer into clean JSON
    try:
        structured = structuring_llm.invoke(
            STRUCTURING_PROMPT.format(answer=raw_answer)
        )

        result = structured.model_dump()

        # --- pull real values from the tool output, never trust the LLM's copy ---
        tool_results = _get_tool_results(response["messages"])
        data_by_title = {r["title"]: r for r in tool_results}

        for movie in result["movies"]:
            source = data_by_title.get(movie["title"])
            if source:
                movie["match_score"] = source["match_score"]  # real int, 0–100, from search.py
                movie["genres"] = source["genres"]
                movie["overview"] = source["overview"]
                movie["rating"] = source.get("rating")
                movie["duration"] = source.get("duration")
                movie["year"] = int(source["release_date"][:4])
            # ---------------------------------------------------------------------

            movie["backdrop_url"] = get_backdrop(movie["title"], movie["year"])

        return result
    except Exception as exc:
        print(f"Structuring step failed: {exc}", file=sys.stderr)
        return {"summary": raw_answer, "movies": []}


if __name__ == '__main__':

    # Parse CLI args with an env-var fallback. For safety in containers/CI,
    # prefer passing --message or the MESSAGE env var. Interactive input is
    # allowed only when --interactive is provided and stdin is a TTY.
    parser = argparse.ArgumentParser()
    parser.add_argument('--message', '-m', help='User message')
    parser.add_argument('--interactive', action='store_true', help='Allow interactive prompt (local/dev only)')
    args = parser.parse_args()

    message = args.message or os.getenv('MESSAGE')

    if not message:
        if args.interactive:
            if sys.stdin is None or not sys.stdin.isatty():
                sys.exit(
                    'Interactive mode requested but no TTY is available. Provide --message or set MESSAGE env var.')
            try:
                message = input('Ask me about movie details and bookings: ')
            except EOFError:
                sys.exit('No input received. Provide --message or set MESSAGE env var.')
        else:
            sys.exit('No message provided. Use --message or set MESSAGE environment variable.')

    print(ask_movie_agent(message))
