# 📊 CSV to Data Warehouse ETL Pipeline using Airflow

This project demonstrates a simple yet production-style **ETL pipeline** that:
- 📥 **Extracts** data from a CSV file
- 🔄 **Transforms** it using Python (Pandas)
- 🛢️ **Loads** it into a PostgreSQL data warehouse
- ⏰ Uses **Apache Airflow** for task orchestration and scheduling



## 🚀 Tech Stack

| Component       | Tech                                |
|----------------|-------------------------------------|
| Language        | Python 3.x                          |
| Workflow Engine | Apache Airflow                     |
| Database        | PostgreSQL                         |
| Data Processing | Pandas                              |
| Containerization| Docker + Docker Compose            |
| Scheduling      | Airflow DAGs (daily trigger)       |



## 📁 Project Structure

```plaintext
csv-datawarehouse-etl-airflow/
├── dags/
│   └── etl_pipeline.py         # Airflow DAG
├── data/
│   └── sales_data.csv          # Sample input data
├── scripts/
│   ├── extract.py              # Extract from CSV
│   ├── transform.py            # Clean & enhance data
│   └── load.py                 # Load into PostgreSQL
├── docker-compose.yml          # Docker for Airflow + Postgres
├── requirements.txt            # Python libraries
└── README.md

```

## Author
 [**Aakaash M S**](https://github.com/msaakaash)





