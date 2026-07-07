import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer, CrossEncoder

# Load environment variables
load_dotenv()


def deduplicate_results(points):
    """Remove duplicate points from a list"""
    # Remove duplicate results by title
    seen = set()
    deduped = []

    for point in points:
        title = point.payload["title"]

        if title not in seen:
            deduped.append(point)
            seen.add(title)
    return deduped


def rerank_results(question, points, limit=5):
    """Rerank results from a list"""

    if not points:
        return []

    reranker = CrossEncoder(os.getenv('RERANKER_MODEL', "cross-encoder/ms-marco-MiniLM-L-6-v2"))

    pairs = [
        (question, point.payload["overview"])
        for point in points
    ]

    # Rerank results with a cross-encoder
    scores = reranker.predict(pairs)

    # Sort reranked results by score
    reranked = sorted(
        zip(points, scores),
        key=lambda x: x[1],
        reverse=True
    )

    # Return the top 5 most relevant movies
    return [point for point, _ in reranked[:limit]]


# Creating a reusable function to search movies in the qdrant collection
def search_movies(question, limit=15):
    """Retrieve, deduplicate, and rerank movies relevant to the user's query"""
    model = SentenceTransformer(os.getenv('EMBEDDING_MODEL'))

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
    deduped = deduplicate_results(results.points)

    # Rerank results with a cross encoder
    top_results = rerank_results(question, deduped, limit=5)

    return top_results
