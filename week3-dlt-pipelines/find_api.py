import requests

url = "https://api.daac.asf.alaska.edu/services/search/param"
params = {
    "platform": "UAVSAR",
    "processingLevel": "L1",
    "output": "json",
    "maxResults": 10
}

r = requests.get(url, params=params)
print(r.json())