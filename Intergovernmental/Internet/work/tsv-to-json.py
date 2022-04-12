#!/usr/bin/env python

import json
import sys
from typing import Dict


def to_structure(asn_record: str) -> Dict[str, str]:
    country, asn, name = asn_record.split("\t")
    return {"key": asn, "value": name.strip()}


data_structure = []

for asn_record in sys.stdin.readlines():
    data_structure.append(to_structure(asn_record))

print(json.dumps(data_structure))
