'''
Lista
Temos índice iniciado com o número 0
A lista é associada aos '[]'
'''

#INDEXAÇÃO DA LISTA
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

#TIPO
# print(lista)
# print(type(lista))

#PERCORRER A LISTA
# lista = ['Robson', 1, 5.5, []]
# for i in lista:
#     print(f'Itens da lista: {i}')

#MANIPULAÇÃO DE LISTA - METODOS
lista = ['Robson', 'Ana']

print(lista.append('Sofia')) #acrescenta sem o dado no final da lista

print(lista.extend(['José', 'Iris']))#acrescenta varios dados ou até mesmo, uma outra lista

print(lista.insert(0, 'Valdite'))#acrescenta o dado na lista na posição desejada

print(lista.remove('Valdite'))#remove o primeiro dado passado, no caso de dois dados repetido

print(lista.pop())#remove o último dado da lista, caso não passe nenhuma informação. Passando o indexe, podemos retonar o valor excluído
nome = lista.pop(2)
print(f'Nome que estou excluído {nome}')
print(lista)

# print(lista.clear())#remove todos os valores da lista

print(lista.index('Ana')) #mostra a posição de um determinado valor da lista