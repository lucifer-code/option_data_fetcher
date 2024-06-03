import requests

url = 'https://api.upstox.com/v2/market/holidays/2024-06-01'
headers = {'Accept': 'application/json'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Process the JSON response
    print(data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)