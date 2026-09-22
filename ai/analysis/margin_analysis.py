from typing import Any


def calculate_margin(revenue: float, profit: float) -> float:
    """
    Calculate profit margin as a percentage.

    Formula:
        Margin % = (Profit / Revenue) * 100
    """

    if revenue == 0:
        return 0.0

    return round((profit / revenue) * 100, 2)


def analyze_margin(
    revenue: float,
    profit: float,
    previous_revenue: float | None = None,
    previous_profit: float | None = None,
) -> dict[str, Any]:
    """
    Analyze current margin and compare it with a previous period.
    """

    current_margin = calculate_margin(revenue, profit)

    result = {
        "revenue": revenue,
        "profit": profit,
        "margin": current_margin,
        "margin_unit": "percent",
    }

    # No previous-period data available
    if previous_revenue is None or previous_profit is None:
        result["previous_margin"] = None
        result["margin_change"] = None
        result["analysis"] = "Previous-period data is not available."

        return result

    previous_margin = calculate_margin(
        previous_revenue,
        previous_profit,
    )

    margin_change = round(
        current_margin - previous_margin,
        2,
    )

    result["previous_margin"] = previous_margin
    result["margin_change"] = margin_change

    if margin_change > 0:
        result["trend"] = "increased"
        result["analysis"] = (
            f"Margin increased by {margin_change} percentage points."
        )

    elif margin_change < 0:
        result["trend"] = "decreased"
        result["analysis"] = (
            f"Margin decreased by {abs(margin_change)} percentage points."
        )

    else:
        result["trend"] = "unchanged"
        result["analysis"] = "Margin remained unchanged."

    return result


def analyze_margin_from_result(semantic_result: dict[str, Any]) -> dict[str, Any]:
    """
    Analyze margin using a structured result returned by the semantic layer.

    Expected input example:

    {
        "success": True,
        "metric": "margin",
        "data": {
            "revenue": 100000,
            "profit": 20000
        }
    }
    """

    if not semantic_result.get("success"):
        return {
            "success": False,
            "error": semantic_result.get(
                "error",
                "Semantic query failed.",
            ),
        }

    data = semantic_result.get("data", {})

    revenue = data.get("revenue")
    profit = data.get("profit")

    if revenue is None or profit is None:
        return {
            "success": False,
            "error": "Revenue and profit data are required for margin analysis.",
        }

    previous_revenue = data.get("previous_revenue")
    previous_profit = data.get("previous_profit")

    analysis = analyze_margin(
        revenue=revenue,
        profit=profit,
        previous_revenue=previous_revenue,
        previous_profit=previous_profit,
    )

    return {
        "success": True,
        "metric": "margin",
        "analysis": analysis,
    }