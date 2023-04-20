from datetime import datetime, timedelta
import random

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

#TODO authenticate to github repo, git add. and git commit the file with dot
#TODO do it N times based on mimic_n_commits function

default_args={
    'owner' : 'active_developer',
    'retries' : 5,
    'retry_interval' : timedelta(minutes=2)
}

# def get_n_of_commits(ti):
#     n_commits=random.randint(1,10)
#     ti.xcom_push(key="n_commits", value=n_commits)

def make_change_to_file():
    with open('dags/git_dir/file_to_push.txt', 'a') as file_with_updates:
        file_with_updates.write('.')     
    print(f'Wow, you\'ve done a change to the file, added {n_commits} dots')

with DAG(
    dag_id='mimic_activity_v12',
    default_args=default_args,
    start_date=datetime(2023,4, 19),
    schedule_interval='@daily'
) as dag:

    chain_operators=[]
    n_commits=1

    for n in range(n_commits):
        task1=PythonOperator(
        task_id = f'make_{n}th_change_to_file',
        python_callable=make_change_to_file
        )
        chain_operators.append(task1)

        task2=BashOperator(
            task_id = f'test_call_{n}_out_of_{n_commits}',
            bash_command = 'pwd; sudo mkdir $active_dev/test_dir'
        )
        chain_operators.append(task2)

    for i, val in enumerate(chain_operators[:-1]):
        val.set_downstream(chain_operators[i+1])
