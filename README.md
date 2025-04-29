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
│   └── etl_pipeline.py        
├── data/
│   └── sales_data.csv         
├── scripts/
│   ├── extract.py             
│   ├── transform.py            
│   └── load.py                 
├── docker-compose.yml          
├── requirements.txt           
└── README.md

```

## Author
 [**Aakaash M S**](https://github.com/msaakaash)





