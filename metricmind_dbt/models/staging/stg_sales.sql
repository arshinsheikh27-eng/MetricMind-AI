{{ config(materialized='view') }}

SELECT
    "Region" AS region,
    "Country" AS country,
    "Item Type" AS item_type,
    "Sales Channel" AS sales_channel,
    "Order Priority" AS order_priority,
    "Order Date" AS order_date,
    "Order ID" AS order_id,
    "Ship Date" AS ship_date,
    "Units Sold" AS units_sold,
    "Unit Price" AS unit_price,
    "Unit Cost" AS unit_cost,
    "Total Revenue" AS total_revenue,
    "Total Cost" AS total_cost,
    "Total Profit" AS total_profit,
    "Shipping Days" AS shipping_days,
    "Profit Margin %" AS profit_margin_pct,
    "Order Year" AS order_year,
    "Month Name" AS month_name,
    "Year-Month" AS year_month,
    "Order Month" AS order_month,
    "Order Quarter" AS order_quarter
FROM {{ source('raw', 'sales_data') }}