
# Escreva um programa que sorteie um nome na lista aleatório

from random import choice
'''
lista = []
a = input("Digite o primeiro nome:")
b = input("Digite o segundo nome:")
c = input("Digite o terceiro nome:")

lista.append(a)
lista.append(b)
lista.append(c)

print(f"Os nomes digitados foram: {lista}")
print(choice(lista))
'''
lista = []
quantidade_nome = int(input("Digite a quantidade de nome que a lista deve conter: "))
while len(lista) < quantidade_nome:
    a = input()
    lista.append(a)
    if quantidade_nome is quantidade_nome:
      print("Digite mais um nome")
    else:
      print()

print(f"Os nomes da lista são: {lista}")
print(f"O nome sorteado: {choice(lista)}")


