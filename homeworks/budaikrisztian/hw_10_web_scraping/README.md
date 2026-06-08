# Homework 10: Selenium web scraping

Selenium scraper for https://quotes.toscrape.com/.
The app first reads the Top Ten tags from the home page, then visits each tag
page, follows pagination, and writes the scraped quotes to CSV.

## Run

```bash
cd homeworks/budaikrisztian/hw_10_web_scraping
pip install -r requirements.txt
PYTHONPATH=src python -m quotes_scraper.main
```

Optional local configuration:

```bash
cp .env-example .env
```

Available `.env` values:

```env
OUTPUT_PATH=output/quotes.csv
HEADLESS=true
MAX_WORKERS=3
```

`MAX_WORKERS` controls how many tag pages are scraped in parallel. Use `1` for
sequential scraping without worker threads. Higher values can be faster, but
they start more ChromeDriver instances and use more CPU and memory.

The scraper uses Chrome in headless mode. Selenium Manager will try to prepare
the matching ChromeDriver automatically.
If ChromeDriver reports missing `libnss3` or `libnspr4` libraries on Linux,
install these system dependencies:

```bash
sudo apt-get install libnss3 libnspr4
```

## Output

The generated file is:

```text
output/quotes_YYYY-MM-DD_HH-MM-SS.csv
```

The timestamp in the file name shows when the CSV was saved.

The CSV columns are:

```text
tag,author,quote
```

The `tag` column contains the original Top Ten tag being scraped, not the
related tags listed on the quote itself.
