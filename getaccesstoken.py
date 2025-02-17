import requests
import json

# Replace these with your actual vRA URL, domain, username, and password
api_url = 'https://<vra-url>/csp/gateway/am/api/login?access_token'
domain = 'YOUR_DOMAIN'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

# Create the payload for the POST request
auth_data = {
    'username': username,
    'password': password,
    'domain': domain  # Including the domain for authentication
}

# Set the headers for the request
headers = {
    'Content-Type': 'application/json'
}

# Print the request details for debugging
print("API URL:", api_url)
print("Request Headers:", headers)
print("Request Body:", json.dumps(auth_data, indent=4))

# Make the POST request
response = requests.post(api_url, headers=headers, data=json.dumps(auth_data))

# Check the response status and print the output
print("Response Status Code:", response.status_code)
print("Response Body:", response.text)

if response.status_code == 200:
    # Parse the response JSON and extract the access token
    token = response.json().get('access_token')
    if token:
        print('Access Token:', token)
    else:
        print('Error: Access token not found in the response')
else:
    print(f'Error: {response.status_code}, {response.text}')
