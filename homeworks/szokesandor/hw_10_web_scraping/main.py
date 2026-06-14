"""
Az app a quotes.toscrape.com oldalról Selenium segítségével scrape-eli a top 10 tag összes idézetét, és
a végeredményt csv fájlba menti

"""

from pathlib import Path
from datetime import datetime as dt
from quotes_scraper import QuotesScraper

def main():
    file_path = Path("homeworks") / "szokesandor" / "hw_10_web_scraping" / f"quotes_{dt.now().strftime('%Y%m%d')}.csv" # Minden nap külön fájl készül az aznapi eredményről.
    scraper = QuotesScraper()
    scraper.scrape_quotes(file_path)

if __name__ == "__main__":
    main()
