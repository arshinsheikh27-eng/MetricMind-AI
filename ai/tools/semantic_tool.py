from typing import Any, Dict

from langchain_core.tools import tool


@tool
def semantic_query(
    metric: str,
    dimension: str = None,
    filters: Dict[str, Any] = None,
    time_period: str = None,
) -> Dict[str, Any]:
    """
    Query the MetricMind semantic layer using approved business metrics.
    """

    filters = filters or {}

    approved_metrics = {
        "revenue",
        "margin",
        "profit",
        "orders",
        "customers",
    }

    if metric not in approved_metrics:
        return {
            "success": False,
            "error": f"Unsupported metric: {metric}",
        }

    return {
        "success": True,
        "metric": metric,
        "dimension": dimension,
        "filters": filters,
        "time_period": time_period,
        "data": [],
    }