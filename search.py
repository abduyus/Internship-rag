import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer, CrossEncoder

model = SentenceTransformer("all-MiniLM-L6-v2")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

load_dotenv()


# Creating a reusable function to search movies in the qdrant collection
def search_movies(question, limit=15):
    qdrant_client = QdrantClient(
        url=os.getenv('QDRANT_URL'),
        api_key=os.getenv('QDRANT_API_KEY'),
        timeout=60
    )

    query_vector = model.encode(question).tolist()

    results = qdrant_client.query_points(collection_name='movies', query=query_vector, limit=limit)

    # Using deduplication to remove duplicates
    seen = set()
    deduped = []

    for point in results.points:
        title = point.payload["title"]

        if title not in seen:
            deduped.append(point)
            seen.add(title)

    # implementing reranking

    # 1. creating a tuple which contains the user's query along with the overview of the movie
    pairs = [
        (question, point.payload["overview"])
        for point in results.points
    ]

    # Using the reranking model to generate new scores for each of the 20 movies
    scores = reranker.predict(pairs)

    # Sorting these rerankings
    reranked = sorted(
        zip(results.points, scores),
        key=lambda x: x[1],
        reverse=True
    )

    # selecting the top 5 results
    top_results = [p[0] for p in reranked[:5]]

    return top_results

