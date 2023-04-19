FROM apache/airflow:2.5.3
USER root
RUN apt-get -y update
RUN apt-get -y install git