from .jobs import github_job , openaq_job
from .assets import dagster_github_assets
import dagster as dg
# when github asset is materialized openaq job is triggered
# trigger openaq_job 

# @dg.asset_sensor(asset_key = dg.AssetKey("dagster_github_assets") , job_name="openaq_job")
# def trigger_openaq_sensor():
#     yield dg.RunRequest()

@dg.asset_sensor(
    asset_key=dg.AssetKey("dlt_github_reactions_issues"), 
    job=openaq_job
)
def trigger_openaq_sensor(context: dg.SensorEvaluationContext, asset_event):
    # Ensure it is a materialization event before proceeding
    if asset_event.dagster_event.event_type == dg.DagsterEventType.ASSET_MATERIALIZATION:
        # Yield a run request to start the job
        yield dg.RunRequest()