import requests


def get_token():
    """
    Gets an access token from Cisco Catalyst center
    """
    # Declare local var to simplify reqeust proccess
    api_path = "https://10.10.20.85/dna"
    auth = ("admin", "Cisco1234!")
    headers = {"Content-Type": "application/json"}

    # Issue HTTP POST request to the URL to get token
    auth_resp = requests.post(
        f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers, verify=False
    )



    # if Successful, print token.  Else raise HTTP Error with some detail
    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]
    print (token)
    return token


def main():
    token = get_token()
    print(token)


if __name__ == "__main__":
    main()