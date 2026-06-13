import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import quote_selectors as quo

class QuoteScraper:

    def __init__(self):
        self._cookies_accepted = False
        self.driver = None

    def initialize_webdriver(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    def get_urls_from_homepage(self, homepage_url: str):
        print(f"Top tags: {homepage_url}")
        
        if self.driver is None:
            self.initialize_webdriver()
            
        self.driver.get(homepage_url)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, quo.TOP_TAGS_XPATH))
        )
        
        tag_elements = self.driver.find_elements(By.XPATH, quo.TOP_TAGS_XPATH)
        
        urls = []
        for element in tag_elements:
            urls.append(element.get_attribute("href"))
            
        print(f"Total urls: {len(urls)}")
        return urls

    def accept_cookies(self, timeout=10):
        self._cookies_accepted = True

    def get_product_hierarchy(self):
        quote_elements = self.driver.find_elements(By.XPATH, value=quo.QUOTE_HIERARCHY_XPATH)
        
        page_data = []
        for block in quote_elements:
            quote_text = block.find_element(By.XPATH, value=quo.QUOTE_NAME_XPATH).text
            author_text = block.find_element(By.CLASS_NAME, value=quo.QUOTE_AUTHOR_CLASS).text
            
            page_data.append({
                "author": author_text,
                "quote": quote_text
            })
            
        return page_data

    def scrape_product_data(self, url):
        print(f"Scraping {url}")

        if self.driver is None:
            self.initialize_webdriver()

        self.driver.get(url)
        if not self._cookies_accepted:
            self.accept_cookies()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, quo.QUOTE_HIERARCHY_XPATH))
        )
        
        tag_name = url.split("/tag/")[-1].replace("/", "")
        
        raw_quotes = self.get_product_hierarchy()
        
        scraped_items = []
        for item in raw_quotes:
            scraped_items.append({
                "tag": tag_name,
                "author": item["author"],
                "quote": item["quote"]
            })

        return scraped_items
        
    @staticmethod
    def read_urls_from_file(file_name):
        urls = []
        with open(file_name, "r") as file:
            for line in file:
                url = line.strip()
                if url:
                    urls.append(url)
        return urls
    
    @staticmethod
    def write_urls_to_file(urls, file_name):
        with open(file_name, "w") as file:
            for url in urls:
                file.write(url + "\n")
        print(f"URLs has been written to {file_name}")

    @staticmethod
    def load_results_to_csv(data, filepath):
        final_list = []
        for sublist in data:
            if isinstance(sublist, list):
                final_list.extend(sublist)
            else:
                final_list.append(sublist)
            
        df = pd.DataFrame(final_list)
        df.to_csv(filepath, index=False, encoding='utf-8')