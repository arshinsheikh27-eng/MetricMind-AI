{{ config(materialized='table') }}

SELECT
    order_id,
    order_date,
    ship_date,
    region,
    country,
    item_type,
    sales_channel,
    order_priority,
    units_sold,
    unit_price,
    unit_cost,
    total_revenue,
    total_cost,
    total_profit,
    shipping_days,
    profit_margin_percent,
    order_year,
    month_name,
    year_month,
    order_month,
    order_quarter
FROM {{ ref('stg_sales') }}