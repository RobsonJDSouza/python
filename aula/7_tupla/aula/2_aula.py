# # Criando uma tupla
# minha_tupla = (1, 2, 3, 4, 5)

# # Acessando elementos da tupla
# print(minha_tupla[0])  # Saída: 1

# # Tentativa de modificar um elemento da tupla (vai gerar um erro)
# # minha_tupla[0] = 10  # TypeError: 'tuple' object does not support item assignment

# # Concatenando tuplas
# outra_tupla = (6, 7, 8)
# nova_tupla = minha_tupla + outra_tupla
# print(nova_tupla)  # Saída: (1, 2, 3, 4, 5, 6, 7, 8)

# # Desempacotando uma tupla
# a, b, c = minha_tupla
# print(a, b, c)  # Saída: 1 2 3

# # unpacking
# vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')
# nome, data_contratacao, data_nascimento, salario, cargo = vendas
# print(salario)


'''- o enumerate que vínhamos usando até agora, na verdade, cria uma tupla para a gente. Vamos ver na prática:'''

vendas = [1000, 2000, 300, 300, 150]
funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']

for i, venda in enumerate(vendas):
        print(f'{funcionarios[i]} vendeu {venda} unidades')       