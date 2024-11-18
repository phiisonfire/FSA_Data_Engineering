from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from pipeline.transform import transform_book_data

current_date_str = datetime.today().strftime('%Y-%m-%d')
transformation_output_path = f"/opt/airflow/crawl_data/tiki_book_data_{current_date_str}"
s3_destination_path = f"s3://phinguyen98bucket01/tiki_books/data_{current_date_str}"

default_args = {
    'owner': 'Phi Nguyen',
    'retries': 1,
    'start_date': datetime(2024, 11, 18)
}

with DAG(
    'etl_pipeline',
    default_args=default_args,
    description='ETL pipeline extract book data from Tiki, transform and upload to S3',
    schedule_interval='@daily'
) as dag:
    
    extract_and_transform_task = PythonOperator(
        task_id='extract_and_transform',
        python_callable=transform_book_data,
        op_args=[transformation_output_path]
    )

    upload_to_s3_task = BashOperator(
        task_id="upload_to_s3",
        bash_command=f"aws s3 cp {transformation_output_path} {s3_destination_path} --recursive"
    )

    extract_and_transform_task >> upload_to_s3_task