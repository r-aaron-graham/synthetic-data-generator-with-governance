# Synthetic Data Generator with Governance

This repository provides tools to generate synthetic datasets while capturing governance
metadata.  Synthetic data can be used for testing, training, and demos without exposing
real user information.  The included generator uses the Faker library to produce realistic
records and writes out a CSV file along with a data card describing the dataset.

## Features

* Generate tabular data with configurable columns (e.g. names, emails, addresses, dates).
* Capture metadata such as generation time, anonymization techniques, and intended use.
* Output a dataset card (`dataset_card.md`) summarizing the data and governance considerations.

## Usage

Install dependencies and run the generator:

```bash
pip install -r requirements.txt
python generator.py --output data.csv --num-records 100
```

The script will produce `data.csv` with 100 synthetic records and create/update
`dataset_card.md` with metadata about the generation run.

## Extending

To add new fields, modify the `generate_record` function in `generator.py`.  For
governance, you can expand the dataset card to include information such as data sources,
legal considerations, and privacy guarantees.