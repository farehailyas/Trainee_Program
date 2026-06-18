from typing import Optional, Tuple

import dlt
from pendulum import DateTime
from rest_api import restapi_source

from stripe_analytics import (
    ENDPOINTS,
    INCREMENTAL_ENDPOINTS,
    incremental_stripe_source,
    stripe_source,
)


def load_data(
    endpoints: Tuple[str, ...] = (
        "Customer"
    ),
    start_date: Optional[DateTime] = None,
    end_date: Optional[DateTime] = None,
) -> None:
   
    pipeline = dlt.pipeline(
        pipeline_name="stripe_analytics",
        destination='snowflake',
        dataset_name="stripe_updated",
    )
    source = stripe_source(
        endpoints=("Customer" , "Charge" , "Subscription")
    )
    load_info = pipeline.run(source)
    print(load_info)

def get_countries_data():
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_countries",
        destination="snowflake",
        dataset_name="countries_data",
    )

    load_info = pipeline.run(restapi_source())
    print(load_info)


def load_incremental_endpoints(
    endpoints: Tuple[str, ...] = INCREMENTAL_ENDPOINTS,
    initial_start_date: Optional[DateTime] = None,
    end_date: Optional[DateTime] = None,
) -> None:
    """
    This demo script demonstrates the use of resources with incremental loading, based on the "append" mode.
    This approach enables us to load all the data
    for the first time and only retrieve the newest data later,
    without duplicating and downloading a massive amount of data.

    Make sure you're loading objects that don't change over time.

    Args:
        endpoints: A tuple of incremental endpoint names to retrieve data from.
                   Defaults to Stripe API endpoints with uneditable data.
        initial_start_date: An optional parameter that specifies the initial value for dlt.sources.incremental.
                            If parameter is not None, then load only data that were created after initial_start_date on the first run.
                            Defaults t:***@TRSSOZD-UB62977/MULTI_SOURCE_DB location to store data
(venv) fareha@datumlabs-HP-EliteBook-845-G7-Notebook-PC:~/Fareha-Training/Trainee_Program/week3-dagster-dbt/Day4-multio None. Format: datetime(YYYY, MM, DD).
        end_date: An optional end date to limit the data retrieved.
                  Defaults to None. Format: datetime(YYYY, MM, DD).
    """
    pipeline = dlt.pipeline(
        pipeline_name="stripe_analytics",
        destination='snowflake',
        dataset_name="stripe_updated",
    )
    # load all data on the first run that created before end_date
    source = incremental_stripe_source(
        endpoints=endpoints,
        initial_start_date=initial_start_date,
        end_date=end_date,
    )
    load_info = pipeline.run(source)
    print(load_info)

    # # load nothing, because incremental loading and end date limit
    # source = incremental_stripe_source(
    #     endpoints=endpoints,
    #     initial_start_date=initial_start_date,
    #     end_date=end_date,
    # )
    # load_info = pipeline.run(source)
    # print(load_info)
    #
    # # load only the new data that created after end_date
    # source = incremental_stripe_source(
    #     endpoints=endpoints,
    #     initial_start_date=initial_start_date,
    # )
    # load_info = pipeline.run(source)
    # print(load_info)


if __name__ == "__main__":
    # load_data()
    get_countries_data()
    # # load only data that was created during the period between the Jan 1, 2024 (incl.), and the Feb 1, 2024 (not incl.).
    # from pendulum import datetime
    # load_data(start_date=datetime(2024, 1, 1), end_date=datetime(2024, 2, 1))
    # # load only data that was created during the period between the May 3, 2023 (incl.), and the March 1, 2024 (not incl.).
    # load_incremental_endpoints(
    #     endpoints=("Event",),
    #     initial_start_date=datetime(2023, 5, 3),
    #     end_date=datetime(2024, 3, 1),
    # )
