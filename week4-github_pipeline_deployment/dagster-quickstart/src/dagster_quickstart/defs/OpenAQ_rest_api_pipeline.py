import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources 
from dlt.sources.helpers.rest_client.paginators import PageNumberPaginator
import sys

from dotenv import load_dotenv
from pathlib import Path

# Get repo root dynamically
repo_root = Path(__file__).resolve().parents[3]
load_dotenv(repo_root / ".env")

# Add repo root to path (works both locally and in Docker)
sys.path.insert(0, str(repo_root))
@dlt.source
def openaq_source(api_key=dlt.secrets.value):
    
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://api.openaq.org",
            "headers": {
                "x-api-key": api_key,  
            },
            
            "paginator": PageNumberPaginator(
                page_param="page",  
                base_page=1,
                total_path=None,
                stop_after_empty_page=True,
            )
        },
        "resource_defaults": {
            "write_disposition": "merge"
        },
        "resources": [
            # {"name": "locations", 
            #     "primary_key": "id",
            #     "endpoint": {
            #         "path": "v3/locations", 
            #         "data_selector": "results",
            #         "params": {
            #             "limit": 1000
            #         }
            #     }
            # },

            {"name": "countries", 
                "primary_key": "id",
                "endpoint": {
                    "path": "v3/countries", 
                    "data_selector": "results",
                    "params": {
                        "limit": 1000
                    }
                }
            },
            # {
            #     "name": "updated_locations",
            #     "primary_key": "id",
            #     "write_disposition" : "merge",
            #     "endpoint": {
            #         "path": "v3/locations/{location_id}/latest",
            #         "data_selector": "results",
            #         "params": {
            #             "location_id": {
            #                 "type": "resolve",
            #                 "resource": "locations",
            #                 "field": "id"
            #             }
            #         }
            #     },
            # },


            # {
            #     "name": "sensors",
            #     "primary_key": "id",
            #     "endpoint": {
            #         "path": "v3/locations/{location_id}/sensors",
            #         "data_selector": "results",
            #         "params": {
            #              "location_id": {
            #                 "type": "resolve",
            #                 "resource": "locations",
            #                 "field": "id"
            #             }
            #         }
            #     },
            #     # "include_from_parent": ["id"]
            # },
            # {
            #     "name": "measurements",
            #     "write_disposition": "append",   
            #     # "include_from_parent": ["id"],

            #     "endpoint": {
            #         "path": "v3/sensors/{sensor_id}/measurements",
            #         "data_selector": "results",
            #         "params": {
            #             "sensor_id": {
            #                 "type": "resolve",
            #                 "resource": "sensors",
            #                 "field": "id"
            #             },
                        
            #             # "date_from": "2024-01-01",
            #             # "date_to": "2024-01-07" 
                        
            #         },
            #     }
            # },
        ],
    }
    
    yield from rest_api_resources(config)

def get_data() -> None:
    print("Starting pipeline...")
    pipeline = dlt.pipeline(
        pipeline_name="openaq_pipeline",
        destination="snowflake",
        dataset_name="openaq_dataset_4_resource",
    )
    print("Fetching data...")

    load_info = pipeline.run(openaq_source())
    print(load_info)
    print("Pipeline completed!")

# get_data()


def get_locations():
    """Returns locations only"""
    return openaq_source()