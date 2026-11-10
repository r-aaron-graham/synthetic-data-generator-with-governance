"""Utility functions for the synthetic data generator."""

import datetime
from pathlib import Path


def write_dataset_card(path, num_records, fields):
    """Create or update a dataset card with metadata about the generation."""
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    card = "# Dataset Card\n\n"
    card += f"**Generated on:** {timestamp}\n\n"
    card += f"**Number of records:** {num_records}\n\n"
    card += "**Fields:**\n\n"
    for name, desc in fields.items():
        card += f"- **{name}**: {desc}\n"
    card += "\n**Purpose:** Synthetic dataset for testing and demonstration.\n"
    card += "\n**Privacy:** No real user data is included. Records are generated using Faker.\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(card)