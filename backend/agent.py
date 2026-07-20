import argparse
import os
import sys
from typing import List, Optional

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import AIMessage
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

from backend.tools import search_movies, book_movie

# from tools import book_movie, search_movies

load_dotenv()


class Movie(BaseModel):
    title: str
    year: int
    genres: List[str]
    overview: str = Field(description="A short 1-2 sentence description")
    why_it_matches: List[str]


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

Examples of requirements include:
- genre (crime, comedy, sci-fi, etc.)
- themes (detectives, investigations, time travel, AI, etc.)
- release year or date
- similarity to another movie
- actors or directors

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


def ask_movie_agent(message):
    # Step 1: let the agent reason and call tools as needed
    response = agent.invoke({
        "messages": [
            ("user", message)
        ]
    })

    raw_answer = _get_final_ai_message(response["messages"])

    if raw_answer is None:
        return {"summary": "I don't know.", "movies": []}

    # Booking confirmations are returned as-is, not squeezed into the
    # movie recommendations schema
    if _used_booking_tool(response["messages"]):
        return {"type": "booking", "message": raw_answer}

    # Step 2: structure the recommendation answer into clean JSON
    try:
        structured = structuring_llm.invoke(
            STRUCTURING_PROMPT.format(answer=raw_answer)
        )
        return structured.model_dump()
    except Exception as exc:
        # Structuring failed — fall back to the raw text rather than crash,
        # but make the failure visible so it can be caught in logs/evals
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
