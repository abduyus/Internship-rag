from fastapi import FastAPI
from pydantic import BaseModel

try:
    from .search import search_movies as search_movies_backend
except ImportError:  # pragma: no cover - allows direct script execution
    from search import search_movies as search_movies_backend

app = FastAPI()


class MovieSearchRequest(BaseModel):
    query: str
    limit: int = 5


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/search")
def search_movies_endpoint(payload: MovieSearchRequest):
    results = search_movies_backend(payload.query, limit=payload.limit)

    return {
        "query": payload.query,
        "results": [
            {
                "title": movie.payload["title"],
                "genres": movie.payload["genres"],
                "director": movie.payload["director"],
                "overview": movie.payload["overview"],
                "release_date": movie.payload["release_date"],
            }
            for movie in results
        ],
    }
