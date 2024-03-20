import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url='https://fundamentus.com.br/fii_resultado.php', headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
linhas = soup.find(id='tabelaResultado').find('tbody').find_all('tr')
for linha in linhas:
    dados_fundo = linha.find_all('td')
    # print(dados_fundo[1].text)
    print(
    f"[{dados_fundo[0].text}]\n"
    f"Cotação: {dados_fundo[2].text}\n"
    f"Setor: {dados_fundo[1].text}\n"
    f"DY: {dados_fundo[4].text}\n"
    f"P/VP: {dados_fundo[5].text}\n"
    )