# active_dev
![license](https://img.shields.io/badge/license-GPL--3.0-orange)
## Description
Are you a begginer programmer, who wants to boost their GitHub?
Or maybe you are tired of recruiters asking why your GitHub is not active?
Or maybe you want your GitHub to look like this?

## Prerequisites
1. Python3
2. [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Quickstart
1. Clone the repo
2. Create virtual environment for the project in your working directory:
`python3 -m venv active_dev_env`
3. Activate it:
`source active_dev_env/bin/activate`
4. Create directories for airflow in your working directory:
`mkdir -p ./dags ./logs ./plugins`
5. Initialize the db:
`docker compose up airflow-init`
6. Create and start containers for our application:
`docker compose up -d`


## Learning materials
1. https://docs.docker.com/get-started/

