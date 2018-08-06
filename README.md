# asn-subnet-parser
Just a draft.

Allows getting summarized networks list for chosen ASN. Can be used to implement whitelist/blacklist for a firewall.

## Usage

> `python main.py --help`

```usage: main.py [-h] --asn ASN [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --asn ASN        Autonomous System Number
  --output OUTPUT  File to save summarized networks
  ```
  
> `python main.py --asn 20473 --output networks.txt`

> `head networks.txt`

```
4.79.145.0/24
5.35.192.0/21
8.2.120.0/23
8.2.122.0/24
8.3.5.0/24
8.3.6.0/23
8.3.28.0/23
8.6.2.0/23
8.6.8.0/23
8.6.15.0/24
```

## Installation and requirements

1. Python 3.6 (or remove f-string instead)
2. `pip install -r requirements.txt` (requests, netaddr and beautifulsoup4)
