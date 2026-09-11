{{ config(materialized='table') }}

SELECT DISTINCT
    region,
    country
FROM {{ ref('stg_sales') }}
WHERE country IS NOT NULL