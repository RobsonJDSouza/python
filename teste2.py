from selenium import webdriver

import time

navegador = webdriver.Chrome()
navegador.get("https://finviz.com/futures.ashx")
navegador.maximize_window()
USD = navegador.find_element("class name", "USD")
USD.click()
time.sleep(10)