import requests

def main():

    api_path = "https://sandboxapicdc.cisco.com/api"
    body = {"aaaUser": {"attributes": {"name": "admin", "pwd": "!v3G@!4@Y"}}}

    requests.packages.urllib3.disable_warnings()

    auth_resp = requests.post(
        f"{api_path}/aaaLogin.json", json=body, verify=False
    )

    auth_resp.raise_for_status()
    auth = auth_resp.json()

    token = auth["imdata"][0]["aaaLogin"]["attributes"]["token"]

    headers = {"Cookie": f"APIC-Cookie={token}"}
    epg_resp = requests.get(
        f"{api_path}/class/fvAEPg.json", headers=headers, verify=False
    )

    epg_resp.raise_for_status()
    epgs =epg_resp.json()

    print(f"EPGs found: {epgs['totalCount']}")
    for epg in epgs["imdata"]:
        print(f"  Name: {epg['fvAEPg']['attributes']['dn']}")

if __name__ == "__main__":
    main()