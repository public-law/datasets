#!/usr/bin/env python

import json
import sys
from typing import Dict


def to_structure(asn_record: str) -> Dict[str, str]:
    """Convert one line of a TSV file to the desired
    KV dict representation.
    """
    country, asn, name = asn_record.strip().split("\t")
    return {"key": asn, "value": name}


structured_data = [to_structure(asn_record) for asn_record in sys.stdin.readlines()]

print(json.dumps(structured_data))
