"""
A feladat érdemi részét végrehajtó QuotesScraper class

"""

from datetime import datetime as dt
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

import quotes_selectors as s

class QuotesScraper:
    
    def __init__(self):
        """
        Objektum init, amely egyúttal a webdriver-t is inicializálja
        """
        options = Options()
        options.add_argument("--headless=new") # A böngésző nem nyílik meg a scraping folyamat alatt
        self.driver = webdriver.Chrome(options=options)

    def get_elements_by_css(self, css_selector, wait_to_load=True) -> list[WebElement]:
        """
        Megkeresi az adott CSS selector szerinti elemeket, és visszaadja a keresési eredményeket tartalmazó listát
        """
        if wait_to_load: # Paraméterként megadható, hogy várakozzon-e amíg a kersett elemek betöltődnek. Alapértelmezetten ez True, de szükség szerint a várakozás kikapcsolható.
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector)))
        elements = self.driver.find_elements(By.CSS_SELECTOR, css_selector)
        return elements

    def scrape_top10_urls(self) -> list[dict]:
        """
        A fő oldalon megkeresi a top 10 tag URL-jét, és egy listában, a tag megnevezésével együtt visszaadja azokat.
        """
        self.driver.get(s.QUOTES_URL)
        tag_elements = self.get_elements_by_css(s.TOP_10_TAG_CSS_SELECTOR)
        top10_list = []
        for element in tag_elements:
            top10_list.append({"name": element.text.strip(),
                               "url" : element.get_attribute("href")})
        return top10_list
    
    def scrape_a_quotes_page(self, tag:str) -> list[dict]:
        """
        Scrape-eli az aktuális oldalt. Végiglépked az oldalon található szövegdobozokon, és kiolvassa az idézet szövegét és szerzőjét.
        Annyi idézetet olvas ki, ahány szövegdoboz az oldalon megjelenik. A beolvasott idézetek száma nincs megkötve.
        A függvény mindig az aktuális oldalt dolgozza fel. A feldolgozandó oldal megnyitásáról a függvény meghívása előtt kell gondoskodni.
        """
        quote_boxes = self.get_elements_by_css(s.QUOTE_LIST_CSS_SELECTOR)  # Beolvassa az oldalon lévő összes szövegdobozt
        quote_list = []
        for quote_box in quote_boxes:
            quote_text = quote_box.find_element(By.CSS_SELECTOR, s.QUOTE_TEXT_CSS_SELECTOR)     # Szövegdobozon belül megkeresi az idézet szövegét
            quote_author = quote_box.find_element(By.CSS_SELECTOR, s.QUOTE_AUTHOR_CSS_SELECTOR) # Megkeresi az idézet szerzőjét
            # A kinyert adatok írása egy dictionary-ba és hozzáfűzése a találati listához
            quote_list.append({"tag"      : tag,
                               "author"   : quote_author.text.strip(),
                               "quote"    : quote_text.text.strip(),
                               "timestamp": dt.now().strftime("%Y-%m-%d %H:%M:%S")
                            })
        return quote_list
    
    def get_next_url(self) -> str | None:
        """
        Az aktuális oldalon megkeresi a "Next" gombot (ha van) és visszaadja az ahhoz tartozó URL-t. Ez lesz a következó oldal, amit fel kell dolgozni.
        """
        next_link = self.get_elements_by_css(s.QUOTE_NEXT_CSS_SELECTOR, wait_to_load=False) # A "next" selector-hoz tartozó találatok kigyűjése
        if len(next_link) == 0: # Ha nincs találat, akkor nincs az oldalon next gomb
            return None
        else:
            url = next_link[0].get_attribute("href")  # Ha van találat, akkor visszaadjuk a "href" attributumban lévő URL-t
            return url

    def scrape_quotes(self, filepath: str):
        """
        Kiolvassa a top 10 tag szerinti URL-eket, végiglépked az URL-eken és azok folytató oldalain, közben egyenként meghívja az aktuális oldalt feldolgozó
        scrape_a_quotes_page függvényt.
        Az eredményeket CSV fájlba gyűjti, amelynek elérési útvonalát paraméterként kell megadni.
        """
        new_file = True # Logikai változót használunk annak eldöntéséhez, hogy kell-e új fájlt létrehozni vagy a meglévőt kell folytatni.
        top10_list = self.scrape_top10_urls() # Beolvassuk a top 10 URL -t

        for index, tag in enumerate(top10_list, start=1):
            print(f'{index}. scraping "{tag["name"]}" from {tag["url"]}') # Kiírjuk, hol tart a folyamat.
            self.driver.get(tag["url"]) # Megnyitjuk az adot tag első oldalát
            while True: # A ciklus addig fut, amíg van az oldalon next gomb
                quote_list = self.scrape_a_quotes_page(tag["name"]) # Feldolgozzuk a megnyitott oldalt
                self.save_to_csv(quote_list, filepath, new_file) # Az eredményeket CSV fájlba mentjük
                new_file = False  # A változó az első mentés után végig False marad
                next_url = self.get_next_url() # Megnézzük van-e az oldalon next gomb? Ha igen, akkor függvény beolvassa az ahhoz tartozó URL-t
                if next_url:
                    self.driver.get(next_url) # Ha kaptunk vissza URL-t (vagyis van next gomb) akkor megnyitjuk az oldalt, amire a next mutat
                else:
                    break # Ha nincs következő URL, akkor az adott tag-hez tartozó ősszes idézetet kinyertük. Kilépünk a belső ciklusból, és lépünk a következő tag-re

        # Ha minden tag-en végighaladtunk, akkor elkészült a feladat. Ezt egy üzenet jelzi:
        print(f"\nAll quotes successfully fetched and saved to {filepath}\n")

    @staticmethod
    def save_to_csv(data: list[dict], filepath: str, new_file: bool):
        """
        A függvény a kinyert adatokat CSV fájlba menti. A new_file paraméter függvényében új fájlt hoz létre vagy a már megkezdett fájlt folytatja
        """
        df = pd.DataFrame(data) # A CSV készítéséhez Pandas DataFrame-et használunk
        if new_file:
            df.to_csv(filepath, mode="w", header=True, index=False, encoding="utf-8-sig") # Új fájl jön létre, amit CSV fejléccel kezd.
        else:    
            df.to_csv(filepath, mode="a", header=False, index=False, encoding="utf-8-sig") # A meglévő fájlt folytatja. CSV fejlécet ilyenkor nem kell a fájlba írni.
