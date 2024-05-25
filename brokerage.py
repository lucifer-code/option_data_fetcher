import requests

url = 'https://api.upstox.com/v2/charges/brokerage'
headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI3N0E4TUQiLCJqdGkiOiI2NjUxYWNiYzE4ZWJlYzEzZDZjYmNmZjUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzE2NjI4NjY4LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3MTY2NzQ0MDB9.mTMsrqvxw-E76Hxx7TL-goOcFYjodlgtb1Hcx0dRrhs'
    }
params = {
    'instrument_token': 'NSE_EQ|INE669E01016',
    'quantity': '10',
    'product': 'D',
    'transaction_type': 'BUY',
    'price': '13.7'
}
response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.json())