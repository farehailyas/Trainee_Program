from dagster import ScheduleDefinition
from dagster_dlt import DagsterDltResource

from .jobs import incremental_job


incremental_schedule = ScheduleDefinition(
    job=incremental_job,
    cron_schedule="30 18 * * *",
    execution_timezone="Asia/Karachi",
)