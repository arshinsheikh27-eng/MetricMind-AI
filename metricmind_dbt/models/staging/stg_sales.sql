{{ config(materialized='view') }}

SELECT
    region,
    country,
    item_type,
    sales_channel,
    order_priority,
    order_date,
    order_id,
    ship_date,
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
FROM {{ source('raw', 'raw_sales') }}