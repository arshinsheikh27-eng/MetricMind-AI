{{ config(materialized='view') }}

SELECT
    SUM(total_revenue) AS total_revenue,
    SUM(total_cost) AS total_cost,
    SUM(total_profit) AS total_profit,
    SUM(units_sold) AS total_units_sold,
    COUNT(DISTINCT order_id) AS total_orders,

    CASE
        WHEN SUM(total_revenue) = 0 THEN 0
        ELSE
            (SUM(total_profit) / SUM(total_revenue)) * 100
    END AS profit_margin_percent,

    CASE
        WHEN COUNT(DISTINCT order_id) = 0 THEN 0
        ELSE
            SUM(total_revenue) / COUNT(DISTINCT order_id)
    END AS average_order_revenue,

    CASE
        WHEN SUM(units_sold) = 0 THEN 0
        ELSE
            SUM(total_revenue) / SUM(units_sold)
    END AS average_selling_price

FROM {{ ref('fact_sales') }}