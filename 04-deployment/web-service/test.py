import requests

url = "http://localhost:9696/predict"

ride = {
    "PUlocationID": 10,
    "DOlocationID": 50,
    "trip_distance": 40
}

response = requests.post(url, json=ride)

print("STATUS:", response.status_code)
print("RESPONSE:", response.json())
