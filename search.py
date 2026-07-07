import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer, CrossEncoder

model = SentenceTransformer("all-MiniLM-L6-v2")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

# Load environement variables
load_dotenv()


# Creating a reusable function to search movies in the qdrant collection
def search_movies(question, limit=15):
    qdrant_client = QdrantClient(
        url=os.getenv('QDRANT_URL'),
        api_key=os.getenv('QDRANT_API_KEY'),
        timeout=60
    )

    # Encode the question into a semantic search vector
    query_vector = model.encode(question).tolist()

    # Retrieve the 15 movies most similar to the query vector
    results = qdrant_client.query_points(collection_name='movies', query=query_vector, limit=limit)

    # Remove duplicate results by title
    seen = set()
    deduped = []

    for point in results.points:
        title = point.payload["title"]

        if title not in seen:
            deduped.append(point)
            seen.add(title)

    # RERANKING
    pairs = [
        (question, point.payload["overview"])
        for point in results.points
    ]

    # Rerank results with a cross-encoder
    scores = reranker.predict(pairs)

    # Sort reranked results by score
    reranked = sorted(
        zip(results.points, scores),
        key=lambda x: x[1],
        reverse=True
    )

    # Return the top 5 most relevant movies
    top_results = [p[0] for p in reranked[:5]]

    return top_results

