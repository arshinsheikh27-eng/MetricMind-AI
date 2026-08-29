from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(
    title="MetricMind Backend",
    version="0.1.0",
    description="Backend API for the MetricMind analytics system",
)


class Question(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Natural-language business question",
    )


@app.get("/")
def home():
    return {
        "message": "MetricMind API is running",
        "status": "healthy",
    }


@app.post("/ask")
def ask_question(request: Question):
    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty.",
        )

    return {
        "status": "success",
        "question": question,
        "answer": "Question received successfully.",
    }