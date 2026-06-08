"""
Scraper workflow for the top tags on quotes.toscrape.com.
"""

from concurrent.futures import ThreadPoolExecutor

from selenium.webdriver.remote.webdriver import WebDriver

from quotes_scraper.browser.driver_factory import DriverFactory
from quotes_scraper.models.quote import Quote
from quotes_scraper.pages.home_page import HomePage
from quotes_scraper.pages.tag_page import TagPage


class QuotesScraper:
    """Scrape quotes for the top ten tags."""

    BASE_URL: str = "https://quotes.toscrape.com"

    def __init__(
        self,
        driver_factory: DriverFactory,
        max_workers: int = 3,
    ) -> None:
        """Initialize the scraper with browser dependencies."""
        self.driver_factory: DriverFactory = driver_factory
        self.max_workers: int = max_workers

    def scrape_top_tag_quotes(self) -> list[Quote]:
        """Scrape all quotes that belong to the current top ten tags."""
        top_tags: list[str] = self._get_top_tags()

        if self.max_workers == 1:
            return self._scrape_tag_quotes_sequentially(top_tags)

        return self._scrape_tag_quotes_concurrently(top_tags)

    def _scrape_tag_quotes_sequentially(
        self,
        top_tags: list[str],
    ) -> list[Quote]:
        """Scrape tag pages one by one without a thread pool."""
        all_quotes: list[Quote] = []

        for tag in top_tags:
            all_quotes.extend(self._scrape_tag_quotes_with_new_driver(tag))

        return all_quotes

    def _scrape_tag_quotes_concurrently(
        self,
        top_tags: list[str],
    ) -> list[Quote]:
        """Scrape tag pages with one browser per worker thread."""
        all_quotes: list[Quote] = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for tag_quotes in executor.map(
                self._scrape_tag_quotes_with_new_driver,
                top_tags,
            ):
                all_quotes.extend(tag_quotes)

        return all_quotes

    def _get_top_tags(self) -> list[str]:
        with self.driver_factory.managed_driver() as driver:
            home_page: HomePage = HomePage(driver)
            home_page.open(self.BASE_URL)

            return home_page.get_top_tags()

    def _scrape_tag_quotes_with_new_driver(self, tag: str) -> list[Quote]:
        with self.driver_factory.managed_driver() as driver:
            return self._scrape_tag_quotes(tag, driver)

    def _scrape_tag_quotes(self, tag: str, driver: WebDriver) -> list[Quote]:
        tag_page: TagPage = TagPage(driver)
        tag_page.open(f"{self.BASE_URL}/tag/{tag}/")

        quotes: list[Quote] = []

        while True:
            quotes.extend(tag_page.get_quotes(tag))
            next_page_url: str | None = tag_page.get_next_page_url()

            if next_page_url is None:
                break

            tag_page.open(next_page_url)

        return quotes
