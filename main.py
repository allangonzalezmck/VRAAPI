import requests
import json

# Replace these with your actual vRA URL, username, and password
api_url = 'https://<vra-url>/automation/api/token'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

# Create the payload for the POST request
auth_data = {
    'username': username,
    'password': password
}

# Set the headers for the request
headers = {
    'Content-Type': 'application/json'
}

# Make the POST request
response = requests.post(api_url, headers=headers, data=json.dumps(auth_data))

# Check the response status and print the output
if response.status_code == 200:
    print('Token:', response.json())
else:
    print(f'Error: {response.status_code}, {response.text}')
