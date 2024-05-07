
# Compreensão de lista, também conhecida como list comprehension em inglês, é uma forma concisa e expressiva de criar listas em linguagens de programação como Python. Em vez de usar loops tradicionais para construir uma lista elemento por elemento, a compreensão de lista permite criar listas de forma mais compacta e legível.

'''* Forma básica
[empressão for intem in sequência]
lista = ['Robson.@gmail ', ' ,anA.@terra.com']
lista_final = [email.strip().replace(',','').lower() for email in lista]
print(lista_final)

numeros = [1, 2, 3, 4, 5]
quadrados = [num**2 for num in numeros]
print(quadrados)

numeros = [1, 2, 3, 4, 5]
quadrados = []
for num in numeros: quadrados.append(num ** 2)
print(quadrados)'''

# ---------

# *Adicionado Estrutura Condicional

# lista = ['Robson.@gmail ', ' ,anA.@terra.com']
# lista_final = [email.strip().replace(',','').lower() for email in lista]
# lista_gmail = [email.strip().replace(',','').lower() for email in lista if 'gmail' in email]
# print(f'Lista tratada: {lista_final}')
# print(f'Email com gmail:{lista_gmail}')

# ---------
# Multiplos de 4 e 5
multiplos = [numero for numero in range(0, 501)if numero % 4 == 0 if numero % 5 == 0]
print(multiplos)