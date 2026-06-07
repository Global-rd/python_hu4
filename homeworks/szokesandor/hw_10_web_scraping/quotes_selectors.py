"""
A scraper-elendő oldal fő URL-jét, és az oldal elemeinek eléréséhez szükséges SCC selector-okat tartalmazza

"""

QUOTES_URL = "https://quotes.toscrape.com/"

TOP_10_TAG_CSS_SELECTOR = ".col-md-4.tags-box .tag"
QUOTE_LIST_CSS_SELECTOR = ".col-md-8 .quote"
QUOTE_TEXT_CSS_SELECTOR = ".text"
QUOTE_AUTHOR_CSS_SELECTOR = ".author"
QUOTE_NEXT_CSS_SELECTOR = ".col-md-8 .pager .next a"