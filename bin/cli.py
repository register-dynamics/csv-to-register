import csv
import json
from datetime import datetime
from hashlib import sha256

import click
from slugify import slugify
from tqdm import tqdm # progress bar

@click.command()
@click.argument('csv_file', type=click.File())
@click.option('-k', '--key-field', required=True, help='Field to use as key')
@click.option('--region', default='user')
def csv_to_rsf(csv_file, key_field, region):
  """Convert CSV file to RSF format"""
  print('assert-root-hash\t{}'.format(hash('')))

  timestamp = get_timestamp()
  reader = csv.DictReader(csv_file)
  for row in tqdm(reader):
    key = sanitise_key(row.get(key_field)) # TODO: Output rows missing keys to stderr
    row_json = json.dumps(row)
    row_hash = hash(row_json)
    print('add-item\t{}'.format(row_json))
    print('append-entry\t{}\t{}\t{}\t{}'.format(
          region, key, timestamp, row_hash))

def get_root_hash():
  return hash('')

def sanitise_key(raw_key):
  return slugify(raw_key, separator='_', lowercase=False)

def get_timestamp():
  return datetime.utcnow().isoformat(timespec='seconds') + 'Z'

def hash(payload):
  return 'sha-256:' + sha256(payload.encode('utf-8')).hexdigest()

if __name__ == '__main__':
  csv_to_rsf()
