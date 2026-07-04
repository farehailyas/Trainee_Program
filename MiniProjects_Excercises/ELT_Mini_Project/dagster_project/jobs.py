# from dagster import Definitions, define_asset_job, AssetSelection
# from dagster_dlt import DagsterDltResource

# from .assets import  stack_exchange_assets

# historical_job = define_asset_job(
#     name="stack_exchange_historical_job",
#     selection=AssetSelection.assets(stack_exchange_assets),
# )

# incremental_job = define_asset_job(
#     name="stack_exchange_incremental_job",
#     selection=AssetSelection.assets(stack_exchange_assets),
# )

# etl_job = define_asset_job(
#     name="stack_exchange_job",
#     selection=(
#         AssetSelection.groups("stack_exchange")
#         .downstream()
#     ),
# )

from dagster import AssetSelection, define_asset_job
from .assets import stack_exchange_historical , stack_exchange_incremental

historical_job = define_asset_job(
    name="stack_exchange_historical_job",
    selection=(
        AssetSelection.assets(
            "stack_exchange_historical",
        )
        |
        AssetSelection.groups("dbt")
    ),
)

incremental_job = define_asset_job(
    name="stack_exchange_incremental_job",
    selection=(
        AssetSelection.assets(
            "stack_exchange_incremental",
        )
        |
        AssetSelection.groups("dbt")
    ),
)