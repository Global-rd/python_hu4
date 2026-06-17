import csv
from urllib.parse import quote
from anyio import Path
import selenium  #verzió lekéréshez csak teszt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#csak akiváncsiság kedvéért kiíratjuk a selenium verzióját
print("A használt Selenium verzió:", selenium.__version__)
# 1. Selenium WebDriver inicializálása (Chrome-hoz)
options = webdriver.ChromeOptions()
# Opcionális: Háttérben futás (headless mód), ha nem akarjuk, hogy felugorjon a böngészőablak:
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)


# Létrehozunk egy WebDriverWait objektumot, maximum 10 másodperces időkorláttal
wait = WebDriverWait(driver, 10)

base_url = "https://quotes.toscrape.com"
all_quotes_data = []

try:
    # 2. Első lépés: Látogassunk el a főoldalra a Top 10 tag összegyűjtéséhez
    print("Főoldal betöltése és a Top 10 tag megvárása...")

    driver.get(base_url)
    
    # A jobb oldalsávban lévő top 10 tag elemeinek megkeresése
    # Az oldalon ezek a 'tags-box' div-en belül találhatók meg, mint .tag osztályú linkek
    tag_elements = wait.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tags-box .tag"))
    )


    # Az első 10 tag nevének kinyerése
    top_10_tags = [tag.text.strip() for tag in tag_elements[:10]]
    print(f"Megtalált Top 10 tag: {top_10_tags}\n")
    
    # 3. Második lépés: Végigmegyünk a gyűjtött tag-eken és kezeljük a pagination-t
    for current_tag in top_10_tags:
        # URL kódolás biztonsági okokból (pl. ha szóköz vagy speciális karakter lenne a tag-ben)
        encoded_tag = quote(current_tag)
        tag_url = f"{base_url}/tag/{encoded_tag}/"
        
        print(f"--- '{current_tag}' tag feldolgozása kezdődik ---")
        driver.get(tag_url)
             
        has_next_page = True
        while has_next_page:
            print(f"Idézetek gyűjtése a következő URL-ről: {driver.current_url}")
            
            # Az oldalon található összes idézet blokk kijelölése
            quote_blocks = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".quote"))
            )


            for block in quote_blocks:
                # Szöveg kinyerése (levágjuk a weboldal által használt speciális idézőjeleket)
                raw_quote = block.find_element(By.CSS_SELECTOR, ".text").text.strip()
                if raw_quote.startswith('“') and raw_quote.endswith('”'):
                    raw_quote = raw_quote[1:-1]
                
                # Szerző kinyerése
                author = block.find_element(By.CSS_SELECTOR, ".author").text.strip()
                
                # Adat hozzáadása a listához
                all_quotes_data.append({
                    'tag': current_tag,
                    'author': author,
                    'quote': raw_quote
                })
        
            # Pagination kezelése explicit wait segítségével
            try:
                # Megpróbáljuk megvárni, hogy a Next gomb kattinthatóvá váljon (max 3 másodpercig, felesleges 10-et várni az utolsó oldalon)
                short_wait = WebDriverWait(driver, 3)
                next_button = short_wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pager .next a"))
                )
                next_button.click()
                print("Ugrás a következő oldalra...")
            except TimeoutException:
                # Ha 3 másodperc után sem jelenik meg a Next gomb, az azt jelenti, hogy az utolsó oldalon vagyunk
                print(f"Elértük az utolsó oldalt a(z) '{current_tag}' tag-nél.")
                has_next_page = False
                
#        print(f"--- '{current_tag}' kész. ---\n")
            
                
        print(f"--- '{current_tag}' tag összes oldala feldolgozva. ---\n")

finally:
    # A böngésző bezárása mindenképpen fusson le
    driver.quit()

# 4. Harmadik lépés: Az összegyűjtött adatok mentése CSV fájlba
file_path = Path("homeworks") / "szulyovszkypeter" / "hw_10_web_scraping"
csv_filename = "top_10_tags_quotes.csv"


# utf-8-sig kódolást használunk, hogy az Excel is közvetlenül, karakterhelyesen nyissa meg
with open(file_path / csv_filename, mode='w', encoding='utf-8-sig', newline='') as csv_file:
    fieldnames = ['tag', 'author', 'quote']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Fejléc kiírása
    writer.writeheader()
    
    # Adatsorok kiírása
    for row in all_quotes_data:
        writer.writerow(row)

print(f"Sikeres futás! Összesen {len(all_quotes_data)} idézet lett elmentve a '{csv_filename}' fájlba.")