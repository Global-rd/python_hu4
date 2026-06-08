"""
Application orchestration for the quotes scraper.
"""

from datetime import datetime
from pathlib import Path
from time import perf_counter

from quotes_scraper.browser.driver_factory import DriverFactory
from quotes_scraper.config import AppConfig
from quotes_scraper.models.quote import Quote
from quotes_scraper.scrapers.quotes_scraper import QuotesScraper
from quotes_scraper.storage.csv_writer import CsvWriter


class App:
    """Coordinate browser setup, scraping and CSV export."""

    def __init__(self, config: AppConfig) -> None:
        """Initialize the application with runtime configuration."""
        self.config: AppConfig = config

    @staticmethod
    def _create_timestamped_output_path(output_path: Path) -> Path:
        """Create an output path with the current local timestamp."""
        timestamp: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        return output_path.with_name(
            f"{output_path.stem}_{timestamp}{output_path.suffix}"
        )

    def run(self) -> int:
        """Scrape quotes, save them to CSV and return the saved row count."""
        start_time: float = perf_counter()
        driver_factory: DriverFactory = DriverFactory(
            headless=self.config.headless
        )

        scraper: QuotesScraper = QuotesScraper(
            driver_factory=driver_factory,
            max_workers=self.config.max_workers,
        )
        quotes: list[Quote] = scraper.scrape_top_tag_quotes()
        output_path: Path = self._create_timestamped_output_path(
            self.config.output_path
        )

        CsvWriter(output_path).write(quotes)

        saved_quote_count: int = len(quotes)
        elapsed_seconds: float = perf_counter() - start_time
        print(
            f"{saved_quote_count} quotes successfully saved to: "
            f"{output_path} in {elapsed_seconds:.2f} seconds"
        )

        return saved_quote_count
