# Internship RAG

A small Retrieval-Augmented Generation (RAG) project for movie discovery and recommendation. The project uses semantic search over a Qdrant vector database, reranks results for better relevance, and exposes both a simple RAG flow and an agent-based workflow.

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
- `ingest.py` – script to load movie data into Qdrant
- `tests/` – unit and integration tests

## Prerequisites

- Python 3.10+
- A running Ollama instance
- A Qdrant instance with an API key
- The movie dataset located in `data/movie_dataset.csv`

## Setup

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set the required environment variables:

   ```bash
   export QDRANT_URL="your-qdrant-url"
   export QDRANT_API_KEY="your-qdrant-api-key"
   export EMBEDDING_MODEL="all-MiniLM-L6-v2"
   export RERANKER_MODEL="cross-encoder/ms-marco-MiniLM-L-6-v2"
   export OLLAMA_MODEL="qwen2.5:14b"
   ```

## Ingest the Data

Run the ingestion script to load the movie dataset into Qdrant:

```bash
python ingest.py
```

## Run the Project

### Simple RAG flow

```bash
python rag.py
```

### Agent flow

```bash
python agent.py
```

## Testing

Run the test suite with:

```bash
python -m pytest -q
```

## Notes

- The project expects a Qdrant collection named `movies`.
- The Ollama model name can be changed through the `OLLAMA_MODEL` environment variable.
- If you want to use a different embedding or reranker model, update the corresponding environment variables.
