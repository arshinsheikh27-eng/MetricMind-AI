# MetricMind-AI

## Agentic Semantic BI Engine

MetricMind-AI is an AI-assisted Business Intelligence platform that combines data engineering, semantic analytics, backend APIs, visualization, and AI-assisted natural-language interaction.

The project provides an end-to-end analytics pipeline using PostgreSQL, dbt, FastAPI, Next.js, React, Recharts, LangChain, and OpenAI API integration.

---

## Project Overview

The implemented analytics pipeline is:

**PostgreSQL → dbt → Analytics Layer → FastAPI → Next.js Dashboard**

The project uses a cleaned sales dataset containing **99,508 records** and provides business analytics including revenue, cost, profit, orders, units sold, regional performance, product performance, channel performance, and quarterly performance.

An AI assistant layer is also integrated for natural-language business questions.

---

## Objectives

- Build an end-to-end business analytics pipeline.
- Store and manage sales data using PostgreSQL.
- Transform and model data using dbt.
- Create reusable analytical models and business metrics.
- Provide analytics through REST APIs.
- Develop an interactive BI dashboard.
- Integrate an AI-assisted natural-language question interface.
- Use Git and GitHub for collaborative team development.

---

## Technology Stack

| Layer | Technology |
|---|---|
| Programming | Python, SQL, TypeScript |
| Database | PostgreSQL |
| Data Transformation | dbt |
| Backend | FastAPI |
| AI / Agent | LangChain, OpenAI API |
| Frontend | Next.js, React |
| Visualization | Recharts |
| Version Control | Git, GitHub |

---

## Dataset

The project uses the MetricMind cleaned sales dataset.

- **Records:** 99,508
- **Source format:** CSV
- **Database:** PostgreSQL
- **Main raw table:** `sales_data`

Important business fields include:

- Region
- Country
- Item Type
- Sales Channel
- Order Date
- Order ID
- Units Sold
- Unit Price
- Unit Cost
- Total Revenue
- Total Cost
- Total Profit
- Profit Margin

---

## Data Architecture

### PostgreSQL Data Layer

The cleaned sales dataset is loaded into PostgreSQL.

The database contains the raw sales data and the analytical tables and views generated through dbt.

### dbt Transformation Layer

The dbt project contains six models:

1. `stg_sales`
2. `dim_date`
3. `dim_geography`
4. `dim_product`
5. `fact_sales`
6. `metrics_sales`

The staging model standardizes the raw database fields.

Fact and dimension models provide a structured analytical data model.

The metrics model provides reusable business-level aggregations.

---

## dbt Validation

The complete dbt project has been successfully executed.

```text
PASS = 6
WARN = 0
ERROR = 0
SKIP = 0

All six dbt models were created successfully.

Validated models:

stg_sales
dim_date
dim_geography
dim_product
fact_sales
metrics_sales
Backend

The backend is implemented using FastAPI.

Available Endpoints
/
 /health
 /analytics/summary
 /analytics/revenue-by-region
 /analytics/profit-by-product
 /analytics/sales-by-channel
 /analytics/sales-by-quarter
 /ask
Analytics Services

The backend provides:

Overall business summary
Revenue by region
Profit by product
Sales by channel
Sales by quarter
AI question endpoint

The analytics services retrieve business data from PostgreSQL.

Frontend Dashboard

The frontend is implemented using Next.js and React.

KPI Metrics
Total Revenue
Total Cost
Total Profit
Total Units Sold
Total Orders
Profit Margin
Average Order Revenue
Average Selling Price
Visual Analytics
Revenue by Region
Profit by Product
Sales by Channel
Sales by Quarter
AI Interface

The dashboard also contains an Ask AI interface connected to the backend /ask endpoint.

AI Assistant

MetricMind-AI contains an AI-assisted analytics architecture consisting of:

Question Parser
Business Analytics Prompts
Semantic Analytics Tool
MetricMind Agent
OpenAI Integration

The intended architecture is:

User Question
      ↓
Question Parser
      ↓
Metric / Dimension Identification
      ↓
Semantic Analytics Layer
      ↓
Database Query
      ↓
Business Result
      ↓
AI Response

The AI layer is designed to support natural-language business analytics.

Current AI Limitation

The OpenAI API integration is implemented and the configured API key is detected successfully.

However, the currently configured OpenAI API account has exhausted its available API credits.

Therefore, live LLM responses through the /ask endpoint require an account with available API credits.

This is an external API quota/billing limitation.

The PostgreSQL-based analytics APIs and dashboard continue to operate independently.

Validation Summary
Database
99,508 sales records
dbt
6 models
PASS = 6
WARN = 0
ERROR = 0
Backend

The FastAPI backend has been locally validated.

The health endpoint reports a healthy database configuration and the analytics endpoints return database-driven results.

Frontend

The Next.js dashboard has been locally validated.

KPI values and analytics charts are displayed using the FastAPI backend.

Example Analytics Output

The integrated analytics API provides metrics such as:

Total Revenue:       132,919,637,175.76
Total Cost:           93,709,135,984.60
Total Profit:         39,210,501,191.16
Total Units Sold:        497,655,981
Total Orders:               99,508
Profit Margin:              29.50%

These values are generated from the project database.

Project Structure
MetricMind-AI/
│
├── Dataset/
│   ├── SQL/
│   ├── cleaned_data/
│   └── documentation/
│
├── ai/
│   ├── agents/
│   ├── analysis/
│   ├── prompts/
│   └── tools/
│
├── agent/
│
├── app/
│   ├── main.py
│   ├── models.py
│   └── services/
│
├── frontend/
│   ├── app/
│   ├── public/
│   └── package.json
│
├── metricmind_dbt/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   ├── dbt_project.yml
│   └── README.md
│
├── documentation/
│
├── requirements.txt
└── README.md
Team Development

The project was developed collaboratively using Git and GitHub.

Each team member worked on assigned modules using individual branches.

The Team Lead integration branch was used to integrate and coordinate:

Data and Semantic Layer
AI Agent
Backend
Frontend
Documentation

The integration was performed while preserving team-member contributions and Git history.

Team Lead Responsibilities

The Team Lead handled:

Repository coordination
Branch coordination
Task allocation
Progress monitoring
Team communication
Module integration
Integration testing
Review preparation
Documentation coordination
Project Review Demo Flow

The recommended project demonstration flow is:

Introduce the MetricMind-AI objective.
Explain the system architecture.
Show the PostgreSQL sales dataset.
Show the dbt project and six models.
Show successful dbt execution.
Show the FastAPI backend.
Demonstrate the analytics API.
Open the Next.js dashboard.
Demonstrate KPI cards and charts.
Explain the AI assistant architecture.
Explain the current OpenAI credit limitation.
Discuss future enhancements.
Future Enhancements
Complete dynamic natural-language-to-query execution.
Add advanced dashboard filters.
Add additional business metrics and dimensions.
Add dashboard drill-down capabilities.
Add authentication and authorization.
Expand automated data-quality testing.
Improve AI-generated business explanations.
Deploy the application to the cloud.
Project Status
Core Components
PostgreSQL database: Implemented
Sales dataset integration: Implemented
dbt transformation layer: Implemented
Analytical models: Implemented
FastAPI backend: Implemented
Analytics APIs: Implemented
Next.js dashboard: Implemented
KPI and chart visualization: Implemented
AI agent architecture: Implemented
OpenAI integration: Implemented
Live OpenAI response: Pending API credits
Documentation: Implemented
Overall

The core MetricMind-AI analytics pipeline has been integrated and locally validated.

PostgreSQL
    ↓
dbt
    ↓
Analytics Layer
    ↓
FastAPI
    ↓
Next.js Dashboard

The project is prepared for the Week 3–4 project review.