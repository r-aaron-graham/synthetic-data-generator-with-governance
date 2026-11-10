import csv
from pathlib import Path
import unittest
from click.testing import CliRunner
from generator import main

class GeneratorTests(unittest.TestCase):
    def test_cli_writes_requested_rows_and_card(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(main, ["--num-records", "3", "--output", "nested/data.csv"])
            self.assertEqual(result.exit_code, 0, result.output)
            with Path("nested/data.csv").open() as source:
                self.assertEqual(len(list(csv.DictReader(source))), 3)
            self.assertIn("3", Path("nested/dataset_card.md").read_text())

    def test_negative_count_fails_before_output(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(main, ["--num-records", "-1"])
            self.assertNotEqual(result.exit_code, 0)
            self.assertFalse(Path("data.csv").exists())
