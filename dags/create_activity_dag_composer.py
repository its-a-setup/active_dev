from datetime import datetime
from airflow.models import Variable

from airflow.decorators import dag, task

GITHUB_ACCESS_TOKEN = Variable.get("GITHUB_ACCESS_TOKEN")
GITHUB_USERNAME = Variable.get("GITHUB_USERNAME")
GITHUB_REPO = Variable.get("GITHUB_REPO")
FILE_NAME = Variable.get("FILE_NAME")
UP_TO_N_COMMITS = Variable.get("UP_TO_N_COMMITS")

default_args = {"owner": "active_developer", "retries": UP_TO_N_COMMITS}


@task
def get_n_of_commits():
    import random

    n = random.randint(2, int(UP_TO_N_COMMITS))
    my_list = list(range(1, n + 1))
    return my_list


@task
def do_n_commits(n):
    import time

    from github import Github

    g = Github(GITHUB_ACCESS_TOKEN)
    my_repo = g.get_repo(f"{GITHUB_USERNAME}/{GITHUB_REPO}")

    print(f"We will be commiting to this repo: {my_repo}")

    contents = my_repo.get_contents(FILE_NAME)
    content_of_the_file = str(datetime.now())
    commit_message = f"Commit at {content_of_the_file}"

    my_repo.update_file(
        contents.path, commit_message, content_of_the_file, contents.sha
    )
    print(f"{n} - Successfully commited the file to github repo")

    print("Waiting 5 minutes to avoid clashes between commits")
    time.sleep(300)


@dag(
    dag_id="mimic_activity_dag_composer",
    default_args=default_args,
    start_date=datetime(2023, 4, 23),
    schedule_interval="0 20 * * *",
    catchup=False
)
def my_dag():
    do_n_commits.expand(n=get_n_of_commits())


dag = my_dag()
