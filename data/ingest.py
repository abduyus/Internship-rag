import os

import pandas as pd
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from sentence_transformers import SentenceTransformer

load_dotenv()

model = SentenceTransformer(os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2"))

csv_path = os.path.join(os.path.dirname(__file__), "movie_dataset.csv")
movies = pd.read_csv(csv_path)

collection_name = "movies"

qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    timeout=60,
)

print(qdrant_client.get_collections())

points = []
batch_size = 20

for idx, movie in movies.iterrows():
    genres = movie["genres"]

    document = f"""
    Title: {movie['title']}
    Genres: {movie['genres']}
    Director: {movie['director']}
    Cast: {movie['cast']}
    Overview: {movie['overview']}
    """

    vector = model.encode(document).tolist()

    payload = {
        "title": movie["title"],
        "overview": movie["overview"],
        "genres": genres,
        "director": movie["director"],
        "cast": movie["cast"],
        "release_date": movie["release_date"],
        "homepage": movie.get("homepage"),
        "spoken_languages": movie.get("spoken_languages"),
        "rating": None if pd.isna(movie.get("vote_average")) else float(movie.get("vote_average")),
        "duration": None if pd.isna(movie.get("runtime")) else int(movie.get("runtime")),
    }

    points.append(
        PointStruct(
            id=idx,
            vector=vector,
            payload=payload,
        )
    )

    if len(points) == batch_size:
        qdrant_client.upsert(
            collection_name=collection_name,
            points=points,
        )
        points = []
        print(f"Uploaded {idx} movies...")

if points:
    qdrant_client.upsert(
        collection_name=collection_name,
        points=points,
    )

print("✅ Finished uploading all movies")
