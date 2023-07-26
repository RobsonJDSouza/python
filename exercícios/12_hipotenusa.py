'''
Escreva um programa
  Encontre o cateto oposto
  Encontre o cateto adjacente
'''
from math import hypot

catO = float(input('Digite o cateto oposto: '))
catA = float(input('Digite o cateto adjacente: '))

hipot = hypot(catO, catA)

print(hipot)

#Da bibliotéca math, importei o objeto hypot "Hipotenusa"

from math import hypot, pow

cateto_oposto = float(input("Digite o Cateto Oposto: "))
cateto_adjacente = float(input("Digite o Cateto Adjacente: "))

# sem usar o módulo math
hip = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2)

print(f"1º caso. Sem usar o módulo math.\nHipotenusa: {hip:.3f}\n") 
print(f"2º caso. Com o módulo math.\nHipotenusa: {hypot(cateto_adjacente, cateto_oposto):.3f}"