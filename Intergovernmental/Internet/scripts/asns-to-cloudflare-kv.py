#!/usr/bin/env python

import json
import sys
from typing import Dict

#
# asns-to-cloudflare-kv.py
#
# Read JSON lines from stdin and output JSON text
# to stdout which is suited for bulk upload with
# Cloudflare wrangler.
#


def to_structure(asn_record: str) -> Dict[str, str]:
    """Convert one line of a TSV file to the desired
    KV dict representation.
    """
    _country, asn, name = asn_record.strip().split("\t")
    return {"key": asn, "value": name}


structured_data = [to_structure(asn_record) for asn_record in sys.stdin.readlines()]

print(json.dumps(structured_data, indent=4))
