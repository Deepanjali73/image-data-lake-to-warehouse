from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from google.cloud import storage, bigquery

def load_to_bigquery():
    storage_client = storage.Client()
    bucket = storage_client.bucket('image-data-lake')
    blobs = bucket.list_blobs(prefix='metadata/')
    client = bigquery.Client()
    table_id = 'your-project-id.image_dataset.image_metadata'  # Replace with your project ID
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        autodetect=True,
        write_disposition='WRITE_APPEND'
    )
    for blob in blobs:
        uri = f"gs://image-data-lake/{blob.name}"
        load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
        load_job.result()

dag = DAG(
    'image_etl',
    start_date=datetime(2025, 3, 31),
    schedule_interval='@hourly',
    catchup=False
)

task = PythonOperator(
    task_id='load_to_bq',
    python_callable=load_to_bigquery,
    dag=dag
)
