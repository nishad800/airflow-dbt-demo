from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig
from cosmos.user_pass import SnowflakeUserPasswordProfileMapping

# then, in your DAG
jaffle_shop = DbtTaskGroup(
    project_config=ProjectConfig("/opt/airflow/git/airflow-dbt-demo.git"),
    profile_config=ProfileConfig(
        profile_name="demo_dbt",
        target_name="dev",
        profile_mapping=SnowflakeUserPasswordProfileMapping(
            conn_id="dbt_demo",
            profile_args={"schema": "public"},
        ),
    )
)
