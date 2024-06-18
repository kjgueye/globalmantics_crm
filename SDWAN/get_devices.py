import requests

def main():


    api_path = "https://10.10.20.90"

    requests.packages.urllib3.disable_warnings()


    login_creds = {"j_username": "admin", "j_password": "C1sco12345"}


    sess = requests.session()
    auth_resp = sess.post(
        f"{api_path}/j_security_check", data=login_creds, verify=False
    )

    if not auth_resp.ok or auth_resp.text:
        print("Login Failed as expected :(")
        import sys
        sys.exit(1)
    device_resp = sess.get(f"{api_path}/dataservice/device", verify=False)
    if device_resp.ok:
        devices = device_resp.json()["data"]

        print(f"Devices managed by Devnet SD-WAN sandbox:")
        for dev in devices:
            print(f"Device IP: {dev['system-ip']:<12} Name: {dev['host-name']}")

if __name__ == "__main__":
    main()