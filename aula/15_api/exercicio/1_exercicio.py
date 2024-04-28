import requests
import json
import matplotlib.pyplot as plt

#Consultar a API 
site = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacao = site.json()
print(f"Cotação Dolar: {cotacao['USD']['bid']:.4}")
print(f"Cotação Euro: {cotacao['EUR']['bid']:.4}")
print(f"Cotação BTC: {cotacao['BTC']['bid']}")


#Consultar a API no período de 30 dias
response = requests.get('https://economia.awesomeapi.com.br/json/daily/USD/30')
cotacao_30d = response.json()
lista_cotacao = []
# lista_cotacao = [item['bid'] for item in cotacao_30d] # Feito pelo metodo de List comprehension
for item in cotacao_30d:
    if 'bid' in item:
        lista_cotacao.append(float(item['bid']))
print(lista_cotacao)


#Contação do dolar por período
cotacoes_usd = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/200?start_date=20240101&end_date=20240426')
cotacoes_usd_dic = cotacoes_usd.json()
lista_cotacoes_usd = [float(item['bid']) for item in cotacoes_usd_dic]
lista_cotacoes_usd.reverse()
print(lista_cotacoes_usd)
print(len(lista_cotacoes_usd))

plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_usd)
plt.show()
