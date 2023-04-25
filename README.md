# active_dev
![license](https://img.shields.io/badge/license-GPL--3.0-orange)
## Description
Are you a beginner programmer, who wants to boost your GitHub? 
Or maybe you are tired of recruiters asking why your GitHub is not active? 
Or maybe you just want your GitHub to look like this?
![alt text](other/linus_gh.png)

Worry not, this Airflow project will help you to mimic the activity in your GitHub profile by generating a random number of commits on a daily basis.

## Prerequisites
1. [Python3](https://www.python.org/downloads/)
2. [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Quickstart
1. Fork this repo
2. Clone the repo to your local machine
3. Create directories for airflow in your working directory:
`mkdir -p ./logs ./plugins`
4. Rename the airflow image in docker-compose.yaml from "extending_airflow:latest" -> "apache/airflow:2.5.3" (this is needed for the docker hub to download the correct airflow image)
5. Initialize the db:
`docker compose up airflow-init`
6. Rename your image back from "apache/airflow:2.5.3" -> "extending_airflow:latest"
6. Run this command to extend your airflow image:
`docker build . --tag extending_airflow:latest`
10. Start containers for our application:
`docker compose up -d`
10. Create new private repo in your GitHub and add empty .txt file there
11. Create .env file in dags/ and edit it to include your data
12. Open [airflow webserver](http://localhost:8080/home) in your browser and log in with (login: airflow, password: airflow)
13. Run "mimic_activity_dag"

Congrats, now your GitHub will stay active forever!