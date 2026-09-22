# MetricMind-AI
## Week 3–4 Project Review Presentation

---

# Slide 1 — Title

## MetricMind-AI

### Agentic Semantic BI Engine

**Project:** Data Analytics Internship  
**Team:** Group 2  
**Role:** Team Lead  
**Project:** Month 1 – MetricMind-AI

---

# Slide 2 — Problem Statement

Traditional Business Intelligence systems often require users to understand databases, SQL queries, dashboards, and predefined reports.

MetricMind-AI aims to provide a more accessible analytics experience by combining:

- Structured business data
- Semantic analytics
- Backend APIs
- Interactive dashboards
- AI-assisted natural-language interaction

The goal is to allow business users to understand sales performance through a unified analytics platform.

---

# Slide 3 — Project Objectives

- Build an end-to-end Business Intelligence pipeline.
- Store sales data in PostgreSQL.
- Transform data using dbt.
- Create reusable analytical models.
- Develop business metrics.
- Provide analytics through FastAPI.
- Build an interactive Next.js dashboard.
- Integrate an AI-assisted question interface.
- Use Git and GitHub for collaborative development.

---

# Slide 4 — Technology Stack

| Component | Technology |
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

# Slide 5 — System Architecture

```text
                    User
                      |
                      v
             Next.js Dashboard
                      |
                      v
                 FastAPI
                /       \
               /         \
              v           v
      Analytics APIs     AI / Ask
              |            |
              v            v
        Analytics Layer  AI Agent
              |            |
              v            v
                 PostgreSQL
                      |
                      v
                     dbt
                      |
                      v
                Sales Dataset

The architecture connects data engineering, analytics, backend services, visualization, and AI interaction.

Slide 6 — Dataset

The project uses the MetricMind cleaned sales dataset.

Dataset Statistics
Total records: 99,508
Format: CSV
Database: PostgreSQL
Main table: sales_data
Important Fields
Region
Country
Item Type
Sales Channel
Order Date
Order ID
Units Sold
Unit Price
Unit Cost
Total Revenue
Total Cost
Total Profit
Profit Margin
Slide 7 — Data & Semantic Layer

The data layer uses PostgreSQL and dbt.

dbt Models
stg_sales
dim_date
dim_geography
dim_product
fact_sales
metrics_sales
Purpose
Standardize raw data.
Create analytical dimensions.
Create fact tables.
Generate reusable business metrics.
Provide a structured analytics layer for the backend.
Validation
PASS = 6
WARN = 0
ERROR = 0
SKIP = 0

All six dbt models were successfully executed.

Slide 8 — Backend

The backend is developed using FastAPI.

Main Endpoints
/
 /health
 /analytics/summary
 /analytics/revenue-by-region
 /analytics/profit-by-product
 /analytics/sales-by-channel
 /analytics/sales-by-quarter
 /ask
Backend Responsibilities
Connect to PostgreSQL.
Retrieve analytical data.
Provide REST APIs.
Return business metrics.
Provide AI question handling.
Slide 9 — Analytics Dashboard

The frontend is developed using Next.js and React.

KPI Cards
Total Revenue
Total Cost
Total Profit
Total Units Sold
Total Orders
Profit Margin
Average Order Revenue
Average Selling Price
Charts
Revenue by Region
Profit by Product
Sales by Channel
Sales by Quarter

The dashboard retrieves live analytical data from the FastAPI backend.

Slide 10 — AI Assistant

MetricMind-AI includes an AI-assisted analytics architecture.

Components
Question Parser
Business Analytics Prompts
Semantic Analytics Tool
MetricMind Agent
OpenAI Integration
Intended Flow
User Question
      |
      v
Question Parser
      |
      v
Metric / Dimension Identification
      |
      v
Semantic Analytics Layer
      |
      v
Database Query
      |
      v
Business Result
      |
      v
AI Response

The purpose is to allow users to ask business questions using natural language.

Slide 11 — Example Analytics Results

The integrated analytics API currently provides:

Total Revenue:       132,919,637,175.76
Total Cost:           93,709,135,984.60
Total Profit:         39,210,501,191.16
Total Units Sold:        497,655,981
Total Orders:               99,508
Profit Margin:              29.50%

These values are generated from the PostgreSQL database.

Slide 12 — Team Contribution

The project was developed collaboratively using Git and GitHub.

Module Contributions

Data & Semantic Layer

PostgreSQL database setup
Dataset integration
dbt models
Semantic analytics layer

AI Agent

Question parser
Semantic tool
Agent architecture
AI prompts
OpenAI integration

Backend

FastAPI application
Analytics services
API endpoints
Database integration

Frontend

Next.js dashboard
KPI cards
Charts
Ask AI interface

Team Lead

Repository coordination
Branch management
Task allocation
Progress monitoring
Module integration
Testing coordination
Review preparation
Documentation
Slide 13 — Current Project Status
Implemented
PostgreSQL database
Sales dataset integration
dbt transformation layer
Six analytical models
FastAPI backend
Analytics APIs
Next.js dashboard
KPI visualization
Charts
AI agent architecture
OpenAI API integration
Project documentation
Current External Limitation

The configured OpenAI API account has exhausted its available API credits.

Therefore, live LLM responses through /ask require an account with available API credits.

The PostgreSQL analytics APIs and dashboard continue to operate independently.

Slide 14 — Future Enhancements
Complete dynamic natural-language-to-query execution.
Add advanced dashboard filters.
Add additional business metrics.
Add more analytical dimensions.
Add dashboard drill-down capabilities.
Expand automated data-quality testing.
Improve AI-generated business explanations.
Add authentication and authorization.
Deploy the application to the cloud.
Slide 15 — Conclusion

MetricMind-AI integrates:

PostgreSQL
      |
      v
     dbt
      |
      v
Analytics Layer
      |
      v
   FastAPI
      |
      v
Next.js Dashboard
      |
      v
AI-assisted Analytics

The core analytics pipeline has been integrated and locally validated.

The project is prepared for the Week 3–4 project review.

Thank You