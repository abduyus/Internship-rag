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
    experiment_prefix='movie-rag-v4',
    description='Evaluation after changing model to mistral:7b'
)

print(results)
