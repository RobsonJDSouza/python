import string
import random

tamanho_senha = int(input('Qual o tamanha da senha: '))

senha = []
for i in range(0, tamanho_senha):
    senha.append(random.choice(string.ascii_letters))
print("".join(senha))

                
