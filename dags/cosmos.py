from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig

# then, in your DAG
jaffle_shop = DbtTaskGroup(
    project_config=ProjectConfig(""),
    profile_config=ProfileConfig(
        profile_name="my_profile",
        target_name="my_target",
        profile_mapping=PostgresUserPasswordProfileMapping(
            conn_id="dbt_demo",
            profile_args={"schema": "public"},
        ),
    )
)
