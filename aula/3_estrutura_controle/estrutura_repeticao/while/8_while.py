from random import randint

# capacidade_maxima = 100
# balde = 0

# while balde <= capacidade_maxima:
#     volume__copo = randint(50, 100)
#     print(f'Copo enchido: {volume__copo}mls')
#     balde += volume__copo
#     print(f'Volume do balde: {balde}mls')


# Exemplo 2
# compra = []
# print('Vocẽ pode parar a compra digitando Não')
# venda = input('Produto: ').lower()

# while venda != 'não':
#     compra.append(venda)
#     venda = input('Produto ').lower()
#     if venda == 'nao':
#         print('\O/\O/\O/ ATENÇÃO \O/\O/\O/ - Digite o não com acento!!!')

# print(f'Lita de produtos {compra}')


# Exemplo 3

# vendas = [20, 30, 9, 11]
# nome = ['Robson', 'Ana', 'Sofia', 'Iris']
# meta = 10
# i = 0

# 1ª Possibilidade
# while vendas[i] > meta:
#     print(f'Vendedor(a) {nome[i]} bateu a meta. Total de vendas: {vendas[i]}')
#     i += 1
#     if vendas[i] < meta:
#         print(f'Vendedor(a) {nome[i]} não bateu a meta. Total de venda: {vendas[i]}')

# 2ª Possibilidade
# while i < len(vendas):
#     if vendas[i] >= meta:
#         print(f'Vendedor(a) {nome[i]} bateu a meta. Total de vendas: {vendas[i]}')
#     else:
#         print(f'Vendedor(a) {nome[i]} não bateu a meta. Total de venda: {vendas[i]}')
#     i += 1


# Exemplo 4
# produtos = []
# quantidades = []

# while True: #loop infinito
#     produto = input('Produto: ')
#     if not produto:
#         break #Mas com uma condição que para o Looping.
#     quantidade = int(input('Quantidade '))
#     if not quantidade:
#         break
#     produtos.append(produto)
#     quantidades.append(quantidade)
#     print(f'Você comprou {quantidade} {produto}')

# print(f'{quantidades} {produtos}')


# Exemplo 5
# nota = []
# while True:
#     nota_valida = int(input('Passa uma nota de 0 a 10. '))
#     if nota_valida < 11:
#         nota.append(nota_valida)
#     else:
#         print('Nota invalida digitada')
#         break
# print(f'Suas notas digitadas foram {nota}')


# Exemplo 5
# """ Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""
# while True:
#     usuario = input('Nome de usuário: ')
#     senha = input('Qual a senha? ')
#     if usuario != senha:
#         break
#     print('Digite uma senha diferente do usuário')
# print(f'Seu nome de usuário {usuario} e senha é {senha}')



# Exemplo 6
"""Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""


# while True:
#     nome = input('Digite o nome: ')
#     idade = int(input('Digite a idade: '))
#     salario = int(input('Digite o salário: '))
#     sexo = input('\nSexo: \nF - Feminino \nM - Masculino')
#     estado = input('\nEstado Civil: \nS - Solteiro \nC - Casado \nV - Viuvo \nD - Divorciado')


nome = input('Digite o nome: ')

if len(nome) < 4:
    print(3)
else:
    print(nome)