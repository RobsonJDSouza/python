from random import randint 
from time import sleep

computador = randint(1, 5)

print("*" * 65)
print("Regra Básica. Jogador deve informar um número no range de 1 a 5")
print("*" * 65)

jogador = int(input("Digite o seu número jogador: "))
print("\n")
print("PROCESSANDO...")
sleep(3)

if jogador == computador:
    print("ACERTOU!! Você ganhou dessa vez!")
else:
    print("EROUUUUU!! Nunca mais irá ganhar!")