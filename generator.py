"""CLI script to generate synthetic data and capture governance metadata."""

from __future__ import annotations

import csv
import datetime
from pathlib import Path

import click
from faker import Faker

# Import our utility for writing the dataset card. We perform the import here
# to avoid circular dependencies and to keep the CLI at the top-level.  The
# `write_dataset_card` function records metadata about the generated data to
# assist with governance and documentation.
from .utils import write_dataset_card


fake = Faker()


def generate_record():
    """Generate a single synthetic record."""
    return {
        "id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address().replace("\n", ", "),
        "signup_date": fake.date_between(start_date="-2y", end_date="today").isoformat(),
    }


@click.command()
@click.option(
    "--output",
    type=click.Path(dir_okay=False, path_type=Path),
    default="data.csv",
    show_default=True,
    help="Path to the CSV file where synthetic data will be written.",
)
@click.option(
    "--num-records",
    type=int,
    default=100,
    show_default=True,
    help="Number of synthetic records to generate.",
)
def main(output: Path, num_records: int):
    """Generate a synthetic dataset and its data card.

    This command writes a CSV file with ``num_records`` rows containing
    synthetic user data.  After generation, it creates or updates a
    ``dataset_card.md`` file in the same directory as ``output`` that
    describes the fields, number of records, and generation timestamp.
    """
    # Ensure the output directory exists. ``parents=True`` allows creation of
    # intermediate directories and ``exist_ok=True`` avoids errors if it
    # already exists.
    output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["id", "name", "email", "address", "signup_date"]
    # Open the CSV file and write headers followed by generated records.
    with output.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_records):
            writer.writerow(generate_record())
    # Define human-readable descriptions for each field. These will be
    # recorded in the dataset card.
    fields = {
        "id": "Unique identifier for the record (UUID).",
        "name": "Randomly generated full name.",
        "email": "Synthetic email address.",
        "address": "Synthetic mailing address with street, city, and country.",
        "signup_date": "Random date within the past two years.",
    }
    # Write or update the dataset card in the same directory.  The card
    # filename is fixed to ``dataset_card.md`` but could be parameterized.
    card_path = output.parent / "dataset_card.md"
    write_dataset_card(card_path, num_records, fields)
    click.echo(f"Generated {num_records} records to {output} and updated {card_path}")


if __name__ == "__main__":  # pragma: no cover
    main()