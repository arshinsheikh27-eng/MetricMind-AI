import psycopg2
from psycopg2.extras import RealDictCursor


class AnalyticsService:
    def __init__(self, database_url: str):
        if not database_url:
            raise RuntimeError("DATABASE_URL is not configured.")

        self.database_url = database_url

    def _execute_query(self, query):
        try:
            with psycopg2.connect(self.database_url) as connection:
                with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    return [dict(row) for row in rows]

        except psycopg2.Error as exc:
            raise RuntimeError(
                f"Unable to query analytics data: {exc}"
            ) from exc

    def get_summary(self):
        query = """
            SELECT
                total_revenue,
                total_cost,
                total_profit,
                total_units_sold,
                total_orders,
                profit_margin_percent,
                average_order_revenue,
                average_selling_price
            FROM metrics_sales
            LIMIT 1;
        """

        rows = self._execute_query(query)
        return rows[0] if rows else None

    def get_revenue_by_region(self):
        query = """
            SELECT
                region,
                SUM(total_revenue) AS revenue
            FROM fact_sales
            WHERE region IS NOT NULL
            GROUP BY region
            ORDER BY revenue DESC;
        """

        return self._execute_query(query)

    def get_profit_by_product(self):
        query = """
            SELECT
                item_type,
                SUM(total_profit) AS profit
            FROM fact_sales
            WHERE item_type IS NOT NULL
            GROUP BY item_type
            ORDER BY profit DESC;
        """

        return self._execute_query(query)

    def get_sales_by_channel(self):
        query = """
            SELECT
                sales_channel,
                SUM(total_revenue) AS revenue,
                SUM(total_profit) AS profit,
                SUM(units_sold) AS units_sold,
                COUNT(DISTINCT order_id) AS orders
            FROM fact_sales
            WHERE sales_channel IS NOT NULL
            GROUP BY sales_channel
            ORDER BY revenue DESC;
        """

        return self._execute_query(query)

    def get_sales_by_quarter(self):
        query = """
            SELECT
                order_year,
                order_quarter,
                SUM(total_revenue) AS revenue,
                SUM(total_profit) AS profit,
                SUM(units_sold) AS units_sold
            FROM fact_sales
            GROUP BY order_year, order_quarter
            ORDER BY order_year, order_quarter;
        """

        return self._execute_query(query)