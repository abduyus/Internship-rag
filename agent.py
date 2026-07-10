import argparse
import os
import sys

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import AIMessage
from langchain_ollama import ChatOllama

from tools import book_movie, search_movies

load_dotenv()

# The LLM is given the available tools
llm = ChatOllama(model=os.getenv('OLLAMA_MODEL'), base_url=os.getenv('OLLAMA_BASE_URL'))
tools = [search_movies, book_movie]
agent = create_agent(llm, tools)


def ask_movie_agent(message):
    # Send the user input to the agent
    response = agent.invoke({
        "messages": [
            ("user", message)
        ]
    })

    # Selecting the final response received from the LLM
    final_message = next(
        (msg for msg in reversed(response['messages']) if isinstance(msg, AIMessage)),
        None
    )

    if final_message:
        return final_message.content
    else:
        return response


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
