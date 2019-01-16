#!/usr/bin/env python

import argparse
from codecs import open
import jinja2
import json

parser = argparse.ArgumentParser(description='Generate printable placards based on JSON metadata.')
parser.add_argument('file', metavar='FILE', type=file, help='the input file to read')
parser.add_argument('-o', '--output', dest='outfile', default='placards_generated.html',
                    help='optional output filename')
parser.add_argument('-t', '--template', dest='template', default='placards_template.html',
                    help='optional template filename')

args = parser.parse_args()

works_wrapper = json.load(args.file)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('.'),
    autoescape=jinja2.select_autoescape(['html'])
)
template = env.get_template('placards_template.html')
with open(args.outfile, 'w', encoding='utf-8') as result:
    result.write(template.render(works=works_wrapper['works']))
