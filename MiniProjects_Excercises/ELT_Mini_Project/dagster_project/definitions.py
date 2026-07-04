from dagster import Definitions
from dagster_dbt import DbtCliResource
from pathlib import Path

DBT_PROJECT_DIR = Path(__file__).resolve().parent.parent / "dbt_project"
MANIFEST_PATH = DBT_PROJECT_DIR / "target" / "manifest.json"

from .assets import (
    stack_exchange_historical,
    stack_exchange_incremental,
    stackexchange_dbt_assets,
)

from .jobs import (
    historical_job,
    incremental_job,
)

from .schedules import (
    incremental_schedule,
)

defs = Definitions(
    assets=[
        stack_exchange_historical,
        stack_exchange_incremental,
        stackexchange_dbt_assets,
    ],
    jobs=[
        historical_job,
        incremental_job,
    ],
    schedules=[
        incremental_schedule,
    ],
    resources={
        "dbt": DbtCliResource(
            project_dir=DBT_PROJECT_DIR,
        ),
    },
)