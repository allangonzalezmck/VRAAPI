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

# Make the POST request to get the access token
response = requests.post(api_url, headers=headers, data=json.dumps(auth_data))

# Check the response status and print the output
print("Response Status Code:", response.status_code)
print("Response Body:", response.text)

if response.status_code == 200:
    # Parse the response JSON and extract the access token
    token = response.json().get('access_token')
    if token:
        print('Access Token:', token)

        # Now make the GET request to /iaas/api/projects with the filter
        projects_api_url = 'https://<vra-url>/iaas/api/projects'
        filter_query = "?$filter=name+contains+'Magnet'"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        # Make the GET request
        projects_response = requests.get(projects_api_url + filter_query, headers=headers)

        # Check the response status and print the output
        print("Projects API Response Status Code:", projects_response.status_code)
        print("Projects API Response Body:", projects_response.text)

        if projects_response.status_code == 200:
            # Print the projects data
            projects_data = projects_response.json()
            print('Projects Data:', json.dumps(projects_data, indent=4))
        else:
            print(f'Error: {projects_response.status_code}, {projects_response.text}')
    else:
        print('Error: Access token not found in the response')
else:
    print(f'Error: {response.status_code}, {response.text}')
