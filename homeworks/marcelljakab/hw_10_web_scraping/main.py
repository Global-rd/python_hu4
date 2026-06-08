"""
main.py
-------
A scraper futtatása: top 10 tag összegyűjtése, mindegyikhez az összes idézet
lescrape-elése, majd mentés egy quotes.csv fájlba (tag, author, quote oszlopok).
"""

import pandas as pd

from scraper import QuotesScraper


def main():
    scraper = QuotesScraper()
    scraper.initialize_webdriver()

    try:
        # 1) Összegyűjtjük a top 10 tag nevét.
        top_tags = scraper.get_top_tags()
        print("Top 10 tag:", top_tags)

        # 2) Tag-enként lescrape-eljük az összes idézetet (lapozással).
        all_data = []
        for tag in top_tags:
            print(f"Scraping tag: {tag} ...")
            all_data.extend(scraper.scrape_tag(tag))

        # 3) Mentés CSV-be (tag, author, quote sorrendben, ékezetes karakterekhez utf-8).
        df = pd.DataFrame(all_data, columns=["tag", "author", "quote"])
        df.to_csv("quotes.csv", index=False, encoding="utf-8")
        print(f"Kész! {len(df)} idézet elmentve a quotes.csv fájlba.")
    finally:
        # Akkor is bezárjuk a böngészőt, ha közben hiba történt.
        scraper.quit()


if __name__ == "__main__":
    main()