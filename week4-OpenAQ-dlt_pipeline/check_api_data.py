import requests
import json

api_key = "60ce0e8fc3872c75fb10c957ac5fd677203de3fdec0837501378323074c03ed3"

url = "https://api.openaq.org/v3/locations"
headers = {"x-api-key": api_key}

response = requests.get(url, headers=headers)
data = response.json()

# Print first result with nice formatting
print(json.dumps(data["results"][0], indent=2))