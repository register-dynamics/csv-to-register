import csv
import json
from datetime import datetime
from hashlib import sha256

import click
from tqdm import tqdm # progress bar

@click.command()
@click.argument('csv_file', type=click.File())
@click.option('-k', '--key-field', required=True, help='Field to use as key')
@click.option('-m', '--metadata', 'metadata_file', type=click.File(), help='JSON-formatted metadata')
def csv_to_rsf(csv_file, key_field, metadata_file):
  """Convert CSV file to RSF format"""
  print('assert-root-hash\t{}'.format(hash('')))

  timestamp = get_timestamp()

  if metadata_file:
    metadata = json.load(metadata_file)
    for key, value in metadata.items():
      [add_item, append_entry] = format_rsf_item(region='system', key=key,
                                    timestamp=timestamp, value=value)
      print(add_item)
      print(append_entry)

  reader = csv.DictReader(csv_file)
  for row in tqdm(reader):
    key = row.get(key_field) # TODO: Output rows missing keys to stderr
    [add_item, append_entry] = format_rsf_item(region='user', key=key,
                                timestamp=timestamp, value=row)
    print(add_item)
    print(append_entry)

def get_root_hash():
  return hash('')

def get_timestamp():
  return datetime.utcnow().isoformat(timespec='seconds') + 'Z'

def format_rsf_item(region, key, timestamp, value):
  value_json = json.dumps(value)
  value_hash = hash(value_json)

  return [
    'add-item\t{}'.format(value_json),
    'append-entry\t{}\t{}\t{}\t{}'.format(
      region, key, timestamp, value_hash),
  ]

def hash(payload):
  return 'sha-256:' + sha256(payload.encode('utf-8')).hexdigest()

if __name__ == '__main__':
  csv_to_rsf()
