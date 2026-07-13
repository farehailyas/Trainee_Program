

import dlt

from dagster import asset
from dagster_dbt import DbtCliResource, dbt_assets , DagsterDbtTranslator
from dagster_dlt import DagsterDltResource, dlt_assets
from dlt_pipeline.stack_exchange_pipeline import stack_exchange_source
from pathlib import Path

DBT_PROJECT_DIR = Path(__file__).resolve().parent.parent / "dbt_project"
MANIFEST_PATH = DBT_PROJECT_DIR / "target" / "manifest.json"


pipeline = dlt.pipeline(
    pipeline_name="rest_api_stackexchange_incremental",
    destination="snowflake",
    # dataset_name="dlt_stack_exchange_source",
    dataset_name = "raw"

)

@dlt_assets(
    dlt_source=stack_exchange_source(load_mode="incremental"),
    dlt_pipeline=pipeline,
    name="stack_exchange_incremental",
    group_name="stack_exchange",
)
def stack_exchange_incremental(context, dlt: DagsterDltResource):
    yield from dlt.run(context=context)


# @dlt_assets(
#     dlt_source=stack_exchange_source(load_mode="historical"),
#     dlt_pipeline=pipeline,
#     name="stack_exchange_historical",
#     group_name="stack_exchange",
# )
# def stack_exchange_historical(context, dlt: DagsterDltResource):
#     yield from dlt.run(context=context)

from dagster_dbt import DagsterDbtTranslator
from dagster_dbt import DagsterDbtTranslator

class FlatDbtTranslator(DagsterDbtTranslator):

    def get_asset_key(self, manifest_node):
        if manifest_node.get("resource_type") == "source":
            return f"dlt_stack_exchange_source_{manifest_node['name']}"

        return super().get_asset_key(manifest_node)
        
@dbt_assets(
    manifest=MANIFEST_PATH,
    dagster_dbt_translator=FlatDbtTranslator(),
    # group_name="stack_exchange_models",

)
def stackexchange_dbt_assets(context, dbt: DbtCliResource):

    yield from dbt.cli(
        ["build"],
        context=context,
    ).stream()