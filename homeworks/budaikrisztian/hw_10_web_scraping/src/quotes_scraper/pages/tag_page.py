"""
Tag page helpers for quotes.toscrape.com.
"""

from selenium.webdriver.common.by import By

from quotes_scraper.models.quote import Quote
from quotes_scraper.pages.base_page import BasePage, Locator, PageElement


class TagPage(BasePage):
    """Read quotes and pagination data from a tag page."""

    # Quote container on the current tag page.
    QUOTES: Locator = (By.CSS_SELECTOR, ".quote")

    # Quote text inside a quote container.
    QUOTE_TEXT: Locator = (By.CSS_SELECTOR, ".text")

    # Author name inside a quote container.
    AUTHOR: Locator = (By.CSS_SELECTOR, ".author")

    # Pagination link to the next page for the current tag.
    NEXT_LINK: Locator = (By.CSS_SELECTOR, "li.next a")

    def get_quotes(self, original_tag: str) -> list[Quote]:
        """Return all quotes from the current page for one top tag."""
        quotes: list[Quote] = []

        for quote_element in self.find_all_visible(self.QUOTES):
            quote_text: PageElement = quote_element.find_child(
                self.QUOTE_TEXT,
            )
            author: PageElement = quote_element.find_child(
                self.AUTHOR,
            )

            quotes.append(
                Quote(
                    tag=original_tag,
                    author=author.text.strip(),
                    quote=quote_text.text.strip(),
                )
            )

        return quotes

    def get_next_page_url(self) -> str | None:
        """Return the next page URL if pagination has another page."""
        next_links: list[PageElement] = self.find_elements(self.NEXT_LINK)

        if not next_links:
            return None

        return next_links[0].get_attribute("href")
