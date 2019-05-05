#!/usr/bin/env python

import argparse
import json
from io import open

import jinja2

PARSER = argparse.ArgumentParser(
    description="Generate printable placards based on JSON metadata."
)
PARSER.add_argument("file", metavar="FILE", help="the input file to read")
PARSER.add_argument(
    "-o",
    "--output",
    dest="outfile",
    default="placards_generated.html",
    help="optional output filename",
)
PARSER.add_argument(
    "-t",
    "--template",
    dest="template",
    default="placards_template.html",
    help="optional template filename",
)

ARGS = PARSER.parse_args()

ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader("."), autoescape=jinja2.select_autoescape(["html"])
)
TEMPLATE = ENV.get_template("placards_template.html")

with open(ARGS.file) as file:
    WORKS = json.load(file)["works"]

    with open(ARGS.outfile, "w", encoding="utf-8") as result:
        result.write(TEMPLATE.render(works=WORKS))
