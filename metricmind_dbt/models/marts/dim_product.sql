{{ config(materialized='table') }}

SELECT DISTINCT
    item_type
FROM {{ ref('stg_sales') }}
WHERE item_type IS NOT NULL