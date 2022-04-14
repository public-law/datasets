#!/usr/bin/env python

import json
import re
from typing import Pattern

INPUT_FILE = "../all-asns-org-names.json_lines"

EDU = re.compile(
    r""" academy
        | college
        | edu\b
        | \-esd
        | institut
        | library
        | school
        | schule
        | suny
        | universidad
        | university """,
    re.IGNORECASE | re.VERBOSE,
)

GOV = re.compile(
    r""" administration
        | agency
        | authority
        | board
        | bureau
        | city\Wof
        | commission
        | county
        | court
        | department
        | \bDNIC\b
        | gov
        | justica
        | justice
        | ministerio
        | ministry
        | municipal
        | police
        | policia
        | public\Wutilities\Wcommission
        | revenue
        | state\Wof
        | territory
        | tribunal
        | united nations """,
    re.IGNORECASE | re.VERBOSE,
)

MEDIA = re.compile(
    r""" broadcasting
        | journal
        | \bmedia\b
        | news
        | \bpress
        | publish
        | reuters
        | televis
        | times
        | verlag
        | washpost
        | zdf """,
    re.IGNORECASE | re.VERBOSE,
)

NGO = re.compile(
    r""" association
        | \bassoc\b
        | church
        | committee
        | credit\bunion
        | foundation
        | \bfund\b
        | nonprofit
        | non-profit
        | society
        | \bUN\b
        | united\bnation """,
    re.IGNORECASE | re.VERBOSE,
)

DATA_FILTERS = [
    {"regex": EDU, "file_slug": "edu"},
    {"regex": GOV, "file_slug": "gov"},
    {"regex": MEDIA, "file_slug": "media"},
    {"regex": NGO, "file_slug": "ngo"},
]


def json_line_to_tsv(line: str) -> str:
    """Produce the standard TSV format:
    Country ASN Name + OrgName
    """
    data = json.loads(line)
    return f"{data['Country']}\t{data['ASNumber']}\t{data['ASName']} {data['OrgName']}".strip()


for data_filter in DATA_FILTERS:
    regex: Pattern[str] = data_filter["regex"]
    slug: str = data_filter["file_slug"]
    output_file = f"../asn-{slug}-list.tsv"

    with open(INPUT_FILE, "r", encoding="utf8") as f:
        records = f.readlines()
        matching_records = [r for r in records if regex.search(r)]
        tsv_records = [json_line_to_tsv(j) for j in matching_records]

    with open(output_file, "w", encoding="utf8") as f:
        f.writelines([record + "\n" for record in tsv_records])
