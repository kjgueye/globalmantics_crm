import requests
from requests.auth import HTTPBasicAuth

# Define the device name and the URL for the RESTCONF API
device_name = "dist-rtr01"
url = f"http://10.10.20.50:8080/restconf/data/tailf-ncs:devices/device={device_name}"

# Set the headers to accept JSON formatted data
headers = {
    "Accept": "application/yang-data+json"
}

# Use basic authentication with the provided credentials
auth = HTTPBasicAuth('admin', 'admin')

# Make the GET request to the NSO server to fetch device data
response = requests.get(url, headers=headers, auth=auth, verify=False)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    device_data = response.json()
    # Print the device data
    print(device_data)
else:
    # Print an error message if the request was not successful
    print(f"Failed to retrieve data for device {device_name}. Status code: {response.status_code}")
