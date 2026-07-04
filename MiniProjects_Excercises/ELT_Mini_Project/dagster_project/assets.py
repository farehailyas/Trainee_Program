# import dlt
# from dagster import AssetExecutionContext

# import dlt
# from dagster import Definitions
# from dagster_dlt import DagsterDltResource, dlt_assets
# from dagster_dbt import dbt_assets
# from dlt_pipeline.stack_exchange_pipeline import stack_exchange_source  # adjust import path


# @dlt_assets(
#     dlt_source=stack_exchange_source(load_mode="incremental"),
#     dlt_pipeline=dlt.pipeline(
#         pipeline_name="rest_api_stackexchange",
#         destination="duckdb",
#         dataset_name="raw_stackexchange",
#     ),
#     name="stack_exchange",
#     group_name="stack_exchange",
# )
# def stack_exchange_assets(context, dlt: DagsterDltResource):
#     yield from dlt.run(context=context)



# @dbt_assets(manifest="../dbt_project/target/manifest.json")
# def stackexchange_dbt_assets(
#     context: AssetExecutionContext,
#     dbt: DbtCliResource,
# ):
#     yield from dbt.cli(["build"], context=context).stream()


import dlt

from dagster import asset
from dagster_dbt import DbtCliResource, dbt_assets

from dlt_pipeline.stack_exchange_pipeline import stack_exchange_source
from pathlib import Path

DBT_PROJECT_DIR = Path(__file__).resolve().parent.parent / "dbt_project"
MANIFEST_PATH = DBT_PROJECT_DIR / "target" / "manifest.json"

pipeline = dlt.pipeline(
    pipeline_name="rest_api_stackexchange",
    destination="duckdb",
    dataset_name="raw_stackexchange",
)


@asset(
    group_name="stack_exchange",
)
def stack_exchange_historical(context):

    load_info = pipeline.run(
        stack_exchange_source(load_mode="historical")
    )
    context.log.info(str(load_info))

    return load_info


@asset(
    group_name="stack_exchange",
)
def stack_exchange_incremental(context):

    load_info = pipeline.run(
        stack_exchange_source(load_mode="incremental")
    )
    context.log.info(str(load_info))

    return load_info


@dbt_assets(
    manifest=MANIFEST_PATH,
)
def stackexchange_dbt_assets(context, dbt: DbtCliResource):

    yield from dbt.cli(
        ["build"],
        context=context,
    ).stream()