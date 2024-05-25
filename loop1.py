import time
import requests
import json

def fetch_and_save_data():
    url = 'https://api.upstox.com/v2/option/chain'
    params = {
        'instrument_key': 'NSE_INDEX|Nifty 50',
        'expiry_date': '2024-05-30'
    }

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI3N0E4TUQiLCJqdGkiOiI2NjUxYWNiYzE4ZWJlYzEzZDZjYmNmZjUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzE2NjI4NjY4LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3MTY2NzQ0MDB9.mTMsrqvxw-E76Hxx7TL-goOcFYjodlgtb1Hcx0dRrhs'
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
            json_filename = f'data_{timestamp}.json'
            with open(json_filename, 'w') as f:
                json.dump(data['data'], f, indent=4)
            print(f"Data saved as {json_filename}")
        else:
            print("No data available.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def main():
    while True:
        fetch_and_save_data()
        time.sleep(10)  # Wait for 10 seconds before fetching data again

if __name__ == "__main__":
    main()
