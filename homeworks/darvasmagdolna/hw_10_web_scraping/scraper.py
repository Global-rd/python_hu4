from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
from datetime import datetime as dt

import selectors


class QuoteScrapper:
    def __init__(self):
        self.driver = None

    def initialize_webdriver(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def get_top_10_tags(self, base_url):
        self.driver.get(base_url)

        tag_elements = self.driver.find_elements(By.CSS_SELECTOR, selectors.TAG_LINKS_CSS)

        top_10_tags = []
        for i in range(10):
            top_10_tags.append(tag_elements[i].text)

        return top_10_tags

    def scrape_tag_quotes(self, base_url, tag):
        page = 1
        result = []
        has_next = True

        while has_next:
            url = f"{base_url}/tag/{tag}/page/{page}"
            self.driver.get(url)

            quotes = self.driver.find_elements(By.CSS_SELECTOR, selectors.QUOTE_BLOCK_CSS)

            if not quotes:
                has_next = False
                continue

            for quote in quotes:
                text = quote.find_element(By.CSS_SELECTOR, selectors.QUOTE_TEXT_CSS)
                author = quote.find_element(By.CSS_SELECTOR, selectors.QUOTE_AUTHOR_CSS)

                result.append({
                    "tag": tag,
                    "author": author,
                    "quote": text,
                    "scrape_timestamp": dt.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "url": url
                })

            next_button = self.driver.find_elements(By.CSS_SELECTOR, selectors.NEXT_BUTTON_CSS)
            has_next = bool(next_button)
            if next_button:
                page += 1

        return result

    @staticmethod
    def save_to_csv(data, filename):
        with open(filename, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["tag", "author", "quote", "scrape_timestamp", "url"])

            for row in data:
                writer.writerow([
                    row["tag"],
                    row["author"],
                    row["quote"],
                    row["scrape_timestamp"],
                    row["url"]
                ])