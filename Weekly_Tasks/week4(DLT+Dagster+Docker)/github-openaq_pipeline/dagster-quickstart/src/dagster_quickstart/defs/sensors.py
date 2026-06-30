# from .jobs import github_job , openaq_job
# from .assets import dagster_github_assets
# import dagster as dg
# # when github asset is materialized openaq job is triggered
# # trigger openaq_job 

# # @dg.asset_sensor(asset_key = dg.AssetKey("dagster_github_assets") , job_name="openaq_job")
# # def trigger_openaq_sensor():
# #     yield dg.RunRequest()

# @dg.asset_sensor(
#     asset_key=dg.AssetKey("dlt_github_reactions_issues"), 
#     job=openaq_job
# )
# def trigger_openaq_sensor(context: dg.SensorEvaluationContext, asset_event):
#     # Ensure it is a materialization event before proceeding
#     if asset_event.dagster_event.event_type == dg.DagsterEventType.ASSET_MATERIALIZATION:
#         # Yield a run request to start the job
#         yield dg.RunRequest()

# # slack_run_on_failure = 



import os
from dagster import (
    RunFailureSensorContext, run_failure_sensor, DefaultSensorStatus,
    run_status_sensor, DagsterRunStatus, RunStatusSensorContext)
from dagster_slack import SlackResource
import datetime
import sys
from dotenv import load_dotenv
from pathlib import Path

# Get repo root dynamically
repo_root = Path(__file__).resolve().parents[3]
load_dotenv(repo_root / ".env")

# Add repo root to path (works both locally and in Docker)
sys.path.insert(0, str(repo_root))


slack_datum = SlackResource(token=os.getenv("SLACK_TOKEN"))
base_url = " http://0.0.0.0:3000 "

@run_failure_sensor(
    description="Sends alerts to Slack when a Dagster job run fails",
    default_status= DefaultSensorStatus.RUNNING,
    monitored_jobs=["openaq_job"],
)
def slack_on_run_failure(context: RunFailureSensorContext) -> None:

    try:        
        complete_url = f"{base_url}/runs/{context.dagster_run.run_id}"

        alert_time = datetime.datetime.now().strftime("%b %d, %Y %H:%M:%S")
    
        message = (
            f"*Dagster Alert Notification* :rotating_light: \n"
            f"*Job Name* - {context.dagster_run.job_name}\n"
            f"*Job Run ID* - {context.dagster_run.run_id}\n"
            f"*Job Status* - FAILED\n"
            f"*Alert Time* - {alert_time}\n"
            f"*Check Error Logs here* - {complete_url}"
        )

        slack_datum.get_client().chat_postMessage(channel="launchpad-technical", text=message)
       
    except Exception as e:
        message = (
            f"Failed to send Slack notification for \n"
            f"*Job Name* - {context.dagster_run.job_name}\n"
            f"*Job Run ID* - {context.dagster_run.run_id}\n"
            f"*Error status* - {e}" 
        )
        slack_datum.get_client().chat_postMessage(channel="launchpad-technical", text=message)


@run_status_sensor(
    run_status = DagsterRunStatus.CANCELED,
    description = "Alerts when a run is canceled / terminated",
    default_status = DefaultSensorStatus.RUNNING
)
def slack_on_run_canceled(context: RunStatusSensorContext) -> None:
    try:        
        complete_url = f"{base_url}/runs/{context.dagster_run.run_id}"

        alert_time = datetime.datetime.now().strftime("%b %d, %Y %H:%M:%S")
    
        message = (
            f"*Dagster Alert Notification* :rotating_light: \n"
            f"*Job Name* - {context.dagster_run.job_name}\n"
            f"*Job Run ID* - {context.dagster_run.run_id}\n"
            f"*Job Status* - CANCELED / Terminated \n"
            f"*Alert Time* - {alert_time}\n"
            f"*Check Error Logs here* - {complete_url}"
        )

        slack_datum.get_client().chat_postMessage(channel="launchpad-technical", text=message)
       
    except Exception as e:
        message = (
            f"Failed to send Slack notification for \n"
            f"*Job Name* - {context.dagster_run.job_name}\n"
            f"*Job Run ID* - {context.dagster_run.run_id}\n"
            f"*Error status* - {e}" 
        )
        slack_datum.get_client().chat_postMessage(channel="launchpad-technical", text=message)