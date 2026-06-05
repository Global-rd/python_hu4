# 10. házi feladat: Selenium web scraping

Selenium alapú scraper a https://quotes.toscrape.com/ oldalhoz.
Az alkalmazás először összegyűjti a főoldalon látható Top Ten tageket,
majd minden tag saját oldalán végigmegy a lapozáson, és CSV-be menti az
idézeteket.

## Az alkalmazás futtatása

```bash
cd homeworks/budaikrisztian/hw_10_web_scraping
pip install -r requirements.txt
PYTHONPATH=src python -m quotes_scraper.main
```

Opcionális helyi konfiguráció:

```bash
cp .env-example .env
```

Elérhető `.env` értékek:

```env
OUTPUT_PATH=output/quotes.csv
HEADLESS=true
MAX_WORKERS=3
```

A `MAX_WORKERS` adja meg, hány tag oldal fusson párhuzamosan. Az `1` érték
szekvenciális scrapinget használ worker szálak nélkül. Nagyobb érték gyorsabb
lehet, de több ChromeDriver példányt indít, ezért több CPU-t és memóriát
használ.

A scraper Chrome böngészőt használ headless módban. Selenium Manager
automatikusan megpróbálja előkészíteni a megfelelő ChromeDriver verziót.
Ha Linuxon a ChromeDriver hiányzó `libnss3` vagy `libnspr4` könyvtárra
panaszkodik, telepítsd ezeket a rendszerfüggőségeket:

```bash
sudo apt-get install libnss3 libnspr4
```

## Kimenet

A futtatás eredménye:

```text
output/quotes_YYYY-MM-DD_HH-MM-SS.csv
```

A fájlnévben lévő időbélyeg mutatja, mikor lett mentve a CSV.

A CSV oszlopai:

```text
tag,author,quote
```

A `tag` oszlop mindig az eredeti Top Ten tag nevét tartalmazza, amelynek az
oldaláról az idézet jött, nem az idézethez kapcsolódó összes taget.

## Ellenőrzés

```bash
cd ../../..
.venv/bin/ruff check homeworks/budaikrisztian/hw_10_web_scraping
.venv/bin/mypy homeworks/budaikrisztian/hw_10_web_scraping/src
```
