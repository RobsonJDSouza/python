'''- o enumerate que vínhamos usando até agora, na verdade, cria uma tupla para a gente. Vamos ver na prática:'''

vendas = [1000, 2000, 300, 300, 150]
funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']

for i, venda in enumerate(vendas):
        print(f'{funcionarios[i]} vendeu {venda} unidades')       