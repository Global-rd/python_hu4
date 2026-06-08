"""
CSV writer for scraped quotes.
"""

import csv
from pathlib import Path

from quotes_scraper.models.quote import Quote


class CsvWriter:
    """Write quotes into a CSV file."""

    def __init__(self, file_path: str | Path) -> None:
        """Initialize the writer with the output path."""
        self.file_path: Path = Path(file_path)

    def write(self, quotes: list[Quote]) -> None:
        """Write quotes with tag, author and quote columns."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open(
            "w",
            encoding="utf-8",
            newline="",
        ) as csv_file:
            fieldnames: list[str] = ["tag", "author", "quote"]
            writer: csv.DictWriter[str] = csv.DictWriter(
                csv_file,
                fieldnames=fieldnames,
            )

            writer.writeheader()

            for quote in quotes:
                writer.writerow(
                    {
                        "tag": quote.tag,
                        "author": quote.author,
                        "quote": quote.quote,
                    }
                )
