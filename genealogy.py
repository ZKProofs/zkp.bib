#!/usr/bin/env python3
import argparse
import base64
import bibtexparser
import json


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--implements', action='store_true',
                    help='show implementation links')
args = parser.parse_args()

# Parse BibTeX to get metadata
with open('zkp.bib') as f:
    db = bibtexparser.load(f)

buildson = [
    (entry['ID'], entry['buildson'])
    for entry in db.entries if 'buildson' in entry.keys()
]

implements = [
    (entry['ID'], entry['implements'])
    for entry in db.entries if 'implements' in entry.keys()
] if args.implements else []

# Convert to Mermaid
mermaid = 'graph TD\n' + '\n'.join([
    '%s --> %s' % (parent.strip(), entry[0]) for entry in buildson for parent in entry[1].split(',')
] + [
    '%s -.-> %s' % (parent.strip(), entry[0]) for entry in implements for parent in entry[1].split(',')
])

# Construct Mermaid online viewer string
viewer = {
    'code': mermaid,
    'mermaid': {
        'theme': 'default',
    },
}
encoded = str(base64.b64encode(bytes(json.dumps(viewer), 'UTF8'), b'-_'), 'UTF8')

print('https://mermaidjs.github.io/mermaid-live-editor/#/view/%s' % encoded)
