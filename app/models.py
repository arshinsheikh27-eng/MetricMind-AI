from typing import Any

from pydantic import BaseModel


class AnalysisResult(BaseModel):
    question: str
    answer: str
    data: list[dict[str, Any]] = []
    insight: str | None = None