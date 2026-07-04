from dagster import Definitions, define_asset_job, AssetSelection
from dagster_dlt import DagsterDltResource

from .assets import stack_exchange_dlt_assets

stack_exchange_job = define_asset_job(
    name="stack_exchange_job",
    selection=AssetSelection.groups("stack_exchange"),
)