from scraper import QuoteScrapper

BASE_URL = "https://quotes.toscrape.com"
CSV_PATH = "quotes.csv"


def main():
    scraper = QuoteScrapper()
    scraper.initialize_webdriver()
    print("Top 10 tags...")
    tags = scraper.get_top_10_tags(BASE_URL)
    print(f"Top 10 tags: {tags}")

    all_data = []
    for tag in tags:
        print(f"Scrapping tag: {tag}")
        tag_data = scraper.scrape_tag_quotes(BASE_URL, tag)
        all_data.extend(tag_data)

    scraper.save_to_csv(all_data, CSV_PATH)
    print(f"Scraping finished. Save to {CSV_PATH}")


if __name__ == "__main__":
    main()
