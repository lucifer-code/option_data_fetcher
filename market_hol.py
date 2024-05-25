import requests
from datetime import datetime

def is_market_holidays(date):
    url = f'https://api.upstox.com/v2/market/holidays/{date}'
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # If data is empty, it means there are no holidays on the given date
        if not data:
            return 0
        else:
            return 1
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return -1  # Return -1 to indicate an error

# Example usage with current date
current_date = datetime.now().strftime("%Y-%m-%d")
result = is_market_holidays(current_date)

# print(result)
