from operator import itemgetter
import requests

def main():
    """
    Execution begins here
    """
    api_path = "https://10.10.20.49/restconf/data"

    #Disable obnoxious SSL verification warning for the sandbox
    requests.packages.urllib3.disable_warnings()

    basic_auth = ("developer", "C1sco12345")

    accept_list = [
        "application/vnd.yang.api+json",
        "application/vnd.yang.datastore+json",
        "application/vnd.yang.data+json",
        "application/vnd.yang.collection+json",
    ]
    get_headers = {"Accept": ",".join(accept_list)}

    arp_table = "device,ip_addr,mac_addr,interface\n"

    for device in ["internet-rtr01", "bogus"]:
        device_url = f"{api_path}/tailf-ncs:devices/device={device}"

        get_resp = requests.get(
            f"{device_url}/live-status/tailf-ned-cisco-ios-stats:arp",
            auth=basic_auth,
            headers=get_headers,
            verify=False,
        )

        if get_resp.status_code != 200:
            print(f"Could not collect {device} ARP stats; skipping FOOOL!!!!")
            continue
        addr_list = get_resp.json()["tailf-ned-cisco-ios-stats:arp"]
        print(addr_list)
        #import json; print(json.dumps(get_resp.json(), indent=2))

        if "address" in addr_list:
            addresses = addr_list["address"]
            for addr in sorted(addresses, key=itemgetter("interface")):

                arp_table += (
                    f"{device},"
                    f"{addr['ip']},"
                    f"{addr['hardware-addr']},"
                    f"{addr['interface']},\n"
                )
        if "vrf" in addr_list:
            vrfs = addr_list["vrf"]

            for vrf in vrfs:
                vrf_name = vrf["name"]
                vrf_addresses = vrf["address"]
                for addr in sorted(vrf_addresses, key=lambda x: x.get("interface", "")):
                    arp_table += (
                        f"{device},"
                        f"{vrf_name},"
                        f"{addr['ip']},"
                        f"{addr['hardware-addr']},"
                        f"{addr.get('interface', 'N/A')}\n"
                    )
    outfile = "arp_stats.csv"
    with open(outfile, "w") as handle:
        handle.write(arp_table)
    print(f"Use 'column -S, -t {outfile}' to view from shell")

if __name__ == "__main__":
    main()

