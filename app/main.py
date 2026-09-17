import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.services.analytics_service import AnalyticsService
from app.services.llm_service import LLMService

load_dotenv()

app = FastAPI(
    title="MetricMind Backend",
    version="0.2.0",
    description="Backend API for the MetricMind analytics system",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Natural-language business question",
    )


database_url = os.getenv("DATABASE_URL")

analytics_service = None

if database_url:
    analytics_service = AnalyticsService(database_url)


@app.get("/")
def home():
    return {
        "message": "MetricMind API is running",
        "status": "healthy",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database_configured": bool(database_url),
    }


@app.get("/analytics/summary")
def analytics_summary():
    if analytics_service is None:
        raise HTTPException(
            status_code=503,
            detail="DATABASE_URL is not configured.",
        )

    try:
        result = analytics_service.get_summary()

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="No summary data found.",
            )

        return {
            "status": "success",
            "data": result,
        }

    except RuntimeError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        ) from exc


@app.get("/analytics/revenue-by-region")
def revenue_by_region():
    if analytics_service is None:
        raise HTTPException(
            status_code=503,
            detail="DATABASE_URL is not configured.",
        )

    try:
        return {
            "status": "success",
            "data": analytics_service.get_revenue_by_region(),
        }

    except RuntimeError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        ) from exc


@app.get("/analytics/profit-by-product")
def profit_by_product():
    if analytics_service is None:
        raise HTTPException(
            status_code=503,
            detail="DATABASE_URL is not configured.",
        )

    try:
        return {
            "status": "success",
            "data": analytics_service.get_profit_by_product(),
        }

    except RuntimeError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        ) from exc


@app.get("/analytics/sales-by-channel")
def sales_by_channel():
    if analytics_service is None:
        raise HTTPException(
            status_code=503,
            detail="DATABASE_URL is not configured.",
        )

    try:
        return {
            "status": "success",
            "data": analytics_service.get_sales_by_channel(),
        }

    except RuntimeError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        ) from exc


@app.get("/analytics/sales-by-quarter")
def sales_by_quarter():
    if analytics_service is None:
        raise HTTPException(
            status_code=503,
            detail="DATABASE_URL is not configured.",
        )

    try:
        return {
            "status": "success",
            "data": analytics_service.get_sales_by_quarter(),
        }

    except RuntimeError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        ) from exc


@app.post("/ask")
def ask_question(request: Question):
    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty.",
        )

    try:
        service = LLMService()
        answer = service.ask(question)

        return {
            "status": "success",
            "question": question,
            "answer": answer,
        }

    except RuntimeError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"LLM service error: {exc}",
        ) from exc