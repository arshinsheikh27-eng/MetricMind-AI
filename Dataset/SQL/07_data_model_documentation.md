# Data Model

## Current Architecture

The current MetricMind implementation uses a centralized sales transaction table and a semantic reporting view.

sales_data
    |
    v
vw_sales_semantic

## Main Data Table

### sales_data

sales_data is the primary transactional table containing the cleaned sales and logistics records.

It contains fields related to:

- Region
- Country
- Item Type
- Sales Channel
- Order Priority
- Order Date
- Order ID
- Units Sold
- Unit Price
- Unit Cost
- Total Revenue
- Total Cost
- Total Profit
- Shipping Days
- Profit Margin %
- Order Year
- Month Name
- Year-Month
- Order Month
- Order Quarter

## Semantic Layer

### vw_sales_semantic

vw_sales_semantic is a business-friendly view created from sales_data.

It provides the existing sales fields along with business classifications such as:

- Profit Category
  - High Profit
  - Medium Profit
  - Low Profit

- Shipping Category
  - Fast
  - Normal
  - Slow

The semantic view is intended to provide a simpler and more business-friendly data layer for analytics, dashboards, and the AI agent.

## Current Implementation vs Planned Model

The project documentation previously described a star-schema model containing:

- Fact_Sales
- Dim_Date
- Dim_Country
- Dim_Product
- Dim_Channel

These dimension tables are not currently implemented as separate PostgreSQL tables in the project.

The current implementation is:

sales_data -> vw_sales_semantic

A dimensional/star-schema architecture can be considered as a future enhancement if required by the project.

## Key Business Measures

The main business measures available from the sales data are:

- Total Revenue
- Total Cost
- Total Profit
- Units Sold
- Profit Margin %

## Key Dimensions

The main dimensions available for analysis are:

- Order Date
- Year
- Month
- Quarter
- Country
- Region
- Item Type
- Sales Channel
- Order Priority

