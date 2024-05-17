
# Métodos Específicos de Lista em Python

'''list.append(valor)'''
# Adiciona um valor ao final de uma lista
# # Uso:
vendas = [150, 320]
vendas.append(110)
# Resultado:
print(f'Usando append {vendas}') 


'''list.extend(lista2)'''
# Adiciona todos os valores da lista2 na lista original
# Uso:
vendas = [150, 320, 110, 450, 390, 370]
vendas_2 = [440, 470, 900, 1000, 1100, 1050]
vendas.extend(vendas_2)
# Resultado:          
print(f'Usando extend {vendas}')  


'''list.insert(posicao, valor)'''
# Adiciona um valor em uma posição específica em uma lista. Não é recomendado usar a não ser que seja realmente necessário inserir em uma posição específica, porque o método append é mais eficiente.
# Uso:
vendas = [150, 320]
vendas.insert(1, 110)
# Resultado:
print(f'Usando insert {vendas}')
# Obs:
# Compare com o caso do list.append para ver a diferença


'''list.remove(valor)'''
# Remove o valor da lista (apenas a 1ª ocorrência, então caso haja 2 vezes o valor na lista, apenas a 1ª será removida). Além disso, dá um erro caso valor não exista dentro da lista.
# Uso:
vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
vendedores.remove('Maria')
# Resultado:
print(f'Usando remove {vendedores}')


'''list.pop(posicao)'''
# Remove o item que está na posicao (índice) passado. Além disso, esse item é dado como resultado do pop, portanto pode ser armazenado em uma variável ou usado para outra coisa na mesma linha de código.
# Uso:
vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
vendedores.pop(2)
# Resultado:
print(f'Usando pop{vendedores}')


'''list.clear()'''
# Remove todos os itens de uma lista
# Uso:
vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
vendedores.clear()
# Resultado:
print(f'Usando clear {vendedores}')


'''list.index(valor)'''
# Retorna a posição do valor dentro da lista (em qual índice está o valor). Dá erro caso não haja o valor dentro da lista.
# Uso:
vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
posicao_Joao = vendedores.index('João')
# Resultado:
print(f'Usando index {posicao_Joao}')


'''list.count(valor)'''
# Retorna a quantidade de vezes que o valor aparece na lista
# Uso:
vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus', 'João']
qtde_Joao = vendedores.count('João')
# Resultado:
print(f'Usando count {qtde_Joao}')


'''list.sort(reverse=False)'''
# Ordena os valores da lista em ordem crescente, ou alfabética, (reverse=False) ou decrescente (reverse=True).
# Uso:
vendas = [150, 300, 190, 480]
vendas.sort(reverse=True)
# Resultado:
print(f'Usando sort {vendas}')


'''list.reverse()'''
# Inverte a ordem dos elementos de uma lista.
# Uso:
vendas = [150, 300, 190, 480]
vendas.reverse()
# Resultado:
print(f'Usando reverse {vendas}')


'''list.copy()'''
# Cria uma cópia da lista original. Outra opção é fazer lista2 = lista1[:]
# Uso:
vendas = [150, 300, 190, 480]
vendas2 = vendas.copy()
# Resultado:
print(f'Usando copy {vendas2}')
