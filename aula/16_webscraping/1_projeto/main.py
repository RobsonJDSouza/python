import requests
from bs4 import BeautifulSoup
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') #passamos uma categoria 

def trata_porcentagem(porcentagem_str):
        # '7,04%'
        # '7,04'
    return locale.atof(porcentagem_str.split('%')[0]) 

def trata_decimal(decimal_str):
    return locale.atof(decimal_str)


headers = {'User-Agent': 'Mozilla/5.0'} #emula um navegador
response = requests.get(url='https://fundamentus.com.br/fii_resultado.php', headers=headers) #emular a busca -
soup = BeautifulSoup(response.text, 'html.parser')
linhas = soup.find(id='tabelaResultado').find('tbody').find_all('tr')
for linha in linhas:
    dados_fundo = linha.find_all('td')
    # print(dados_fundo[1].text)
    # print(
    # f"[{dados_fundo[0].text}]\n"
    # f"Cotação: {dados_fundo[2].text}\n"
    # f"Setor: {dados_fundo[1].text}\n"
    # f"DY: {dados_fundo[4].text}\n"
    # f"P/VP: {dados_fundo[5].text}\n"
    # )

    papel = dados_fundo[1].text
    segmento = dados_fundo[2].text
    cotacao = trata_porcentagem(dados_fundo[3].text)
    ffo = trata_porcentagem(dados_fundo[4].text)
    dividendo = trata_porcentagem(dados_fundo[5].text)
    pvp = trata_decimal(dados_fundo[6].text)
    liquidez = trata_decimal(dados_fundo[7].text)
    qtdimoveis = dados_fundo[8].text
    precom2 = trata_decimal(dados_fundo[9].text)
    aluguelm2 = trata_decimal(dados_fundo[10].text)
    rate = trata_porcentagem(dados_fundo[11].text)
    vanciamedia = trata_porcentagem(dados_fundo[12].text)

    pass