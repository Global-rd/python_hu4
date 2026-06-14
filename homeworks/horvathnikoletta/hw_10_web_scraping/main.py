import os
from quote_scraper import QuoteScraper
from selenium.common.exceptions import TimeoutException

def main():
    scraper = QuoteScraper()

    URLS_FILE_PATH = "homeworks/horvathnikoletta/hw_10_web_scraping/TOP10TAGS_urls.txt"
    RESULT_FILEPATH = "homeworks/horvathnikoletta/hw_10_web_scraping/scraped_results.csv"
   
    if os.path.exists(URLS_FILE_PATH):
        print("URL list already exists, reading from file...")
        urls = scraper.read_urls_from_file(URLS_FILE_PATH)
    else:
        print("No URL list yet, reading from sitemap..")

        urls = []
        urls = scraper.get_urls_from_homepage("https://quotes.toscrape.com/")
        scraper.write_urls_to_file(urls, URLS_FILE_PATH)

        scraper.write_urls_to_file(urls, URLS_FILE_PATH)
        print(f"Stored {len(urls)} in {URLS_FILE_PATH}")    
   
    print(urls[:10])
    
    scraper.initialize_webdriver()
    
    data = []
    for url in urls[:10]:
        product_data = scraper.scrape_product_data(url)
        data.append(product_data)
    
    scraper.load_results_to_csv(data, RESULT_FILEPATH)

if __name__ == "__main__":
    main()