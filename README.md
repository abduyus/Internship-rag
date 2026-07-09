# Internship RAG

A small Retrieval-Augmented Generation (RAG) project for movie discovery and recommendation. The project uses semantic
search over a Qdrant vector database, reranks results for better relevance, and exposes both a simple RAG flow and an
agent-based workflow.

## Features

- Semantic movie search using sentence embeddings
- Duplicate removal before returning results
- Reranking with a cross-encoder model
- A simple LLM-based movie recommendation flow via Ollama
- An agent workflow with movie search and booking tools

## Project Structure

- `search.py` – semantic search, deduplication, and reranking
- `rag.py` – simple RAG pipeline that retrieves movies and builds a prompt for Ollama
- `agent.py` – agent-based version using LangChain tools
- `tools.py` – tool wrappers for search and booking
- `data/ingest.py` – script to load movie data into Qdrant
- `tests/` – unit and integration tests

## Prerequisites

- Docker Desktop
- Docker Compose
- A `.env` file with the required environment variables

## Docker Setup

1. Build and start the services:

   ```bash
   docker compose up --build
   ```

2. Create the movies collection in Qdrant:

   ```bash
   docker compose run --rm app python data/create_collection.py
   ```

3. Ingest the movie dataset into Qdrant:

   ```bash
   docker compose run --rm app python data/ingest.py
   ```


3. Send a message to the app:

   ```bash
   docker compose run --rm app python agent.py --message "Find a funny superhero movie and book it for 7pm"
   ```

## Local Development (optional)

If you want to run the project outside Docker:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then set the required environment variables and run:

```bash
python data/ingest.py
python agent.py
```

## Environment Variables

The project expects the following values in `.env`:

```env
QDRANT_URL=http://qdrant:6333
QDRANT_API_KEY=your-qdrant-api-key
EMBEDDING_MODEL=all-MiniLM-L6-v2
RERANK_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2
OLLAMA_MODEL=qwen2.5:7b
OLLAMA_BASE_URL=http://ollama:11434
MESSAGE=tony stark
```

## Testing

Run the test suite locally with:

```bash
./.venv/bin/python -m pytest -q
```

## Notes

- The project expects a Qdrant collection named `movies`.
- The Ollama model name can be changed through the `OLLAMA_MODEL` environment variable.
- If you want to use a different embedding or reranker model, update the corresponding environment variables.
