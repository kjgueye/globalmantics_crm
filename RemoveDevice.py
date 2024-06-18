import requests
from auth_token import get_token


def main():
    url = f"https://10.10.20.85/dna/intent/api/v1/network-device/{input("Enter ID")}"
    headers = {
        "Content-Type": "application/json",
        "x-Auth-Token": get_token()
    }

    delete = requests.delete(url, headers=headers, verify=False)
    delete.raise_for_status()
    return delete


if __name__ == "__main__":
    main()
