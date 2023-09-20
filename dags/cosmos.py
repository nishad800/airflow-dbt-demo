from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig


# then, in your DAG
jaffle_shop = DbtTaskGroup(
    project_config=ProjectConfig("/opt/airflow/git/airflow-dbt-demo.git"),
    conn_id="dbt_demo",
            
        )
