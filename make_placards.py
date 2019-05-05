#!/usr/bin/env python

import argparse
import json
from io import open

import jinja2
import mistune

def create_parser():
    parser = argparse.ArgumentParser(
        description="Generate printable placards based on JSON metadata."
    )
    parser.add_argument("file", metavar="FILE", help="the input file to read")
    parser.add_argument(
        "-o",
        "--output",
        dest="outfile",
        default="placards_generated.html",
        help="optional output filename",
    )
    parser.add_argument(
        "-t",
        "--template",
        dest="template",
        default="placards_template.html",
        help="optional template filename",
    )
    return parser


def markdownformat(value):
    return MARKDOWN(str(value))


def create_jinja_env():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("."),
        autoescape=jinja2.select_autoescape(["html"])
    )
    env.filters['markdown'] = markdownformat
    return env


MARKDOWN = mistune.Markdown()
PARSER = create_parser()
ARGS = PARSER.parse_args()
ENV = create_jinja_env()
TEMPLATE = ENV.get_template("placards_template.html")

with open(ARGS.file) as file:
    WORKS = json.load(file)["works"]

    with open(ARGS.outfile, "w", encoding="utf-8") as result:
        result.write(TEMPLATE.render(works=WORKS))
