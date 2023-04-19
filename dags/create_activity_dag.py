from datetime import datetime, timedelta
import random

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

#TODO authenticate to github repo, git add. and git commit the file with dot
#TODO do it N times based on mimic_n_commits function
#TODO change execution interval to daily

default_args={
    'owner' : 'active_developer',
    'retries' : 5,
    'retry_interval' : timedelta(minutes=2)
}

def mimic_n_commits():
    #n_commits=random.randint(1,10)
    n_commits=1
    with open('dags/git_dir/file_to_push.txt', 'a') as file_with_updates:
        file_with_updates.write(n_commits*'.')     
    print(f'Wow, you\'ve done a change to the file, added {n_commits} dots')

with DAG(
    dag_id='mimic_activity_v8',
    default_args=default_args,
    start_date=datetime(2023,4, 18),
    schedule_interval='@daily'
) as dag:
    task1=PythonOperator(
        task_id = 'test_operator',
        python_callable=mimic_n_commits
    )

    task2=BashOperator(
        task_id = 'navigate_to_dir',
        bash_command = 'ls'
    )

    task3=BashOperator(
        task_id = 'add_file_to_staging',
        bash_command = 'git add .'
    )

    task4=BashOperator(
        task_id = 'commit_file',
        bash_command = 'git commit -m "does it work?"'
    )

    task5=BashOperator(
        task_id = 'push_file_to_remote_repo',
        bash_command = 'git push -u origin main'
    )

    task1>>task2
