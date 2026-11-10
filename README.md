# Synthetic data generator with metadata

Generate a CSV of fictional records and a companion dataset card. The card
records a UTC timestamp, row count, field descriptions, purpose, and generation
method. The fixed schema contains ID, name, email, address, and signup date.

## Run the example

```bash
python -m pip install -r requirements.txt
python generator.py --num-records 3 --output output/data.csv
```

The command writes three data rows plus a header to `output/data.csv` and
creates `output/dataset_card.md`. Values and dates vary between runs.
Use the generated records as fixtures for demos and validation experiments.
Record generation uses Faker rather than anonymizing an input dataset.

## Verify

```bash
python -m pip install pytest
python -m pytest -q
```

The tests check the documented CLI, nested output directories, row counts,
the dataset card, and rejection of negative counts before output is written.
