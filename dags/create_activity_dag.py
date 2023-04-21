from datetime import datetime, timedelta
import random

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

#TODO Find a way to pass ti.argument to the cycle
#TODO Find a way to create folder
#TODO authenticate to github repo, git add. and git commit the file with dot
#TODO do it N times based on mimic_n_commits function

default_args={
    'owner' : 'active_developer',
    'retries' : 5,
    'retry_interval' : timedelta(minutes=2)
}

def get_n_of_commits(ti):
    n_commits=random.randint(1,10)
    ti.xcom_push(key="n_commits", value=n_commits)

def do_n_commits(ti):
    n_commits=ti.xcom_pull(task_ids='get_n_of_commits', key="n_commits")
    for n in range(n_commits):
        print(f"Doing {n}-th commit of {n_commits}")


with DAG(
    dag_id='mimic_activity_v14',
    default_args=default_args,
    start_date=datetime(2023,4, 19),
    schedule_interval='@daily'
) as dag:
    task1=PythonOperator(
        task_id='get_n_of_commits',
        python_callable=get_n_of_commits
    )

    task2=PythonOperator(
        task_id='do_n_commits',
        python_callable=do_n_commits
    )

    task1.set_downstream(task2)