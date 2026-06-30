from dagster import ScheduleDefinition

# schedule a job

github_schedule=ScheduleDefinition(
    name="10_minutes_schedule_github_issues",
    job_name="github_job",
    cron_schedule="*/10 * * * *"
)



locations_schedule=ScheduleDefinition(
    name="10_minutes_schedule_openaq_locations",
    job_name="openaq_job",
    cron_schedule="*/10 * * * *"
)


