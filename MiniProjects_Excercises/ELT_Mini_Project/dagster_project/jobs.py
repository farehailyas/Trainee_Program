
from dagster import AssetSelection, define_asset_job
from .assets import   stack_exchange_incremental  , stackexchange_dbt_assets  #stack_exchange_historical

# historical_job = define_asset_job(
#     name="stack_exchange_historical_job",
#     selection=(
#         AssetSelection.assets(
#             "stack_exchange_historical",
#         )
        
#     ),
# )
# from dagster import AssetSelection, define_asset_job

incremental_job = define_asset_job(
    name="stack_exchange_incremental_job",
    selection=AssetSelection.groups("stack_exchange"),
)