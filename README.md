# 🎬 Internship RAG – AI Movie Recommendation System

An AI-powered movie recommendation system built using Retrieval-Augmented Generation (RAG), semantic search, local LLMs, and a modern React interface.

The application retrieves semantically relevant movies from a Qdrant vector database, reranks the results for accuracy, enriches them with TMDB metadata, and generates personalised recommendations using a local Ollama model.

---

## Features

### 🤖 AI Recommendation Engine

- Semantic movie search using sentence-transformer embeddings
- Cross-encoder reranking for improved relevance
- Duplicate removal
- Local LLM recommendations via Ollama
- LangChain agent with tool calling
- Structured JSON responses for the frontend

### 🎥 Modern Movie UI

- React + Vite frontend
- Responsive movie cards
- Movie backdrops from TMDB
- Match score progress bars
- Genre badges
- Runtime and rating display
- "Best Match" highlighting
- Clean dark-themed interface

### ⚙ Backend

- FastAPI REST API
- LangChain Agent
- Qdrant Vector Database
- Ollama integration
- TMDB API integration
- Dockerised services

### 📊 Evaluation

- LangSmith tracing
- Automated evaluation
- LLM scoring
- Feedback collection for future improvements

---

# Tech Stack

## Frontend

- React
- Vite
- Styled Components

## Backend

- Python
- FastAPI
- LangChain

## AI / ML

- Ollama
- Sentence Transformers
- Cross Encoder Reranker
- Qdrant

## Infrastructure

- Docker
- Docker Compose

---

# Architecture

```
                User
                  │
                  ▼
        React + Vite Frontend
                  │
                  ▼
            FastAPI Backend
                  │
        ┌─────────┴──────────┐
        ▼                    ▼
   LangChain Agent       TMDB API
        │
        ▼
 Semantic Search
        │
        ▼
 Qdrant Vector Database
        │
        ▼
 Cross Encoder Reranker
        │
        ▼
    Ollama LLM
        │
        ▼
 Structured JSON Response
```

---

# Project Structure

```
backend/
│
├── agent.py          # LangChain agent
├── api.py            # FastAPI API
├── search.py         # Semantic search & reranking
├── rag.py            # RAG pipeline
├── tmdb.py           # TMDB integration
├── tools.py          # LangChain tools
├── evaluator.py      # LangSmith evaluation
└── requirements.txt

frontend/
└── frontend/
    ├── src/
    ├── public/
    └── package.json

data/
tests/

docker-compose.yml
Dockerfile.ollama
```

---

# Running with Docker

Build every service

```bash
docker compose up --build
```

This starts:

- FastAPI
- React
- Ollama
- Qdrant

---

## Create the Vector Collection

```bash
docker compose run --rm app python data/create_collection.py
```

---

## Ingest Movie Dataset

```bash
docker compose run --rm app python data/ingest.py
```

---

## Application URLs

| Service | URL |
|----------|-----|
| React | http://localhost:5173 |
| FastAPI | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |
| Qdrant | http://localhost:6333 |
| Ollama | http://localhost:11434 |

---

# Environment Variables

Create a `.env` file.

```env
QDRANT_URL=http://qdrant:6333
QDRANT_API_KEY=

EMBEDDING_MODEL=all-MiniLM-L6-v2
RERANK_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2

OLLAMA_MODEL=qwen2.5:7b
OLLAMA_BASE_URL=http://ollama:11434

TMDB_API_KEY=YOUR_API_KEY

LANGCHAIN_API_KEY=
LANGCHAIN_ENDPOINT=
LANGCHAIN_PROJECT=
LANGCHAIN_TRACING_V2=true
```

---

# Local Development

Backend

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r backend/requirements.txt

uvicorn backend.api:app --reload
```

Frontend

```bash
cd frontend/frontend

npm install

npm run dev
```

---

# Testing

```bash
pytest
```

---

# Example Query

```
Find a funny superhero movie released after 2005.
```

Example response:

- Superhero Movie (2008)
- Super (2010)
- Mystery Men (1999)

Each recommendation includes:

- Match score
- Genres
- Runtime
- Rating
- Overview
- Why it matches
- Movie backdrop

---

# Future Improvements

- User feedback collection
- Personal recommendation history
- Hybrid keyword + semantic search
- Authentication
- Movie trailers
- Streaming platform availability
- Watchlists
- Favourite movies
- Continuous LangSmith evaluation

---

# License

This project was developed as part of an AI Engineering internship to explore Retrieval-Augmented Generation (RAG), semantic search, local LLMs, and modern frontend development.
