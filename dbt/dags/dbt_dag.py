from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Default arguments for the DAG
default_args = {
    'owner': 'phinguyen',
    'depends_on_past': False,
    'retries': 1,
}

# Define the DAG
with DAG(
    dag_id='dbt_run_and_test',
    default_args=default_args,
    description='Run dbt commands: dbt run and dbt test',
    schedule_interval=None,  # Trigger manually or set to a cron expression
    start_date=datetime(2024, 11, 28),
    catchup=False,
    tags=['dbt', 'bash'],
) as dag:

    # Task to run `dbt run`
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/airflow/dbtlearn && dbt run',
    )

    # Task to run `dbt test`
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/airflow/dbtlearn && dbt test',
    )

    # Task dependencies
    dbt_run >> dbt_test