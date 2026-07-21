from typing import List, Union, Literal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.agent import ask_movie_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class MovieOut(BaseModel):
    title: str
    year: int
    genres: List[str]
    overview: str
    why_it_matches: List[str]
    match_score: float
    backdrop_url: str | None = None


class RecommendationResponse(BaseModel):
    summary: str
    movies: List[MovieOut]


class BookingResponse(BaseModel):
    type: Literal["booking"]
    message: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/chat", response_model=Union[RecommendationResponse, BookingResponse])
async def chat(request: ChatRequest):
    return ask_movie_agent(request.message)
