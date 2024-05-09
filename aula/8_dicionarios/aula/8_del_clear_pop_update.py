lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}

# - Modificar itens:

# dicionario[chave] = valor

'''Da mesma forma que adicionamos 1 valor, caso essa chave já exista o item é apenas modificado.
Vamos modificar o lucro de fevereiro:<br>
(Lembrando: caso o item não exista, ele vai criar o item no dicionário)'''

lucro_1tri['abril'] = 15000
print(lucro_1tri)

lucro_1tri.update(lucro_2tri)
print(lucro_1tri)

lucro_1tri.pop('janeiro')
print(lucro_1tri)

del lucro_1tri['janeiro']
print(lucro_1tri)

lucro_1tri.clear()
print(lucro_1tri)