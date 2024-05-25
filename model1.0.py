# import requests

# url = 'https://api.upstox.com/v2/option/contract?instrument_key=NSE_INDEX%7CNifty%2050'
# headers = {
#     'Accept': 'application/json',
#     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI3N0E4TUQiLCJqdGkiOiI2NjUxYWNiYzE4ZWJlYzEzZDZjYmNmZjUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzE2NjI4NjY4LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3MTY2NzQ0MDB9.mTMsrqvxw-E76Hxx7TL-goOcFYjodlgtb1Hcx0dRrhs'
# }

# response = requests.get(url, headers=headers)

# # Print the response content
# print(response.text)




import requests
import pandas as pd
# import requests

url = 'https://api.upstox.com/v2/option/chain'
params = {
    'instrument_key': 'NSE_INDEX|Nifty 50',
    'expiry_date': '2024-05-30'
}

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI3N0E4TUQiLCJqdGkiOiI2NjUxYWNiYzE4ZWJlYzEzZDZjYmNmZjUiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzE2NjI4NjY4LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3MTY2NzQ0MDB9.mTMsrqvxw-E76Hxx7TL-goOcFYjodlgtb1Hcx0dRrhs'
}

# Make API request
response = requests.get(url,params=params, headers=headers)
data = response.json()

# Check if data is available
# print(data)

if 'data' in data:
    # Convert data to DataFrame
    df = pd.DataFrame(data['data'])

    # Save data to JSON file
    df.to_json('data.json', orient='records', indent=4)

    # Save data to Excel file with well-formatted headers
    excel_filename = 'data.xlsx'
    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, header=True)
    
    print("Data saved as data.json and data.xlsx in the current directory.")
else:
    print("No data available.")
