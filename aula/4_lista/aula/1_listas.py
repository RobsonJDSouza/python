# Estrutura:
'''
lista = [valor, valor, valor, valor, ...]


- Lista é um dos objetos mais importantes de Python, por isso vamos trabalhar bastante neles
- Quando importamos uma base de dados para o Python, normalmente ele é lido como uma "lista" ou como alguma "variação de lista"
- Listas em Python foram feitas para serem homogêneas, apesar de aceitarem valores heterogêneos
- Exemplos de Lista:
'''
# Listas de Produtos de uma Loja:
produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

# Lista de Unidades Vendidas de cada Produto da Loja
vendas = [1000, 1500, 350, 270, 900]


#TIPO
# lista = ['Robson', 1, 5.5, []]
# print(type(lista))


# INDEXAÇÃO DA LISTA
# lista = ['Robson', 1, 5.5, []]
# print(f'{lista[0]} Souza') 


#FATIAMENTO DE LISTA
# lista = ['a', 'b', 'c', 'd', 'e', 'f']
# print(lista[0:3:1])
# print(lista[3:6:1])
# print(lista[::-1])
# print(lista[-6:-3:1])
# print(lista[3::1])
# print(lista[::2])
# print(lista[1::2])
# print(lista[::2] + lista[1::2]) #concatenar lista resultante

#PERCORRER A LISTA
lista = ['Robson', 1, 5.5, []]
# for i in lista:
#     print(f'Itens da lista: {i}')

#MANIPULAÇÃO DE LISTA - METODOS
# lista = ['Robson', 'Ana']

#acrescenta sem o dado no final da lista
# print(lista.append('Sofia')) 

#acrescenta varios dados ou até mesmo, uma outra lista
# print(lista.extend(['José', 'Iris']))

#acrescenta o dado na lista na posição desejada
# print(lista.insert(0, 'Valdite'))

#remove o primeiro dado passado, no caso de dois dados repetido
# print(lista.remove('Valdite'))

#remove o último dado da lista, caso não passe nenhuma informação. Passando o index, podemos retonar o valor excluído
# print(lista.pop())
# nome = lista.pop(2)
# print(f'Nome que estou excluído {nome}')
# print(lista)

#remove todos os valores da lista
# # print(lista.clear())

#mostra a posição de um determinado valor da lista
# print(lista.index('Ana')) 

#mostra a posição de um determinado valor da lista. Podemos passar o começo e o final do range.
# print(lista.index('Ana', 0, 4)) 

#orderna a lista
# lista.sort() 
# print(lista)

#orderna a lista do final para o início
# lista.sort(reverse=True)
# print(lista)

# lista.reverse
# print(lista)