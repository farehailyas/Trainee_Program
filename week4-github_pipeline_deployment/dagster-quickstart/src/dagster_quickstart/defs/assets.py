import dlt
from dagster import AssetExecutionContext
from dagster_dlt import DagsterDltResource, dlt_assets
from .github_pipeline import github_source
import dagster as dg
from .OpenAQ_rest_api_pipeline import get_locations

@dlt_assets(
    dlt_source=github_source(),
    dlt_pipeline=dlt.pipeline(
        pipeline_name="github_issues",
        dataset_name="dagster_multisource",
        destination="snowflake",
        progress="log",
    ),
    name="github",
    group_name="github",
)
def dagster_github_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)



@dlt_assets(
    dlt_source=get_locations(),
    dlt_pipeline=dlt.pipeline(
        pipeline_name="openaq_pipeline",
        dataset_name="dagster_multisource",
        destination="snowflake",
        progress="log",
    ),
    name="locations",
    group_name="locations",
)
def dagster_openaq_locations(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)