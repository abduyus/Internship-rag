from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_core.messages import AIMessage

from tools import book_movie, search_movies

llm = ChatOllama(model='qwen2.5:14b')

tools = [search_movies, book_movie]

agent = create_agent(llm, tools)

message = input('Ask me about movie details and bookings: ')

response = agent.invoke({
    "messages": [
        ("user", message)
    ]
})

final_message = next(
    (msg for msg in reversed(response['messages']) if isinstance(msg, AIMessage)),
    None
)

if final_message:
    print(final_message.content)
else:
    print(response)

