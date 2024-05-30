import time
import requests
from auth_token import get_token


def main():
    token = get_token()

    api_path = "https://10.10.20.85/dna"
    headers = {"Content-Type": "application/json", "X-Auth-Token": token}

    new_device_dict = {
        "ipAddress": ["192.0.2.1"],
        "snmpVersion": "v2",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetry": "1",
        "snmpTimeout": "60",
        "cliTransport": "ssh",
        "userName": "nick",
        "password": "secret123!",
        "enablePassword": "secret456!",
    }
    add_resp = requests.post(
        f"{api_path}/intent/api/v1/network-device",
        json=new_device_dict,
        headers=headers,
        verify=False
    )

    if add_resp.ok:
        print(f"Request accepted:  status code {add_resp.status_code}")
        time.sleep(10)

        task = add_resp.json()["response"]["taskId"]
        task_resp = requests.get(
            f"{api_path}/intent/api/v1/task/{task}", headers=headers, verify=False
        )

        if task_resp.ok:
            task_data = task_resp.json()["response"]
            if not task_data["isError"]:
                print("new device successfully added")
            else:
                print(f"Asyn GET failed.  Satus code {task_resp.status_code}")
        else:
            print(f"Aysnc GET Failed: status code {task_resp.status_code}")
    else:
        print(f"Device Addition failed with code {add_resp.status_code}")
        print(f"Failure body:  {add_resp.text}")


if __name__ == "__main__":
    main()
