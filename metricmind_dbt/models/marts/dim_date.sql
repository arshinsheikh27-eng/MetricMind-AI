{{ config(materialized='table') }}

SELECT DISTINCT
    order_date AS date_key,
    order_year,
    order_month,
    month_name,
    year_month,
    order_quarter
FROM {{ ref('stg_sales') }}
WHERE order_date IS NOT NULL