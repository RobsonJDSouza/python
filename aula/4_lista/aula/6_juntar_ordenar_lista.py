# Juntar Listas, Ordenar e Cuidados Especiais

'''
- lista1.extend(lista2)
- lista_nova = lista1 + lista2

Obs: o Método .append não junta listas, mas adiciona um valor no final da lista

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
novos_produtos = ['iphone 12', 'ioculos']

### Cuidado:

- [1] + [2] não é a mesma coisa que 1 + 2, então cuidado sempre com o formato dos valores na hora de fazer operações.
'''

vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
vendas_iphonex = [15000]
vendas_iphone11 = [20000]

vendas_iphonex.extend(vendas_iphone11)
print(vendas_iphonex)

vendas_iphonex.extend(vendas)
print(vendas_iphonex)


"""
### Ordenar listas
lista.sort()
"""
vendas_iphonex.sort()
print(vendas_iphonex)

vendas_iphonex.sort(reverse= True)
print(vendas_iphonex)


