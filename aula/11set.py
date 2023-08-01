'''
Caracteristica
- Desordenados
- Itens não intercambiáveis
- Não são indexados
- Não possuem elementos duplicados
- possuem metodos para manipulação de conjunto

'''

sets = {'Robson', 'Ana', 'Sofia'}

sets.add('Iris') #add apenas um valor

sets.update({'José', 'Valdite'}) #add varios valores

sets.discard('José') #caso não tenha o valor solicitado para remoção o python não trás uma exceção

# sets.remove('Jose') # caso não tenha o valor solicitado para remoção o python trás a exceção

item = sets.pop() #remove o último item aleatório
print(item)

sets.clear() #zera o set
print(sets)