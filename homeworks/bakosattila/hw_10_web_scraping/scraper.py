from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

BASE_URL = "https://quotes.toscrape.com"


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def get_top_tags(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.tags-box span.tag-item a"))
    )
    tag_elements = driver.find_elements(By.CSS_SELECTOR, "div.tags-box span.tag-item a")
    return [el.text.strip() for el in tag_elements]


def scrape_quotes_for_tag(driver, tag):
    quotes = []
    page = 1

    while True:
        url = f"{BASE_URL}/tag/{tag}/page/{page}/"
        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.quote"))
            )
        except Exception:
            break

        quote_elements = driver.find_elements(By.CSS_SELECTOR, "div.quote")
        for elem in quote_elements:
            text = elem.find_element(By.CSS_SELECTOR, "span.text").text.strip()
            author = elem.find_element(By.CSS_SELECTOR, "small.author").text.strip()
            quotes.append({"tag": tag, "author": author, "quote": text})

        next_btn = driver.find_elements(By.CSS_SELECTOR, "li.next a")
        if not next_btn:
            break
        page += 1
        time.sleep(0.5)

    return quotes


def main():
    driver = get_driver()
    try:
        print("Collecting top 10 tags...")
        top_tags = get_top_tags(driver)
        print(f"Tags found: {top_tags}\n")

        all_quotes = []
        for tag in top_tags:
            print(f"Scraping tag: '{tag}'...")
            quotes = scrape_quotes_for_tag(driver, tag)
            print(f"  -> {len(quotes)} quotes collected")
            all_quotes.extend(quotes)

        df = pd.DataFrame(all_quotes, columns=["tag", "author", "quote"])
        output_file = "quotes.csv"
        df.to_csv(output_file, index=False, encoding="utf-8")
        print(f"\nDone! {len(df)} rows saved to '{output_file}'")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
