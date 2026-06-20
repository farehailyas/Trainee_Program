import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources

@dlt.source
def restapi_source():

    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://www.ncei.noaa.gov/cdo-web/api/v2/",
            "headers": {
                "token": "rTYXIeRPAWSFjplaxAOCzJoctgGAkePL"
            }
        },

        "resources": [
            {
                "name": "weather_observations",

                "endpoint": {
                    "path": "data",
                    "params": {
                        "datasetid": "GHCND",
                        "startdate": "2024-01-01",
                        "enddate": "2025-01-01",
                        "limit": 1000
                    },

                    "data_selector": "results",

                    "paginator": {
                        "type": "offset",
                        "limit": 1000
                    },

                    "incremental": {
                        "cursor_path": "date",
                        "initial_value": "2020-01-01",
                    }
                }
            }
        ]
    }

    yield from rest_api_resources(config)