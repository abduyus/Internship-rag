import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient, models

# Load the environment variables
load_dotenv()

model_name = "sentence-transformers/all-MiniLM-L6-v2"

# Initialise the qdrant_client
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

# Create the collection 'movies', using the model specified for the size
qdrant_client.create_collection(collection_name='movies', vectors_config=models.VectorParams(
    size=qdrant_client.get_embedding_size(model_name),
    distance=models.Distance.COSINE
))
print(qdrant_client.get_collections())
