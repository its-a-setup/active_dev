import os
from dotenv import load_dotenv
from datetime import datetime

from github import Github
from airflow.decorators import dag, task

default_args={
    'owner' : 'active_developer',
    'retries' : 5
}

@dag(
    dag_id='connect_to_github_v1',
    default_args=default_args,
    start_date=datetime(2023,4, 15),
    schedule_interval='@daily'
)
def get_repos():

    @task
    def get_list_of_repos():
        load_dotenv()

        GITHUB_ACCESS_TOKEN=os.getenv('GITHUB_ACCESS_TOKEN')

        # using an access token
        g = Github(GITHUB_ACCESS_TOKEN)
        for repo in g.get_user().get_repos():
            print(repo.name)
    get_list_of_repos()
get_repos()