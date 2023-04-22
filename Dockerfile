FROM apache/airflow:2.5.3
USER root
RUN apt-get -y update
RUN apt-get -y install git
USER airflow
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt