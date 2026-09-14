import os
from typing import Any, Dict

import psycopg2
from psycopg2.extras import RealDictCursor
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()


APPROVED_METRICS = {
    "revenue",
    "profit",
    "margin",
    "orders",
}


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

    if metric not in APPROVED_METRICS:
        return {
            "success": False,
            "error": f"Unsupported metric: {metric}",
        }

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        return {
            "success": False,
            "error": "DATABASE_URL is not configured.",
        }

    metric_expressions = {
        "revenue": "SUM(total_revenue)",
        "profit": "SUM(total_profit)",
        "margin": """
            CASE
                WHEN SUM(total_revenue) = 0 THEN 0
                ELSE (SUM(total_profit) / SUM(total_revenue)) * 100
            END
        """,
        "orders": "COUNT(DISTINCT order_id)",
    }

    dimension_columns = {
        "region": "region",
        "country": "country",
        "product": "item_type",
        "category": "item_type",
        "time": "order_year",
    }

    if dimension and dimension not in dimension_columns:
        return {
            "success": False,
            "error": f"Unsupported dimension: {dimension}",
        }

    try:
        with psycopg2.connect(database_url) as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:

                metric_expression = metric_expressions[metric]

                if dimension:
                    dimension_column = dimension_columns[dimension]

                    query = f"""
                        SELECT
                            {dimension_column} AS dimension,
                            {metric_expression} AS value
                        FROM fact_sales
                        WHERE {dimension_column} IS NOT NULL
                        GROUP BY {dimension_column}
                        ORDER BY value DESC;
                    """

                    cursor.execute(query)
                    rows = [dict(row) for row in cursor.fetchall()]

                    return {
                        "success": True,
                        "metric": metric,
                        "dimension": dimension,
                        "filters": filters,
                        "time_period": time_period,
                        "data": rows,
                    }

                query = f"""
                    SELECT
                        {metric_expression} AS value
                    FROM fact_sales;
                """

                cursor.execute(query)
                row = cursor.fetchone()

                return {
                    "success": True,
                    "metric": metric,
                    "dimension": dimension,
                    "filters": filters,
                    "time_period": time_period,
                    "data": dict(row) if row else {},
                }

    except psycopg2.Error as exc:
        return {
            "success": False,
            "error": f"Unable to query semantic data: {exc}",
        }