from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, GitHubSourceConfig

# Define the GitHub repository URL of your dbt project
github_repo_url = "https://github.com/nishad800/airflow-dbt-demo.git"

# Then, in your DAG
jaffle_shop = DbtTaskGroup(
    project_config=ProjectConfig(
        source_config=GitHubSourceConfig(
            repo_url=github_repo_url,
            # Optionally, specify a specific branch or commit
            branch="main",  # Replace with your desired branch or commit
        )
    ),
    profile_config=ProfileConfig(
        profile_name="profiles",
        target_name="target",
        profile_mapping=PostgresUserPasswordProfileMapping(
            conn_id="demo_dbt",
            profile_args={"schema": "public"},
        ),
    )
)
