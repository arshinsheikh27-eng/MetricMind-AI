# MetricMind AI - dbt Data and Semantic Layer

## Overview

This dbt project transforms the cleaned MetricMind sales dataset in PostgreSQL into a structured analytics model for reporting and Power BI.

## Data Flow

Raw CSV
-> Python Data Cleaning
-> PostgreSQL raw_sales
-> dbt staging
-> stg_sales
-> Fact and Dimension Models
-> fact_sales + dim_date + dim_geography + dim_product
-> metrics_sales
-> Power BI / Analytics

## PostgreSQL Configuration

Database: metricmind

Schema: public

Source Table:
- raw_sales

## dbt Models

### Staging

- stg_sales
  - Materialized as a view
  - Contains 99,508 sales records

### Fact

- fact_sales
  - Materialized as a table
  - Contains 99,508 records

### Dimensions

- dim_date
  - 2,766 records

- dim_geography
  - 375 records

- dim_product
  - 12 records

### Metrics

- metrics_sales
  - Materialized as a view
  - Provides aggregated sales metrics for reporting

## Validation

### dbt Debug

- All checks passed

### dbt Run

- 6 models completed successfully
- 0 errors

### dbt Test

- 2 tests passed
- 0 errors

## Key Business Metrics

Current fact table totals:

- Revenue: 132,919,637,175.76
- Cost: 93,709,135,984.60
- Profit: 39,210,501,191.16
- Units Sold: 497,655,981
- Orders: 99,508

## Running the Project

From the metricmind_dbt directory:

```text
dbt debug
dbt run
dbt test

## Team Handoff

The Power BI and reporting layer should use the dbt-generated PostgreSQL models rather than directly using the raw CSV.

Recommended reporting tables and views:

- fact_sales
- dim_date
- dim_geography
- dim_product
- metrics_sales