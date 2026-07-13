from agent import ask_movie_agent

questions = [
    "Recommend a sci-fi movie.",
    "Recommend a comedy."
]

for q in questions:
    print(q)
    print(ask_movie_agent(q))
