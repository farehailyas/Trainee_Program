import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources

@dlt.source
def restapi_source():
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://api.restcountries.com/countries/v5",
            "auth": {
                "type": "bearer",
                "token": dlt.secrets["sources"]["rest_countries_source"]["bearer_token"],
            },
        },
        "resource_defaults": {
            "primary_key": "uuid",
            "write_disposition": "merge",
        },
        "resources": [
        {
            "name": "countries",
            "endpoint": {
                "path": "",
                "params": {
                    "limit": 250,
                },
                "data_selector": "data.objects",  
            },
        },
    ],
    }
    yield from rest_api_resources(config)