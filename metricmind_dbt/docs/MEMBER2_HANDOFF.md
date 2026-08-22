\# Member 2 Handoff - Data + Semantic Layer



\## 1. Owner



Member: Member 2 - Data + Semantic Layer



Project: MetricMind AI



Branch: member2-data-semantic



\---



\## 2. PostgreSQL Configuration



Database: metricmind

Schema: public

Host: localhost

Port: 5432



Main source table:

\- raw\_sales



\---



\## 3. Data Flow



Cleaned CSV

|

v

PostgreSQL raw\_sales

|

v

dbt staging

|

v

stg\_sales

|

v

fact\_sales + dimensions

|

v

metrics\_sales

|

v

AI / Backend / Power BI

