"""
scraper.py
----------
Selenium-alapú scraper a https://quotes.toscrape.com/ oldalhoz (19. óra mintája).
Összegyűjti a top 10 tag nevét, majd tag-enként végigmegy az összes oldalon
(pagination), és kiszedi az idézet szövegét és a szerzőt.
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://quotes.toscrape.com"

# A HTML-selectorok egy helyen (best practice a 19. óráról):
TOP_TAGS_SELECTOR = ".tags-box .tag-item a.tag"   # CSAK a top 10 tag (nem a quote-ok tagjei)
QUOTE_SELECTOR = "div.quote"
QUOTE_TEXT_SELECTOR = "span.text"
QUOTE_AUTHOR_SELECTOR = "small.author"
NEXT_BUTTON_SELECTOR = "li.next a"


class QuotesScraper:
    def __init__(self):
        self.driver = None

    def initialize_webdriver(self):
        """Létrehozza a Chrome WebDrivert."""
        options = Options()
        # Ha NEM akarod látni a böngészőt, vedd ki a komment-jelet az alábbi sorból:
        # options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)

    def get_top_tags(self):
        """A főoldalról összegyűjti a top 10 tag nevét."""
        self.driver.get(BASE_URL)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, TOP_TAGS_SELECTOR))
        )
        elements = self.driver.find_elements(By.CSS_SELECTOR, TOP_TAGS_SELECTOR)
        return [el.text for el in elements]

    def scrape_tag(self, tag):
        """Egy taghez tartozó összes idézet kiszedése, lapozással."""
        results = []
        page = 1
        while True:
            # Az url manipulálása a tag neve alapján (a feladat tippje szerint).
            url = f"{BASE_URL}/tag/{tag}/page/{page}/"
            self.driver.get(url)

            quotes = self.driver.find_elements(By.CSS_SELECTOR, QUOTE_SELECTOR)
            if not quotes:
                # Ha ezen az oldalon már nincs idézet, kilépünk.
                break

            for quote in quotes:
                text = quote.find_element(By.CSS_SELECTOR, QUOTE_TEXT_SELECTOR).text
                author = quote.find_element(By.CSS_SELECTOR, QUOTE_AUTHOR_SELECTOR).text
                results.append({"tag": tag, "author": author, "quote": text})

            # Pagination: van-e "Next" gomb? Ha nincs, ez volt az utolsó oldal.
            next_buttons = self.driver.find_elements(By.CSS_SELECTOR, NEXT_BUTTON_SELECTOR)
            if not next_buttons:
                break

            page += 1
            time.sleep(0.5)  # apró udvariassági szünet a szerver felé

        return results

    def quit(self):
        """Bezárja a böngészőt."""
        if self.driver:
            self.driver.quit()