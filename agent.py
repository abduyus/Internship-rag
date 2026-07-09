import argparse
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import AIMessage
from langchain_ollama import ChatOllama

from tools import book_movie, search_movies

load_dotenv()

# The LLM is given the available tools
llm = ChatOllama(model=os.getenv('OLLAMA_MODEL'))
tools = [search_movies, book_movie]
agent = create_agent(llm, tools)

# Allowing the user input through CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('--message', '-m', help='User message')
args = parser.parse_args()
message = args.message or os.getenv('MESSAGE') or input('Ask me about movie details and bookings: ')

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
    print(final_message.content)
else:
    print(response)
