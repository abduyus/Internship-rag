from langsmith.evaluation import evaluate

from agent import ask_movie_agent


def target(inputs: dict) -> dict:
    answer = ask_movie_agent(inputs["input"])

    return {
        "output": answer
    }


results = evaluate(
    target,
    data='movie-rag-evaluation',
    experiment_prefix='movie-rag-v2',
    description='Evaluation with more in depth prompts for the agent and tools'
)

print(results)
