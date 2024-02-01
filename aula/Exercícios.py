
# Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
# nome = input(str('Digite o seu nome: '))
# nome_m = nome.upper()
# nome_t = nome_m[::-1]
# print(nome_t)

# Faça um programa que solicite o nome do usuário e imprima-o na vertical.
# nome = input(str('Digite o seu nome: '))
# for i in (nome):
#     print(i)

# Modifique o programa anterior de forma a mostrar o nome em formato de escada.
# nome = input(str('Digite o seu nome: '))
# nome_vazio = ''
# for i in nome:
#     nome_vazio += i
#     print(nome_vazio)

# Altere o programa anterior de modo que a escada seja invertida.
nome = input(str('Digite o seu nome: '))
nome1 = ''
nome2 = ''
for i in nome:
    nome1 += i
for letra in range(len(nome)):
    nome2 = nome1[0:len(nome) -letra:]
    print(nome2)

