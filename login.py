import requests
from urllib.parse import urlencode

# Step 1: Generate the authorization URL
client_id = 'fc55ed66-aaa7-43c7-a7ac-15d08daa9c30'
redirect_uri = 'https://pro.upstox.com/'
response_type = 'code'

auth_url = 'https://api.upstox.com/v2/login/authorization/dialog'
params = {
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'response_type': response_type
}

auth_request_url = f"{auth_url}?{urlencode(params)}"
print(f"Please go to the following URL to authorize the application:\n{auth_request_url}")

# Step 2: Manually get the authorization code
# Normally, you would automate this process by interacting with the browser, but for simplicity,
# we'll assume you manually go to the URL and get the authorization code from the redirected URL.

auth_code = input("Enter the authorization code from the URL: ")

# Step 3: Exchange the authorization code for an access token
token_url = 'https://api.upstox.com/v2/login/authorization/token'
client_secret = '9o6pxfkdfl'
grant_type = 'authorization_code'

token_params = {
    'code': auth_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'grant_type': grant_type
}

response = requests.post(token_url, data=token_params)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data.get('access_token')
    print("Access Token:", access_token)
else:
    print(f"Failed to obtain access token. Status code: {response.status_code}")
    print("Response Content:", response.text)
