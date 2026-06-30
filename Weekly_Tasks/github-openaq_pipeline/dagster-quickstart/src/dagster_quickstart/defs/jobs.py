from .assets import dagster_github_assets, dagster_openaq_locations
from dagster import define_asset_job

# create a job
github_job = define_asset_job(
    name="github_job",
    selection=[dagster_github_assets], #must be in a form of list

)

openaq_job = define_asset_job(
    name="openaq_job",
    selection=[dagster_openaq_locations]
)



