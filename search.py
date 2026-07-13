import os
import time

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer, CrossEncoder

# Load environment variables
load_dotenv()

qdrant_client = QdrantClient(
    url=os.getenv('QDRANT_URL'),
    api_key=os.getenv('QDRANT_API_KEY'),
    timeout=60
)

_embedding_model = None
_reranker = None


def _get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = SentenceTransformer(os.getenv('EMBEDDING_MODEL', 'all-MiniLM-L6-v2'))
    return _embedding_model


def _get_reranker():
    global _reranker
    if _reranker is None:
        _reranker = CrossEncoder(os.getenv('RERANKER_MODEL', 'cross-encoder/ms-marco-MiniLM-L-6-v2'))
    return _reranker


model = _get_embedding_model()
reranker = _get_reranker()


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
def search_movies(question, limit=7):
    """Retrieve, deduplicate, and rerank movies relevant to the user's query"""

    retrieval_limit = 10

    # Encode the question into a semantic search vector
    start = time.perf_counter()
    query_vector = model.encode(question).tolist()
    print(f"Embedding: {time.perf_counter() - start:.2f}s")

    # Retrieve the 15 movies most similar to the query vector
    start = time.perf_counter()
    results = qdrant_client.query_points(collection_name='movies', query=query_vector, limit=retrieval_limit)
    print(f"Qdrant: {time.perf_counter() - start:.2f}s")

    # Remove duplicate results by title
    start = time.perf_counter()
    deduped = deduplicate_results(results.points)
    print(f"Deduped: {time.perf_counter() - start:.2f}s")

    # Rerank results with a cross encoder
    start = time.perf_counter()
    top_results = rerank_results(question, deduped, limit=limit)
    print(f"Rerank: {time.perf_counter() - start:.2f}s")

    return top_results
