from urllib.parse import urljoin

import os
from dotenv import load_dotenv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


load_dotenv()
BASE_URL = os.environ.get("QUOTES_URL")

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1200,900")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def get_top_10_tags(driver):
    driver.get(BASE_URL)

    tag_elements = driver.find_elements(By.CSS_SELECTOR, ".tag-item a.tag")
    tags = [tag.text.strip() for tag in tag_elements]

    return tags


def scrape_quotes_for_tag(driver, tag):

    results = []

    url = urljoin(BASE_URL, f"tag/{tag}/page/1/")

    while True:
        driver.get(url)

        quote_blocks = driver.find_elements(By.CSS_SELECTOR, ".quote")

        for block in quote_blocks:
            quote_text = block.find_element(By.CSS_SELECTOR, ".text").text.strip()
            author = block.find_element(By.CSS_SELECTOR, ".author").text.strip()

            results.append({
                "tag": tag,
                "author": author,
                "quote": quote_text
            })

        next_buttons = driver.find_elements(By.CSS_SELECTOR, "li.next a")

        if not next_buttons:
            break

        next_href = next_buttons[0].get_attribute("href")
        url = next_href

    return results
