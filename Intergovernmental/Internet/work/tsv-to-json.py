#!/usr/bin/env python

import json
import sys


data_structure = []

for asn_record in sys.stdin.readlines():
    try:
        country, asn, name = asn_record.split("\t")
        data_structure.append({"key": asn, "value": name.strip()})
    except (ValueError):
        print(f"Skipping {asn_record}")

print(json.dumps(data_structure))
