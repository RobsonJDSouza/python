'''
Escreva um programa:
    Esreva o nome em maiúscula
    Escrava o nome em minúscula
    Conte o total de letras
    Conte o taotal de letras da primeira palavra


nome = str(input('Digite um nome: ')).strip()

print('Seu nome em maiúculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('O Nome possui {} letras'.format(len(nome) - nome.count(' ')))

nome_separado = nome.split()
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(nome_separado[0], len(nome_separado[0])))
'''

nome = str(input("Escreva um nome: ")).strip()

print(f"Seu nome em maiúsculo {nome.upper()}")
print(f"Seu nome em minúsculo {nome.lower()}")
print(f"Seu nome tem {len(nome)} letras")
print(f"O primeiro nome tem {nome.find(' ')} letras")

nome_s = nome.split()
print(f"O primeiro nome tem {len(nome_s[1])} letras")