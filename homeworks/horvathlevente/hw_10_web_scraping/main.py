from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

BASE_URL = "https://quotes.toscrape.com"

wait = WebDriverWait(driver, 10)

# 1) Top 10 tag összegyűjtése
driver.get(BASE_URL)

wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tag-item a")))
tag_elements = driver.find_elements(By.CSS_SELECTOR, ".tag-item a")
top_10_tags = [tag.text.strip() for tag in tag_elements[:10]]

print("Top 10 tag:", top_10_tags)

data = []

# 2) Idézetek gyűjtése minden taghez
for tag in top_10_tags:
    print(f"Scraping tag: {tag}")
    page = 1

    while True:
        url = f"{BASE_URL}/tag/{tag}/page/{page}/"
        driver.get(url)

        # Ha nincs quote elem → vége
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".quote")))
        except:
            break

        quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")

        for q in quotes:
            quote_text = q.find_element(By.CSS_SELECTOR, ".text").text.strip()
            author = q.find_element(By.CSS_SELECTOR, ".author").text.strip()

            data.append({
                "tag": tag,
                "author": author,
                "quote": quote_text
            })

        page += 1

# 3) CSV mentése
df = pd.DataFrame(data)
df.to_csv("quotes_by_top10_tags.csv", index=False, encoding="utf-8")

driver.quit()

print("Kész! A CSV fájl neve: quotes_by_top10_tags.csv")