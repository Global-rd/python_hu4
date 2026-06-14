"""
Homework 10: Selenium scraper for quotes.toscrape.com.
Author: Budai Krisztian
"""

from quotes_scraper.app import App
from quotes_scraper.config import AppConfig


def main() -> None:
    """Scrape top tag quotes and write them to CSV."""
    config: AppConfig = AppConfig.from_env()
    App(config).run()


if __name__ == "__main__":
    main()
