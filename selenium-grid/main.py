from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import time

# URL dari Selenium Hub
hub_url = "http://localhost:4444/wd/hub"

#Inisializise webdriver
def init_driver(node):
    options = Options()
    # options.add_argument("--start-maximized")
    options.add_argument("--headless")
    options.set_capability("se:nodeLabels", ["firefox", f"{node}"])

    driver = webdriver.Remote(command_executor=hub_url,options=options)
    driver.maximize_window()
    return driver

def scraping(node):
    # Inisialisasi driver untuk node1
    driver = init_driver(f"{node}")
    driver.get("https://quotes.toscrape.com")
    time.sleep(2)

    # Ambil semua elemen quote
    quotes = driver.find_elements(By.CLASS_NAME, "text")

    time.sleep(20)
    # Cetak hasil
    for i, quote in enumerate(quotes, start=1):
        print(f"{i}. {quote.text}")

    # Tutup browser
    driver.quit()

if __name__ == "__main__":
    nodes = ["node1", "node2", "node3", "node4"]
    with ThreadPoolExecutor(max_workers=len(nodes)) as executor:
        executor.map(scraping, nodes)