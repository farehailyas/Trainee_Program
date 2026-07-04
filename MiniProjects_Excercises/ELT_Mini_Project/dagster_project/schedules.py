from dagster import ScheduleDefinition
from dagster_dlt import DagsterDltResource

from .assets import stack_exchange_historical ,stack_exchange_incremental

from .jobs import incremental_job


incremental_schedule = ScheduleDefinition(
    job=incremental_job,
    cron_schedule="20 15 * * *",
    execution_timezone="Asia/Karachi",
)