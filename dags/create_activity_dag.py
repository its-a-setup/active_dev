import os
from dotenv import load_dotenv
from datetime import datetime

from github import Github
from airflow.decorators import task, dag

#TODO change create_file to update_file
#TODO find proper way to name files uniquely
#TODO get the name of repo without relying on order
#TODO delete previous file when new one was committed, to save space

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
    import random
    import time
    load_dotenv()

    GITHUB_ACCESS_TOKEN=os.getenv('GITHUB_ACCESS_TOKEN')
    g = Github(GITHUB_ACCESS_TOKEN)
    user = g.get_user()
    my_repo= user.get_repos()[4]

    print(f"We will be commiting to this repo: {my_repo}")
    number_for_file=random.randint(1,10000000)
    
    my_repo.create_file(f"{number_for_file}-th_test_commit.txt", f"This is the {number_for_file}-th commit from airflow dag", ".")

    time.sleep(300)

@dag(
    dag_id='mimic_activity_v27',
    default_args=default_args,
    start_date=datetime(2023,4, 22),
    schedule_interval='@daily'
)

def my_dag():
    do_n_commits.expand(n=get_n_of_commits())

dag=my_dag()