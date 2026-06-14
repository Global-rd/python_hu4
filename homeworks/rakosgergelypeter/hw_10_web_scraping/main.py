import pandas as pd
from selenium import webdriver
from scraper import (
    create_driver,
    get_top_10_tags,
    scrape_quotes_for_tag
)
def main():
    driver = create_driver()

    try:
        all_results = []

        top_10_tags = get_top_10_tags(driver)
        print("Top 10 tag:", top_10_tags)

        for tag in top_10_tags:
            print(f"Scraping tag: {tag}")
            tag_results = scrape_quotes_for_tag(driver, tag)
            all_results.extend(tag_results)

        df = pd.DataFrame(all_results, columns=["tag", "author", "quote"])
        df.to_csv("quotes_top_10_tags.csv", index=False, encoding="utf-8-sig")

        print("Kész! A fájl neve: quotes_top_10_tags.csv")
        print(f"Lescrape-elt sorok száma: {len(df)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
