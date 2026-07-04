from dagster import Definitions
from dagster_dlt import DagsterDltResource

from .assets import stack_exchange_dlt_assets
from .jobs import stack_exchange_job


defs = Definitions(
    assets=[stack_exchange_dlt_assets],
    jobs=[stack_exchange_job],
    resources={"dlt": DagsterDltResource()},
)