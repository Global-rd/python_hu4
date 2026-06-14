from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv


class QuoteScraper:
    BASE_URL = "https://quotes.toscrape.com"
    TAG_URL_TEMPLATE = BASE_URL + "/tag/{tag}/page/{page}/"

    def __init__(self, headless: bool = True):
        options = Options()
        if headless:
            options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def close(self):
        if self.driver:
            self.driver.quit()

    def get_top_10_tags(self):
        self.driver.get(self.BASE_URL)
        time.sleep(1)

        tag_elements = self.driver.find_elements(By.CSS_SELECTOR, ".tag-item a")
        tags = [t.text.strip() for t in tag_elements][:10]
        return tags

    def scrape_quotes_for_tag(self, tag: str):
        quotes_data = []
        page = 1

        while True:
            url = self.TAG_URL_TEMPLATE.format(tag=tag, page=page)
            self.driver.get(url)
            time.sleep(1)

            quotes = self.driver.find_elements(By.CSS_SELECTOR, ".quote")
            if not quotes:
                break

            for q in quotes:
                text = q.find_element(By.CSS_SELECTOR, ".text").text.strip()
                author = q.find_element(By.CSS_SELECTOR, ".author").text.strip()

                quotes_data.append({"tag": tag, "author": author, "quote": text})

            page += 1

        return quotes_data

    def scrape_all_top_tags(self):
        all_quotes = []
        top_tags = self.get_top_10_tags()

        for tag in top_tags:
            print(f"Actual scraping tag: {tag}")
            tag_quotes = self.scrape_quotes_for_tag(tag)
            all_quotes.extend(tag_quotes)

        return all_quotes

    def save_to_csv(self, data, filename: str = "quotes_top10_tags_with_oop.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["tag", "author", "quote"])
            writer.writeheader()
            writer.writerows(data)
        print("The task is completed!")
        print(f"I've saved the requested data here: {filename}")


def main():
    scraper = QuoteScraper(headless=True)
    try:
        all_quotes = scraper.scrape_all_top_tags()
        scraper.save_to_csv(all_quotes)
    finally:
        scraper.close()


if __name__ == "__main__":
    main()
