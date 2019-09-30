# CSV to Register
Converts a CSV file to RSF format for importing into a Register
(e.g. via [orc][orc]).

## Usage
With Python 3 and [Pipenv][pipenv] installed:

1. Clone this repository and run `pipenv install` within it.
2. Run `pipenv shell` to activate a local environment shell.
3. Run the script using `python bin/cli.py`

```
Usage: cli.py [OPTIONS] CSV_FILE

  Convert CSV file to RSF format

Options:
  -k, --key-field TEXT     Field to use as key  [required]
  -m, --metadata FILENAME  JSON-formatted metadata
  --help                   Show this message and exit.
```

Basic example:

```
python bin/cli.py --key id data.csv > output.rsf
```

You can pipe the CSV file to it by passing `-` as the file name argument.

```
cat file.csv | python bin/cli.py -k id - > output.rsf
```

You can include metadata in the output by passing a JSON file to the `--metadata` flag. The JSON file should be an object where the top-level keys are used as entry keys. 

```
python bin/cli.py -k id -m metadata.json data.csv > output.rsf
```

[orc]: https://github.com/register-dynamics/orc
[pipenv]: https://pipenv.readthedocs.io/en/latest/
