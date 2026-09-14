from typing import Any, Dict


APPROVED_METRICS = {
    "revenue": "revenue",
    "sales": "revenue",
    "margin": "margin",
    "profit": "profit",
    "orders": "orders",
    "customers": "customers",
}


def parse_question(question: str) -> Dict[str, Any]:
    """
    Parse a business question into structured information.

    Returns:
        A dictionary containing:
        - success
        - metric
        - dimension
        - filters
        - time_period
        - intent
    """

    text = question.lower().strip()

    # -------------------------
    # Detect approved metric
    # -------------------------
    metric = None

    for keyword, approved_metric in APPROVED_METRICS.items():
        if keyword in text:
            metric = approved_metric
            break

    # -------------------------
    # Detect dimension
    # -------------------------
    dimension = None

    if "europe" in text or "european" in text:
        dimension = "region"
    elif "region" in text:
        dimension = "region"
    elif "product" in text:
        dimension = "product"
    elif "customer" in text:
        dimension = "customer"

    # -------------------------
    # Detect time period
    # -------------------------
    time_period = None

    if "last quarter" in text:
        time_period = "last quarter"
    elif "this quarter" in text:
        time_period = "this quarter"
    elif "last year" in text:
        time_period = "last year"
    elif "this year" in text:
        time_period = "this year"

    # -------------------------
    # Detect filters
    # -------------------------
    filters = {}

    if "europe" in text or "european" in text:
        filters["region"] = "Europe"

    # -------------------------
    # Detect intent
    # -------------------------
    intent = "general"

    if "why" in text:
        intent = "explanation"
    elif "what caused" in text:
        intent = "explanation"
    elif "reason" in text:
        intent = "explanation"

    # -------------------------
    # Return structured result
    # -------------------------
    return {
        "success": metric is not None,
        "metric": metric,
        "dimension": dimension,
        "filters": filters,
        "time_period": time_period,
        "intent": intent,
    }