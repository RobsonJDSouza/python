# elif

'''
E se temos mais do que um caso de sim e não?
E se tivermos 3 casos?
Usamos o elif da seguinte forma:

if condição:
    o que fazer se a condição 1 for verdadeira
elif condição_2:
    o que fazer se a condição 1 for falsa e a condição 2 for verdadeira
else:
    o que fazer se a condição 1 e a condição 2 forem falsas
'''

### Exemplo:
'''
Vamos criar um programa para analisar o bônus dos funcionários de uma empresa (pode parecer "simples", mas uma empresa como a Amazon tem 900.000 funcionários)
Para os cargos de vendedores, a regra do bônus é de acordo com a meta de vendas da pessoa:
Se ela vendeu abaixo da meta dela, ela não ganha bônus.
Se ela vendeu acima da meta dela, ela ganha como bônus 3% do valor que ela vendeu.
Se ela vendeu mais do que o dobro da meta dela, ela ganha como bônus 7% do valor que ela vendeu.
Vamos criar um programa para avaliar uma pessoa que tinha como meta de vendas 20.000 reais e calcular o bônus dela de acordo com o valor de vendas que ela tiver.'''

meta = 20000
vendas = 15000

if vendas < meta:
    print('Não ganhou bônus')
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print(f'Ganhou {bonus} de bônus')
else:
    bonus = 0.03 * vendas
    print(f'Ganhou {bonus} de bônus')