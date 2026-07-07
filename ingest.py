import pandas as pd
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
load_dotenv()

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Store the model name
model_name = "sentence-transformers/all-MiniLM-L6-v2"

# Load the movies from the csv with pandas
movies = pd.read_csv('data/movie_dataset.csv')
movie = movies.iloc[0]

collection_name = 'movies'

# Create the document and payload template
document = f"""
Title: {movie['title']}
Genres: {movie['genres']}
Director: {movie['director']}
Cast: {movie['cast']}
Overview: {movie['overview']}
"""

qdrant_client = QdrantClient(
    url=os.getenv('QDRANT_URL'),
    api_key=os.getenv('QDRANT_API_KEY'),
    timeout=60
)
print(qdrant_client.get_collections())

# qdrant_client.create_collection(collection_name='movies', vectors_config=models.VectorParams(
#     size=qdrant_client.get_embedding_size(model_name),
#     distance=models.Distance.COSINE
# ))
# embedding = model.encode(document).tolist()
#
#
# points = []
# batch_size = 20
#
# for idx, movie in movies.iterrows():
#
#     # Build text for embedding
#     document = f"""
#     Title: {movie['title']}
#     Genres: {movie['genres']}
#     Director: {movie['director']}
#     Cast: {movie['cast']}
#     Overview: {movie['overview']}
#     """
#
#     # Create embedding
#     vector = model.encode(document).tolist()
#
#     # Payload (what we retrieve later)
#     payload = {
#         "title": movie["title"],
#         "overview": movie["overview"],
#         "genres": movie["genres"],
#         "director": movie["director"],
#         "cast": movie["cast"],
#         "release_date": movie["release_date"],
#         "homepage": movie["homepage"],
#         "spoken_languages": movie["spoken_languages"]
#     }
#
#     # Create Qdrant point
#     points.append(
#         PointStruct(
#             id=idx,
#             vector=vector,
#             payload=payload
#         )
#     )
#
#     # -------------------------
#     # Batch upload
#     # -------------------------
#     if len(points) == batch_size:
#         qdrant_client.upsert(
#             collection_name=collection_name,
#             points=points
#         )
#         points = []
#         print(f"Uploaded {idx} movies...")
#
# # Upload remaining points
# if points:
#     qdrant_client.upsert(
#         collection_name=collection_name,
#         points=points
#     )
#
# print("✅ Finished uploading all movies")


# qdrant_client.upsert(
#     collection_name="movies",
#     points=[
#         PointStruct(
#             id=1,
#             vector=embedding,
#             payload=payload
#         )
#     ]
# )