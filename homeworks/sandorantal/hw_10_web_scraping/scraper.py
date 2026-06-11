import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

print("Launch browser...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
all_quotes_data = []

try:
    base_url = "https://quotes.toscrape.com/"
    print("1. Loading homepage, collecting Top 10 members...")
    driver.get(base_url)
    time.sleep(2)

    tag_elements = driver.find_elements(By.CSS_SELECTOR, ".tag-item .tag")
    top_10_tags = [tag.text for tag in tag_elements][:10]
    print(f"-> Megtalált tagek: {top_10_tags}\n")

    for current_tag in top_10_tags:
        tag_url = f"{base_url}tag/{current_tag}/"
        driver.get(tag_url)
        time.sleep(1)
        
        page_number = 1
        while True:
            print(f"Scraping: Tag: [{current_tag}] -> {page_number}. oldal")
            quote_blocks = driver.find_elements(By.CSS_SELECTOR, ".quote")
            
            for block in quote_blocks:
                quote_text = block.find_element(By.CSS_SELECTOR, ".text").text
                author_text = block.find_element(By.CSS_SELECTOR, ".author").text
                
                all_quotes_data.append({
                    "tag": current_tag,
                    "author": author_text,
                    "quote": quote_text
                })
            
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
                next_button.click()
                page_number += 1
                time.sleep(1)
            except:
                print(f"-> There are no more pages for the tag '{current_tag}'.\n")
                break

finally:
    driver.quit()

if all_quotes_data:
    df = pd.DataFrame(all_quotes_data)
    df.to_csv("top_10_tags_quotes.csv", index=False, encoding="utf-8-sig")
    print(f"\nSuccessfully saved! The 'top_10_tags_quotes.csv' file is ready.")
    print(f"Total {len(df)} quotes downloaded.")
else:
    print("\nError: Failed to collect data.")