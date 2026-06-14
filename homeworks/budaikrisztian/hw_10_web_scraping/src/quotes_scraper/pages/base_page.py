"""
Shared Selenium page helpers.
"""

from typing import Protocol, cast

from selenium.webdriver.common.by import ByType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

# Selenium locator pair: selector strategy and selector value.
Locator = tuple[ByType, str]


class TypedWebElement(Protocol):
    """Typed subset of Selenium WebElement methods used by page objects."""

    def find_element(self, by: ByType, value: str) -> WebElement:
        """Find one child element."""
        ...

    def get_attribute(self, name: str) -> str | None:
        """Read one element attribute."""
        ...


class PageElement:
    """Typed wrapper around Selenium WebElement."""

    def __init__(self, element: WebElement) -> None:
        """Initialize the wrapper with a Selenium element."""
        self.element: WebElement = element

    @property
    def text(self) -> str:
        """Return the element text."""
        return self.element.text

    def find_child(self, locator: Locator) -> "PageElement":
        """Find and wrap one child element."""
        typed_element: TypedWebElement = cast(TypedWebElement, self.element)
        child_element: WebElement = typed_element.find_element(*locator)

        return PageElement(child_element)

    def get_attribute(self, name: str) -> str | None:
        """Read an element attribute."""
        typed_element: TypedWebElement = cast(TypedWebElement, self.element)

        return typed_element.get_attribute(name)


class BasePage:
    """Base class for Selenium page objects."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """Initialize page helpers."""
        self.driver: WebDriver = driver
        self.wait: WebDriverWait[WebDriver] = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        """Open the given URL in the current browser."""
        self.driver.get(url)

    def find_all_visible(self, locator: Locator) -> list[PageElement]:
        """Find all visible elements for a Selenium locator."""
        elements: list[WebElement] = list(
            self.wait.until(
                expected.visibility_of_all_elements_located(locator)
            )
        )

        return [PageElement(element) for element in elements]

    def find_elements(self, locator: Locator) -> list[PageElement]:
        """Find all elements for a Selenium locator without waiting."""
        elements: list[WebElement] = self.driver.find_elements(*locator)

        return [PageElement(element) for element in elements]
