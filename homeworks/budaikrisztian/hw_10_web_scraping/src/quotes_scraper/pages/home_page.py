"""
Home page helpers for quotes.toscrape.com.
"""

from selenium.webdriver.common.by import By

from quotes_scraper.pages.base_page import BasePage, Locator, PageElement


class HomePage(BasePage):
    """Read the Top Ten tags from the home page."""

    # Links in the sidebar Top Ten tags list.
    TOP_TAG_LINKS: Locator = (By.CSS_SELECTOR, ".tag-item a.tag")

    def get_top_tags(self) -> list[str]:
        """Return the tag names from the Top Ten tags block."""
        tag_links: list[PageElement] = self.find_all_visible(
            self.TOP_TAG_LINKS
        )

        return [
            tag_link.text.strip()
            for tag_link in tag_links
            if tag_link.text.strip()
        ]
