import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url='https://fundamentus.com.br/fii_resultado.php', headers=headers)

