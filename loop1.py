import time
import requests
import json
from datetime import datetime, timedelta
from bussiness_hour_check import is_within_business_hours
from market_status import is_market_open
from market_hol import is_market_holidays
# Initialize the expiry date
expiry_date = datetime.strptime('2024-05-30', '%Y-%m-%d')


def fetch_and_save_data(expiry_date):
    # Fetch data from API
    url = 'https://api.upstox.com/v2/option/chain'
    params = {
        'instrument_key': 'NSE_INDEX|Nifty 50',
        'expiry_date': expiry_date.strftime('%Y-%m-%d')
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
    global expiry_date
    while True:
        # Get the current date
        current_date = datetime.now()

        # if not (is_market_open()):
        #     print("Market is not open yet. Waiting for 1 minute")
        #     time.sleep(60)

        if(is_within_business_hours(current_date) and is_market_open() ):
            print("Market is open. Fetching data...")
            # Calculate the difference in days between current date and expiry date
            days_difference = (current_date - expiry_date).days
            
            if days_difference > 0:
                # Calculate number of weeks between current date and expiry date
                weeks_difference = (days_difference // 7) + 1
                # Update expiry date to n*7 days ahead
                expiry_date += timedelta(weeks=weeks_difference)
                print(f"Expiry date updated to {expiry_date.strftime('%Y-%m-%d')}")

            fetch_and_save_data(expiry_date)
            time.sleep(10)  # Wait for 10 seconds before fetching data again

        # elif not 


        else:
            print("Market is closed. Waiting for 1 hour")
            time.sleep(3600)

if __name__ == "__main__":
    main()
