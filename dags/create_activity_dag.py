from datetime import datetime

from airflow.decorators import task, dag

#TODO Find a way to create folder
#TODO authenticate to github repo, git add. and git commit the file with dot
#TODO do it N times based on mimic_n_commits function

default_args={
    'owner' : 'active_developer',
    'retries' : 5
}

@task
def get_n_of_commits():
    import random
    n = random.randint(2, 10)
    my_list = list(range(1, n+1))
    return my_list

@task
def do_n_commits(n):
    # here will be code for committing to repo
    print(f'This is {n}th commit')

@dag(
    dag_id='mimic_activity_v19',
    default_args=default_args,
    start_date=datetime(2023,4, 15),
    schedule_interval='@daily'
)

def my_dag():
    do_n_commits.expand(n=get_n_of_commits())

dag=my_dag()