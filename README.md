# MetricMind Backend

MetricMind is an Agentic Semantic BI platform that provides business analytics through a FastAPI backend, PostgreSQL database, dbt transformations, and AI-powered natural-language analysis.

## Backend Responsibilities

The backend is responsible for:

- Providing REST APIs using FastAPI
- Connecting to PostgreSQL
- Executing analytics queries
- Providing KPI and business metrics
- Providing analytics data for the frontend
- Handling natural-language questions through the LLM service
- Enabling frontend-to-backend communication using CORS

## Technology Stack

- Python
- FastAPI
- Uvicorn
- PostgreSQL
- psycopg2
- Pydantic
- python-dotenv
- OpenAI API
- dbt

## Project Structure

```text
MetricMind-AI/
│
├── app/
│   ├── main.py
│   ├── models.py
│   │
│   └── services/
│       ├── analytics_service.py
│       └── llm_service.py
│
├── Dataset/
│   ├── cleaned_data/
│   └── SQL/
│
├── metricmind_dbt/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   └── dbt_project.yml
│
├── frontend/
│
├── .env.example
├── requirements.txt
└── README.md