import requests

def is_market_open():
    url = 'https://api.upstox.com/v2/market/status/NSE'
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI3N0E4TUQiLCJqdGkiOiI2NjUxYWNiYzE4ZWJlYzEzZDZjYmNmZjUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzE2NjI4NjY4LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3MTY2NzQ0MDB9.mTMsrqvxw-E76Hxx7TL-goOcFYjodlgtb1Hcx0dRrhs'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
        data = response.json()
        return data.get('status') == 'open'
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
# print(is_market_open())