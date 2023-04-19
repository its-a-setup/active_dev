from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args={
    'owner' : 'active_developer',
    'retries' : 5,
    'retry_interval' : timedelta(minutes=2)
}

def test_func():
    print('test is successful')

with DAG(
    dag_id='mimic_activity_v1',
    default_args=default_args,
    start_date=datetime(2023,4, 19),
    schedule_interval='@hourly'
) as dag:
    task1=PythonOperator(
        task_id = 'test_operator',
        python_callable=test_func
    )
    task1