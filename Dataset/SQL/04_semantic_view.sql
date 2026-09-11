/* ============================================================
   METRICMIND-AI
   SEMANTIC VIEW
   Member 2 - Data & Semantic Layer
   ============================================================ */

CREATE OR REPLACE VIEW vw_sales_semantic AS

SELECT
    "Order ID",
    "Order Date",
    "Ship Date",

    "Region",
    "Country",

    "Item Type",
    "Sales Channel",
    "Order Priority",

    "Order Year",
    "Order Month",
    "Month Name",
    "Year-Month",
    "Order Quarter",

    "Units Sold",
    "Unit Price",
    "Unit Cost",

    "Total Revenue",
    "Total Cost",
    "Total Profit",

    "Profit Margin %",
    "Shipping Days",

    -- Profit category thresholds are prototype business classifications
    -- selected for reporting and AI-agent demonstration purposes.
    -- High Profit: >= 500,000
    -- Medium Profit: 100,000 to < 500,000
    -- Low Profit: < 100,000

    CASE
        WHEN "Total Profit" >= 500000 THEN 'High Profit'
        WHEN "Total Profit" >= 100000 THEN 'Medium Profit'
        ELSE 'Low Profit'
    END AS profit_category,

    CASE
        WHEN "Shipping Days" <= 7 THEN 'Fast'
        WHEN "Shipping Days" <= 14 THEN 'Normal'
        ELSE 'Slow'
    END AS shipping_category

FROM sales_data;

SELECT *
FROM vw_sales_semantic
LIMIT 5;

