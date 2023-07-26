'''
Escreva um programa
  Encontre o seno
  Encontre o cosseno
'''
from math import sin, cos, tan

angulo = float(input('Angulo: '))

print(f"O Seno de {angulo} é: {sin(angulo):.2f}º\nO Coseno do {angulo} é: {cos(angulo):.2f}º\nA Tangente do {angulo} é: {tan(angulo):.2f}º")