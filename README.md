# CSV to Register
Converts a CSV file to RSF format for importing into a Register
(e.g. via [orc][orc]).

## Usage
With Python 3 and [Pipenv][pipenv] installed:

1. Clone this repository and run `pipenv install` within it.
2. Run `pipenv shell` to activate a local environment shell.
3. Run the script using `python bin/cli.py <CSV_FILE> --key-field <FIELD_NAME> > output.rsf`

You can pipe the CSV file to it by passing `-` as the file name argument, e.g. `cat file.csv | python bin/cli.py -k id > output.rsf`

[orc]: https://github.com/register-dynamics/orc
[pipenv]: https://pipenv.readthedocs.io/en/latest/
