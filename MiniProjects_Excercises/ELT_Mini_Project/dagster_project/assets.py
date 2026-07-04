import dlt
from dagster import AssetExecutionContext

import dlt
from dagster import Definitions
from dagster_dlt import DagsterDltResource, dlt_assets

from pipelines.stack_exchange_pipeline import stack_exchange_source  # adjust import path


@dlt_assets(
    dlt_source=stack_exchange_source(),
    dlt_pipeline=dlt.pipeline(
        pipeline_name="rest_api_stackexchange",
        destination="duckdb",
        dataset_name="raw_stackexchange",
    ),
    name="stack_exchange",
    group_name="stack_exchange",
)
def stack_exchange_dlt_assets(context, dlt: DagsterDltResource):
    yield from dlt.run(context=context)