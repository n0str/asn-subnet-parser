import argparse
import re
import sys
import requests
from bs4 import BeautifulSoup
from netaddr import IPAddress, cidr_merge, IPNetwork


def parse_asn(content):
    soup = BeautifulSoup(content, 'html.parser')
    results = []
    nets = []
    for element in soup.find('div', id='ipv4-data').find('table', id="block-table").find_all('tr')[1:]:
        ip, company, num = [e.text.strip() for e in element.find_all('td')]
        results.append((ip, company, num))
        nets.append(IPNetwork(ip))
    return results, '\n'.join([str(net) for net in cidr_merge(nets)])


def get_asn(number):
    try:
        r = requests.get(f"https://ipinfo.io/AS{number}")
        if not r.status_code == 200:
            print(f"Cannot load website: https://ipinfo.io/AS{number}. Status code is {r.status_code}")
            exit(1)
        return parse_asn(r.content)

    except Exception as e:
        print(f"Exception: {e}")
        exit(1)
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--asn', type=int, required=True, help="Autonomous System Number")
    parser.add_argument('--output', help="File to save summarized networks")
    options = parser.parse_args(sys.argv[1:])

    networks, nsumm = get_asn(options.asn)
    if options.output:
        with open(f"{options.output}", "w") as w:
            w.write(nsumm)
