"""
A https://quotes.toscrape.com/ oldalról legyűjti a "Top Ten tags"

"""

import csv
import time
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://quotes.toscrape.com/"


DELAY = 0.5


def make_driver(headless: bool = True) -> webdriver.Chrome:
    """Létrehoz egy Chrome WebDriver-t."""
    options = Options()
    if headless:
      
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)


def get_top_ten_tags(driver) -> list[str]:
    """A kezdőlapról összegyűjti a "Top Ten tags" lista tag-neveit.

    Tipp a feladatból: először a tag-neveket gyűjtjük össze, hogy aztán
    ezekből tudjuk összerakni az egyes tag-oldalak URL-jét.
    """
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.tags-box"))
    )
    
    tag_links = driver.find_elements(
        By.CSS_SELECTOR, "div.tags-box span.tag-item a.tag"
    )
    tags = [link.text.strip() for link in tag_links]
    return tags


def scrape_tag(driver, tag: str) -> list[dict]:
    """Egy adott tag ÖSSZES oldaláról legyűjti az idézeteket."""
    rows = []
   
    url = urljoin(BASE_URL, f"tag/{tag}/")

    while url:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.quote"))
        )

        
        quote_blocks = driver.find_elements(By.CSS_SELECTOR, "div.quote")
        for block in quote_blocks:
            text = block.find_element(By.CSS_SELECTOR, "span.text").text
            author = block.find_element(By.CSS_SELECTOR, "small.author").text
           
            rows.append({"tag": tag, "author": author, "quote": text})

        next_buttons = driver.find_elements(By.CSS_SELECTOR, "li.next a")
        url = next_buttons[0].get_attribute("href") if next_buttons else None

        time.sleep(DELAY)

    return rows


def main() -> None:
    driver = make_driver(headless=True)
    all_rows: list[dict] = []

    try:
        tags = get_top_ten_tags(driver)
        print(f"Top 10 tag: {tags}")

        for tag in tags:
            tag_rows = scrape_tag(driver, tag)
            print(f"  {tag:<15} -> {len(tag_rows)} idézet")
            all_rows.extend(tag_rows)
    finally:
       
        driver.quit()

 
    with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["tag", "author", "quote"])
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\nKész! Összesen {len(all_rows)} sor mentve a quotes.csv fájlba.")


if __name__ == "__main__":
    main()
