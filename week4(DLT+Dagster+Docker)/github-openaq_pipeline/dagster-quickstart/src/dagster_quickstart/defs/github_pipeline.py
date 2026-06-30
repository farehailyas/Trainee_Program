import dlt
import sys

from dotenv import load_dotenv
from pathlib import Path
# Get repo root dynamically
repo_root = Path(__file__).resolve().parents[3]
print("root path " ,repo_root )
load_dotenv(repo_root / ".env")

# Add repo root to path (works both locally and in Docker)
sys.path.insert(0, str(repo_root))

from github import github_reactions, github_repo_events, github_stargazers


def github_source():
    """Returns github source with only issues"""
    return github_reactions(
        "duckdb", "duckdb", 
        items_per_page=100, 
        max_items=100
    ).with_resources("issues")

def load_duckdb_repo_reactions_issues_only() -> None:
    """Loads issues, their comments and reactions for duckdb"""
    pipeline = dlt.pipeline(
        "github_reactions",
        destination='snowflake',
        dataset_name="github_data_final",
        # dev_mode=True,
    )
    # get only 100 items (for issues and pull request)
    data = github_reactions(
        "duckdb", "duckdb", items_per_page=100, max_items=100
    ).with_resources("issues")
    print(pipeline.run(data))


def load_airflow_events() -> None:
    """Loads airflow events. Shows incremental loading. Forces anonymous access token"""
    pipeline = dlt.pipeline(
        "github_events", destination='snowflake', dataset_name="github_data_final"
    )
    data = github_repo_events("apache", "airflow", access_token="")
    print(pipeline.run(data))
    # if you uncomment this, it does not load the same events again
    # data = github_repo_events("apache", "airflow", access_token="")
    # print(pipeline.run(data))


def load_dlthub_dlt_all_data() -> None:
    """Loads all issues, pull requests and comments for dlthub dlt repo"""
    pipeline = dlt.pipeline(
        "github_reactions",
        destination='snowflake',
        dataset_name="github_data_final",
        # dev_mode=True,
    )
    data = github_reactions("dlt-hub", "dlt")
    print(pipeline.run(data))


def load_dlthub_dlt_stargazers() -> None:
    """Loads all stargazers for dlthub dlt repo"""
    pipeline = dlt.pipeline(
        "github_stargazers",
        destination='snowflake',
        dataset_name="github_data_final",
        # dev_mode=True,
    )
    data = github_stargazers("dlt-hub", "dlt")
    print(pipeline.run(data))


if __name__ == "__main__":
    load_duckdb_repo_reactions_issues_only()
    load_airflow_events()
    load_dlthub_dlt_all_data()
    load_dlthub_dlt_stargazers()
