
sets = {'Robson', 'Ana', 'Sofia'}

#add apenas um valor
sets.add('Iris') 

#add varios valores
sets.update({'José', 'Valdite'}) 

#caso não tenha o valor solicitado para remoção o python não trás uma exceção
sets.discard('José') 

# caso não tenha o valor solicitado para remoção o python trás a exceção
sets.remove('Jose') 

#remove o último item aleatório
item = sets.pop() 
print(item)

#zera o set
sets.clear() 
print(sets)

# Criando um conjunto
meu_conjunto = {1, 2, 3, 4, 5}

# Adicionando elementos ao conjunto
meu_conjunto.add(6)
print(meu_conjunto)  # Saída: {1, 2, 3, 4, 5, 6}

# Removendo elementos do conjunto
meu_conjunto.remove(3)
print(meu_conjunto)  # Saída: {1, 2, 4, 5, 6}

# Verificando a existência de um elemento no conjunto
print(2 in meu_conjunto)  # Saída: True

# Operações de conjuntos
outro_conjunto = {4, 5, 6, 7, 8}
print(meu_conjunto.union(outro_conjunto))  # Saída: {1, 2, 4, 5, 6, 7, 8}
print(meu_conjunto.intersection(outro_conjunto))  # Saída: {4, 5, 6}
print(meu_conjunto.difference(outro_conjunto))  # Saída: {1, 2}