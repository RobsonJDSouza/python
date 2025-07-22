from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Ajuste esse caminho para onde está o seu chromedriver
chromedriver_path = 'C:/caminho/para/chromedriver.exe'  # Windows
# chromedriver_path = '/usr/local/bin/chromedriver'      # Linux/Mac (exemplo)

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    url = 'https://www.investing.com/indices/us-30'
    driver.get(url)
    
    # Espera a página carregar JavaScript
    time.sleep(5)
    
    # Pega o preço atual pelo ID 'last_last'
    price_element = driver.find_element(By.ID, 'last_last')
    price = price_element.text
    
    print(f'Cotação atual do US 30: {price}')
    
finally:
    driver.quit()
