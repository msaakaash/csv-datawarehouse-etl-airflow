from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
}

def run_pipeline():
    from scripts.extract import extract
    from scripts.transform import transform
    from scripts.load import load

    df = extract('/opt/airflow/data/sales_data.csv')
    df = transform(df)
    conn_params = {
        'dbname': 'salesdb',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'postgres',
        'port': '5432'
    }
    load(df, conn_params)

with DAG('etl_pipeline', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    task = PythonOperator(
        task_id='run_etl',
        python_callable=run_pipeline
    )
