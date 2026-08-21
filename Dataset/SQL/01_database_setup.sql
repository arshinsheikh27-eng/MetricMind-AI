-- ============================================================
-- MetricMind-AI
-- Database Setup
-- PostgreSQL
-- ============================================================


CREATE TABLE sales_data (
    "Region" TEXT,
    "Country" TEXT,
    "Item Type" TEXT,
    "Sales Channel" TEXT,
    "Order Priority" TEXT,
    "Order Date" DATE,
    "Order ID" BIGINT,
    "Ship Date" DATE,
    "Units Sold" INTEGER,
    "Unit Price" NUMERIC(12,2),
    "Unit Cost" NUMERIC(12,2),
    "Total Revenue" NUMERIC(14,2),
    "Total Cost" NUMERIC(14,2),
    "Total Profit" NUMERIC(14,2),
    "Shipping Days" INTEGER,
    "Profit Margin %" NUMERIC(8,2),
    "Order Year" INTEGER,
    "Month Name" TEXT,
    "Year-Month" TEXT,
    "Order Month" INTEGER,
    "Order Quarter" TEXT
);

