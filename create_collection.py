# creating the Qdrant collection 'movies'
from qdrant_client import QdrantClient, models

model_name = "sentence-transformers/all-MiniLM-L6-v2"


qdrant_client = QdrantClient(
    url="https://18d6025a-fdb1-46c4-bcdd-cda78aa31eb9.sa-east-1-0.aws.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwic3ViamVjdCI6ImFwaS1rZXk6MGIyMzNkYmEtOGYxOS00NGViLTllZDMtZGU1NjAwZWYwNjlhIn0.g0PY42E7Qf3qtsulXyR_KwZ4oTKk5zFrv0lZyXQFX2M",
)

qdrant_client.create_collection(collection_name='movies', vectors_config=models.VectorParams(
    size=qdrant_client.get_embedding_size(model_name),
    distance=models.Distance.COSINE
))
print(qdrant_client.get_collections())