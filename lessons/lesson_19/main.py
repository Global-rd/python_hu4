import os
from auchan_scraper import AuchanScraper


def main():
    scraper = AuchanScraper()

    URLS_FILE_PATH="lessons/lesson_19/all_auchan_urls.txt"
    RESULT_FILEPATH="lessons/lesson_19/scraped_results.csv"

    if os.path.exists(URLS_FILE_PATH):
        print("URL list already exists, reading from file...")
        urls = scraper.read_urls_from_file(URLS_FILE_PATH)
    else:
        print("No URL list yet, reading from sitemap..")

        urls = []
        for i in range(0,3):
            url_sublist = scraper.get_urls_from_sitemap(f"https://auchan.hu/sitemaps/product-sitemap-{i}.xml")
            urls.extend(url_sublist)

        scraper.write_urls_to_file(urls, URLS_FILE_PATH)
        print(f"Stored {len(urls)} in {URLS_FILE_PATH}")        

    print(urls[:5])
    scraper.initialize_webdriver()
    data = []
    for url in urls[:5]:
        product_data = scraper.scrape_product_data(url)
        data.append(product_data)
    
    scraper.load_results_to_csv(data, RESULT_FILEPATH)


if __name__ == "__main__":
    main()