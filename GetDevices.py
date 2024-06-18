import requests
from auth_token import get_token


def get_devices():
    url = "https://10.10.20.85/dna/intent/api/v1/network-device"
    headers = {
        "Content-Type": "application/json",
        "x-Auth-Token": get_token()
    }

    getresponse = requests.get(url, headers=headers, verify=False)
    getresponse.raise_for_status()
    return getresponse



def main():
    results = get_devices()
    import json;
    if results.ok:
        for device in results.json() ["response"]:
            print(f"ID: {device['id']}  IP: {device['managementIpAddress']}")
    else:
        print(f"Device Collection failed with code {results.status_code}")
        print(f"Failure Body: {results.text}")
    #print(json.dumps(results.json(), indent=2))





if __name__ == "__main__":
    main()
