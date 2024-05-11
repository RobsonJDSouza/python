# Adicionar e Remover itens de uma lista
'''
Adicionar:
lista.append(item)

Remover:
item_removido = lista.pop(indice)
lista.remove(item)
'''

# Digamos que você está construindo o controle de produtos da Apple.
# E a Apple lançou o IPhone 11 e irá tirar dos seus estoques o IPhone X


produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']
produtos.append('Robson')
produtos.pop(1)
produtos.remove('apple tv')

print(produtos)