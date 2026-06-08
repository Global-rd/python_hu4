"""
Selenium browser factory.
"""

from collections.abc import Iterator
from contextlib import contextmanager

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class DriverFactory:
    """Create and manage configured Chrome drivers."""

    DEFAULT_ARGUMENTS: tuple[str, ...] = (
        "--window-size=1920,1080",
        "--disable-gpu",
        "--no-sandbox",
    )

    def __init__(self, headless: bool = True) -> None:
        """Initialize the factory with browser configuration."""
        self.headless: bool = headless

    def _create_options(self) -> Options:
        """Create Chrome options from the factory configuration."""
        options: Options = Options()

        if self.headless:
            options.add_argument("--headless=new")

        for argument in self.DEFAULT_ARGUMENTS:
            options.add_argument(argument)

        return options

    def _create_driver(self) -> WebDriver:
        """Create a configured Chrome driver for scraping."""
        options: Options = self._create_options()

        try:
            return webdriver.Chrome(options=options)
        except WebDriverException as error:
            raise RuntimeError(
                "ChromeDriver could not start. On Linux, install the "
                "missing system libraries with: "
                "sudo apt-get install libnss3 libnspr4"
            ) from error

    @staticmethod
    def _quit_driver(driver: WebDriver) -> None:
        """Close Chrome and explicitly stop the ChromeDriver service."""
        try:
            driver.quit()
        finally:
            driver.service.stop()

    @contextmanager
    def managed_driver(self) -> Iterator[WebDriver]:
        """Create a Chrome driver and always clean it up."""
        driver: WebDriver = self._create_driver()

        try:
            yield driver
        finally:
            self._quit_driver(driver)
