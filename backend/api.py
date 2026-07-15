from fastapi import FastAPI
from pydantic import BaseModel

from backend.agent import ask_movie_agent

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return ChatResponse(
        response=ask_movie_agent(request.message),
    )
