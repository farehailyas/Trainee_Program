from .defs.assets import dagster_github_assets , dagster_openaq_locations
from dagster import Definitions, load_assets_from_modules , define_asset_job , ScheduleDefinition
from dagster_dlt import DagsterDltResource 
from .defs.jobs import github_job , openaq_job
from .defs.schedules import github_schedule ,locations_schedule
from .defs.sensors import trigger_openaq_sensor

# modify the definition to include my job and schedules
defs = Definitions(
    jobs = [ openaq_job ],
    assets=[ dagster_openaq_locations ],
    resources={
        "dlt": DagsterDltResource(),
    },
    schedules = [ locations_schedule],
    # sensors=[trigger_openaq_sensor]
)