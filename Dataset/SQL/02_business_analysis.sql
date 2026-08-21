-- ============================================================
-- MetricMind-AI
-- Business Analysis
-- PostgreSQL
-- ============================================================

/* ============================================================
   1. DATA VALIDATION
   ============================================================ */

-- Total number of records
SELECT COUNT(*) AS total_rows
FROM sales_data;


-- Preview first 10 records
SELECT *
FROM sales_data
LIMIT 10;


-- Check missing values
SELECT
    COUNT(*) FILTER (WHERE "Region" IS NULL) AS region_missing,
    COUNT(*) FILTER (WHERE "Country" IS NULL) AS country_missing,
    COUNT(*) FILTER (WHERE "Item Type" IS NULL) AS item_type_missing,
    COUNT(*) FILTER (WHERE "Sales Channel" IS NULL) AS sales_channel_missing,
    COUNT(*) FILTER (WHERE "Order Priority" IS NULL) AS priority_missing,
    COUNT(*) FILTER (WHERE "Order Date" IS NULL) AS order_date_missing,
    COUNT(*) FILTER (WHERE "Ship Date" IS NULL) AS ship_date_missing,
    COUNT(*) FILTER (WHERE "Units Sold" IS NULL) AS units_sold_missing,
    COUNT(*) FILTER (WHERE "Unit Price" IS NULL) AS unit_price_missing,
    COUNT(*) FILTER (WHERE "Total Revenue" IS NULL) AS revenue_missing,
    COUNT(*) FILTER (WHERE "Total Cost" IS NULL) AS cost_missing,
    COUNT(*) FILTER (WHERE "Total Profit" IS NULL) AS profit_missing
FROM sales_data;


-- Check date range
SELECT
    MIN("Order Date") AS earliest_order_date,
    MAX("Order Date") AS latest_order_date,
    MIN("Ship Date") AS earliest_ship_date,
    MAX("Ship Date") AS latest_ship_date
FROM sales_data;


/* ============================================================
   2. OVERALL BUSINESS KPIs
   ============================================================ */

SELECT
    COUNT(DISTINCT "Order ID") AS total_orders,
    SUM("Units Sold") AS total_units_sold,
    SUM("Total Revenue") AS total_revenue,
    SUM("Total Cost") AS total_cost,
    SUM("Total Profit") AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent,

    ROUND(
        SUM("Total Revenue")
        / NULLIF(COUNT(DISTINCT "Order ID"), 0),
        2
    ) AS average_order_value,

    ROUND(AVG("Unit Price"), 2) AS average_unit_price,

    ROUND(AVG("Unit Cost"), 2) AS average_unit_cost,

    ROUND(
        SUM("Total Profit")
        / NULLIF(COUNT(DISTINCT "Order ID"), 0),
        2
    ) AS average_profit_per_order,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Units Sold"), 0),
        2
    ) AS profit_per_unit,

    ROUND(AVG("Shipping Days"), 2) AS average_shipping_days

FROM sales_data;


/* ============================================================
   3. PROFIT VALIDATION
   ============================================================ */

SELECT
    SUM("Total Revenue") AS total_revenue,
    SUM("Total Cost") AS total_cost,
    SUM("Total Profit") AS stored_total_profit,
    SUM("Total Revenue" - "Total Cost") AS calculated_total_profit
FROM sales_data;


/* ============================================================
   4. REGION-WISE ANALYSIS
   ============================================================ */

SELECT
    "Region",
    COUNT(DISTINCT "Order ID") AS total_orders,
    SUM("Units Sold") AS total_units_sold,
    ROUND(SUM("Total Revenue"), 2) AS total_revenue,
    ROUND(SUM("Total Cost"), 2) AS total_cost,
    ROUND(SUM("Total Profit"), 2) AS total_profit,
    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent
FROM sales_data
GROUP BY "Region"
ORDER BY total_revenue DESC;

SELECT
    COUNT(DISTINCT "Order ID") AS total_orders,
    SUM("Units Sold") AS total_units_sold,
    ROUND(SUM("Total Revenue"), 2) AS total_revenue,
    ROUND(SUM("Total Cost"), 2) AS total_cost,
    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent,

    ROUND(
        SUM("Total Revenue")
        / NULLIF(COUNT(DISTINCT "Order ID"), 0),
        2
    ) AS average_order_value,

    ROUND(AVG("Unit Price"), 2) AS average_unit_price,

    ROUND(AVG("Unit Cost"), 2) AS average_unit_cost,

    ROUND(
        SUM("Total Profit")
        / NULLIF(COUNT(DISTINCT "Order ID"), 0),
        2
    ) AS average_profit_per_order,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Units Sold"), 0),
        2
    ) AS profit_per_unit,

    ROUND(AVG("Shipping Days"), 2) AS average_shipping_days

FROM sales_data;


SELECT
    "Region",
    COUNT(DISTINCT "Order ID") AS total_orders,
    SUM("Units Sold") AS total_units_sold,
    ROUND(SUM("Total Revenue"), 2) AS total_revenue,
    ROUND(SUM("Total Cost"), 2) AS total_cost,
    ROUND(SUM("Total Profit"), 2) AS total_profit,
    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent
FROM sales_data
GROUP BY "Region"
ORDER BY total_revenue DESC;


/* ============================================================
   5. COUNTRY-WISE ANALYSIS
   ============================================================ */

SELECT
    "Country",

    COUNT(DISTINCT "Order ID") AS total_orders,

    SUM("Units Sold") AS total_units_sold,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Cost"), 2) AS total_cost,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Country"

ORDER BY total_revenue DESC;


/* ============================================================
   6. ITEM TYPE ANALYSIS
   ============================================================ */

SELECT
    "Item Type",

    COUNT(DISTINCT "Order ID") AS total_orders,

    SUM("Units Sold") AS total_units_sold,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Cost"), 2) AS total_cost,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Item Type"

ORDER BY total_revenue DESC;


/* ============================================================
   7. SALES CHANNEL ANALYSIS
   ============================================================ */

SELECT
    "Sales Channel",

    COUNT(DISTINCT "Order ID") AS total_orders,

    SUM("Units Sold") AS total_units_sold,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Cost"), 2) AS total_cost,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Sales Channel"

ORDER BY total_revenue DESC;


/* ============================================================
   8. YEAR-WISE ANALYSIS
   ============================================================ */

SELECT
    "Order Year",

    COUNT(DISTINCT "Order ID") AS total_orders,

    SUM("Units Sold") AS total_units_sold,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Cost"), 2) AS total_cost,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Order Year"

ORDER BY "Order Year";


/* ============================================================
   9. MONTHLY ANALYSIS
   ============================================================ */

SELECT
    "Year-Month",

    COUNT(DISTINCT "Order ID") AS total_orders,

    SUM("Units Sold") AS total_units_sold,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Cost"), 2) AS total_cost,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Year-Month"

ORDER BY "Year-Month";


/* ============================================================
   10. QUARTER-WISE ANALYSIS
   ============================================================ */

SELECT
    "Order Year",
    "Order Quarter",

    COUNT(DISTINCT "Order ID") AS total_orders,

    SUM("Units Sold") AS total_units_sold,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Cost"), 2) AS total_cost,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY
    "Order Year",
    "Order Quarter"

ORDER BY
    "Order Year",
    "Order Quarter";


/* ============================================================
   11. TOP 10 COUNTRIES BY REVENUE
   ============================================================ */

SELECT
    "Country",

    COUNT(DISTINCT "Order ID") AS total_orders,

    SUM("Units Sold") AS total_units_sold,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Country"

ORDER BY total_revenue DESC

LIMIT 10;



/* ============================================================
   12. TOP 10 ITEM TYPES BY PROFIT
   ============================================================ */

SELECT
    "Item Type",

    COUNT(DISTINCT "Order ID") AS total_orders,

    SUM("Units Sold") AS total_units_sold,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Item Type"

ORDER BY total_profit DESC

LIMIT 10;



/* ============================================================
   13. TOP 10 COUNTRIES BY PROFIT
   ============================================================ */

SELECT
    "Country",

    COUNT(DISTINCT "Order ID") AS total_orders,

    SUM("Units Sold") AS total_units_sold,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Country"

ORDER BY total_profit DESC

LIMIT 10;


/* ============================================================
   14. REGIONS WITH REVENUE ABOVE 10 BILLION
   ============================================================ */

SELECT
    "Region",

    COUNT(DISTINCT "Order ID") AS total_orders,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Region"

HAVING SUM("Total Revenue") > 10000000000

ORDER BY total_revenue DESC;


/* ============================================================
   15. REGIONS WITH PROFIT ABOVE 5 BILLION
   ============================================================ */

SELECT
    "Region",

    COUNT(DISTINCT "Order ID") AS total_orders,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Region"

HAVING SUM("Total Profit") > 5000000000

ORDER BY total_profit DESC;


/* ============================================================
   16. COUNTRY PROFIT RANKING
   ============================================================ */

WITH country_performance AS (

    SELECT
        "Country",

        COUNT(DISTINCT "Order ID") AS total_orders,

        ROUND(SUM("Total Revenue"), 2) AS total_revenue,

        ROUND(SUM("Total Profit"), 2) AS total_profit,

        ROUND(
            SUM("Total Profit")
            / NULLIF(SUM("Total Revenue"), 0) * 100,
            2
        ) AS profit_margin_percent

    FROM sales_data

    GROUP BY "Country"
)

SELECT
    RANK() OVER (
        ORDER BY total_profit DESC
    ) AS profit_rank,

    "Country",
    total_orders,
    total_revenue,
    total_profit,
    profit_margin_percent

FROM country_performance

ORDER BY profit_rank
LIMIT 10;



/* ============================================================
   17. TOP COUNTRIES BY PROFIT MARGIN
   Minimum 500 orders
   ============================================================ */

SELECT
    "Country",

    COUNT(DISTINCT "Order ID") AS total_orders,

    ROUND(SUM("Total Revenue"), 2) AS total_revenue,

    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS profit_margin_percent

FROM sales_data

GROUP BY "Country"

HAVING COUNT(DISTINCT "Order ID") >= 500

ORDER BY profit_margin_percent DESC

LIMIT 10;


/* ============================================================
   18. DATA QUALITY & BUSINESS RULE VALIDATION
   ============================================================ */

-- Revenue validation
SELECT
    COUNT(*) AS revenue_mismatch_rows
FROM sales_data
WHERE ROUND("Total Revenue", 2) <>
      ROUND("Units Sold" * "Unit Price", 2);


-- Cost validation
SELECT
    COUNT(*) AS cost_mismatch_rows
FROM sales_data
WHERE ROUND("Total Cost", 2) <>
      ROUND("Units Sold" * "Unit Cost", 2);


-- Profit validation
SELECT
    COUNT(*) AS profit_mismatch_rows
FROM sales_data
WHERE ROUND("Total Profit", 2) <>
      ROUND("Total Revenue" - "Total Cost", 2);


-- Shipping date validation
SELECT
    COUNT(*) AS invalid_shipping_days
FROM sales_data
WHERE "Ship Date" < "Order Date";


-- Negative values validation
SELECT
    COUNT(*) FILTER (WHERE "Units Sold" < 0) AS negative_units,
    COUNT(*) FILTER (WHERE "Unit Price" < 0) AS negative_unit_price,
    COUNT(*) FILTER (WHERE "Unit Cost" < 0) AS negative_unit_cost,
    COUNT(*) FILTER (WHERE "Total Revenue" < 0) AS negative_revenue,
    COUNT(*) FILTER (WHERE "Total Cost" < 0) AS negative_cost,
    COUNT(*) FILTER (WHERE "Total Profit" < 0) AS negative_profit
FROM sales_data;


/* ============================================================
   19. FINAL NULL / MISSING VALUE VALIDATION
   ============================================================ */

SELECT
    COUNT(*) FILTER (WHERE "Region" IS NULL) AS region_missing,
    COUNT(*) FILTER (WHERE "Country" IS NULL) AS country_missing,
    COUNT(*) FILTER (WHERE "Item Type" IS NULL) AS item_type_missing,
    COUNT(*) FILTER (WHERE "Sales Channel" IS NULL) AS sales_channel_missing,
    COUNT(*) FILTER (WHERE "Order Priority" IS NULL) AS priority_missing,
    COUNT(*) FILTER (WHERE "Order Date" IS NULL) AS order_date_missing,
    COUNT(*) FILTER (WHERE "Ship Date" IS NULL) AS ship_date_missing,
    COUNT(*) FILTER (WHERE "Units Sold" IS NULL) AS units_sold_missing,
    COUNT(*) FILTER (WHERE "Unit Price" IS NULL) AS unit_price_missing,
    COUNT(*) FILTER (WHERE "Unit Cost" IS NULL) AS unit_cost_missing,
    COUNT(*) FILTER (WHERE "Total Revenue" IS NULL) AS revenue_missing,
    COUNT(*) FILTER (WHERE "Total Cost" IS NULL) AS cost_missing,
    COUNT(*) FILTER (WHERE "Total Profit" IS NULL) AS profit_missing
FROM sales_data;


/* ============================================================
   20. FINAL DATABASE SUMMARY
   ============================================================ */

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT "Order ID") AS total_orders,
    COUNT(DISTINCT "Country") AS total_countries,
    COUNT(DISTINCT "Region") AS total_regions,
    COUNT(DISTINCT "Item Type") AS total_item_types,
    COUNT(DISTINCT "Sales Channel") AS total_sales_channels,

    MIN("Order Date") AS earliest_order_date,
    MAX("Order Date") AS latest_order_date,

    ROUND(SUM("Units Sold"), 2) AS total_units_sold,
    ROUND(SUM("Total Revenue"), 2) AS total_revenue,
    ROUND(SUM("Total Cost"), 2) AS total_cost,
    ROUND(SUM("Total Profit"), 2) AS total_profit,

    ROUND(
        SUM("Total Profit")
        / NULLIF(SUM("Total Revenue"), 0) * 100,
        2
    ) AS overall_profit_margin

FROM sales_data;