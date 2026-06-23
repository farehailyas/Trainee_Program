from .defs.assets import dagster_github_assets
from dagster import Definitions, load_assets_from_modules , define_asset_job , ScheduleDefinition
from dagster_dlt import DagsterDltResource
from .defs.jobs import github_job
from .defs.schedules import github_schedule

# modify the definition to include my job and schedules
defs = Definitions(
    jobs = [github_job],
    assets=[dagster_github_assets],
    resources={
        "dlt": DagsterDltResource(),
    },
    schedules = [github_schedule]
)