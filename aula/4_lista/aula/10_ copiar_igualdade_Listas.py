# Copiar e "Igualdade" de Listas

### Estrutura:
'''
Quando fazemos:
lista2 = lista1
não estamos criando uma lista nova, mas estamos atribuindo outra variável à mesma lista.

- Se quisermos copiar lista devemos fazer
lista2 = lista1.copy()
ou entao
lista2 = lista1[:]
'''

lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista
lista[1] = 'iphone 11'
print(lista2)


# Agora copiando

lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista.copy()
lista[1] = 'iphone 11'
print(lista2)