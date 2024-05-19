## 1. Faturamento do Melhor e do Pior Mês do Ano

'''
Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?'''

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)
lista_tupla = zip(meses, vendas_1sem)
vendas_ano = dict(lista_tupla)

melhor_venda = 0
melhor_mes = ''

for mes in vendas_ano:
    if vendas_ano[mes] > melhor_venda:
        melhor_venda = vendas_ano[mes]
        melhor_mes = mes

print(f"O valor de vendas do melhor mês do ano ({melhor_mes}) foi: {melhor_venda}")

pior_venda = float('inf')  # Inicializando com infinito positivo
pior_mes = ''

for mes in vendas_ano:
    if vendas_ano[mes] < pior_venda:
        pior_venda = vendas_ano[mes]
        pior_mes = mes

print(f"O valor de vendas do pior mês do ano ({pior_mes}) foi: {pior_venda}")