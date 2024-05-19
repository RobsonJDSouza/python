## 1. Faturamento do Melhor e do Pior Mês do Ano

'''
Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?'''

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)
maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)
posição_maior_valor = vendas_1sem.index(maior_valor)
posição_menor_valor = vendas_1sem.index(menor_valor)
mes_maior_valor = meses[10].capitalize()
mes_menor_valor = meses[11].capitalize()

print(f'O mês que mais faturou foi {mes_maior_valor} no valor de R${maior_valor}')
print(f'O mês que menos faturou foi {mes_menor_valor} no valor de R${menor_valor}')


'''
Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.
'''
faturamento_total = sum(vendas_1sem)
print(f'Faturamento Total: R${faturamento_total}')


'''Crie uma lista com o top 3 valores de vendas do ano.'''

vendas_1sem.sort(reverse= True)
print(f'Os 3 maiores valores foram: {vendas_1sem[:3]}')