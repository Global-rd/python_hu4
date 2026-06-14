"""
HW 10 – Web Scraping
URL: https://quotes.toscrape.com/
Feladat: a Top 10 tag mindegyikéhez le kell scrape-elni az összes hozzá tartozó
idézetet (pagination figyelembevételével), majd CSV-be menteni.

Oszlopok: tag | author | quote
"""

import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://quotes.toscrape.com"
OUTPUT_FILE = "quotes_top10_tags.csv"


def create_driver() -> webdriver.Chrome:
    """Headless Chrome driver létrehozása."""
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)


def get_top10_tags(driver: webdriver.Chrome) -> list[str]:
    """
    A főoldalról összegyűjti a Top 10 tag nevét.
    A jobb oldali sávban találhatók 'tag-item' CSS osztályú elemek.
    """
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.tags-box span.tag-item"))
    )
    tag_elements = driver.find_elements(By.CSS_SELECTOR, "div.tags-box span.tag-item a")
    tags = [el.text.strip() for el in tag_elements]
    print(f"Top 10 tag-ek: {tags}")
    return tags


def scrape_tag(driver: webdriver.Chrome, tag: str) -> list[dict]:
    """
    Egy adott tag összes idézetét összegyűjti az összes oldalon (pagination).
    URL struktúra: /tag/<tag_name>/page/<n>/
    """
    results = []
    page = 1

    while True:
        url = f"{BASE_URL}/tag/{tag}/page/{page}/"
        driver.get(url)
        time.sleep(0.5)  # udvarias szünet a szerver felé

        try:
            WebDriverWait(driver, 8).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.quote"))
            )
        except Exception:
            # Ha nincs quote ezen az oldalon, kilépünk
            break

        quotes = driver.find_elements(By.CSS_SELECTOR, "div.quote")

        if not quotes:
            break

        for q in quotes:
            text = q.find_element(By.CSS_SELECTOR, "span.text").text.strip()
            author = q.find_element(By.CSS_SELECTOR, "small.author").text.strip()
            results.append({
                "tag": tag,
                "author": author,
                "quote": text,
            })

        # Megnézzük, van-e "Next" gomb
        next_buttons = driver.find_elements(By.CSS_SELECTOR, "li.next a")
        if next_buttons:
            page += 1
        else:
            break

    print(f"  [{tag}] {len(results)} idézet összegyűjtve ({page} oldal)")
    return results


def save_to_csv(data: list[dict], filename: str) -> None:
    """Adatok mentése CSV fájlba."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["tag", "author", "quote"])
        writer.writeheader()
        writer.writerows(data)
    print(f"\nMentve: {filename} ({len(data)} sor)")


def main():
    driver = create_driver()

    try:
        print("1. lépés: Top 10 tag lekérése...")
        tags = get_top10_tags(driver)

        print("\n2. lépés: Idézetek scrape-elése tagonként...")
        all_quotes = []
        for tag in tags:
            tag_quotes = scrape_tag(driver, tag)
            all_quotes.extend(tag_quotes)

        print("\n3. lépés: CSV mentése...")
        save_to_csv(all_quotes, OUTPUT_FILE)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()