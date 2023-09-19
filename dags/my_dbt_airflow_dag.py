from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import subprocess

def run_dbt():
    dbt_command = "dbt run --profiles-dir https://dbtfile2023.blob.core.windows.net/dbtcontainer/dbt_demo/profiles.yml --profile dbt_demo"
    subprocess.run(dbt_command, shell=True)

dag = DAG(
    'run_dbt_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,  # Set your desired schedule interval
)

run_dbt_task = PythonOperator(
    task_id='run_dbt_task',
    python_callable=run_dbt,
    dag=dag,
)

# Add other tasks and dependencies as needed
