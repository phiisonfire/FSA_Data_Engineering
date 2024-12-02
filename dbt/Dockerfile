FROM apache/airflow:2.10.3

USER airflow

WORKDIR /opt/airflow

COPY requirements.txt .
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r requirements.txt

RUN mkdir /home/airflow/.dbt/
COPY dbt_profiles.yml /home/airflow/.dbt/profiles.yml
COPY . .

WORKDIR /opt/airflow/dbtlearn

# USER root
RUN dbt deps
# USER airflow


# dbt run 
# dbt test