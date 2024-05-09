# - clear() - Deleta todos os elementos do Dicionário (semelhante ao que aprendemos em listas)

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_mes.clear()
print(f'Dicionário {vendas_mes} deletado')


# - copy() - Cria uma cópia do dicionário (semelhante ao que aprendemos em listas)

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_mes_copia = vendas_mes.copy()
print(f'O dicionário {vendas_mes_copia} é uma copia do dicionário {vendas_mes}.')


# - fromkeys(chaves, valor_padrao) - Cria um dicionário com as chaves e o mesmo valor padrão para todas as chaves
chaves = ('jan', 'fev', 'mar')
inicio = '1º trimestre'
chave_final = dict.fromkeys(chaves, inicio)
print(chave_final)


# - get(chave) - Retorna o valor especificado pela chave (Semelhante a fazer dictionario[chave]
vendas_mes = {'jan': 180, 'fev': 100, 'mar': 190}
print(vendas_mes.get('jan'))


# - items() - Retorna uma lista em que cada item é uma tupla com (chave, valor)
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
lista = list(vendas_mes.items())
print(lista)


# - keys() - Retorna uma lista com todas as chaves do dicionário
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
lista = list(vendas_mes.keys())
print(lista[1])


# - values() - Retorna uma lista com todos os valores do dicionários
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(list(vendas_mes.values()))


# - pop(chave) - Retira o item do dicionário e retorna o valor dele para ser usado
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_fev = vendas_mes.pop('fev') #retira o fevereiro do dicionário ao mesmo tempo que armazena o valor dele na variável
print(vendas_mes)
print(vendas_fev)


vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
#retira o último item adicionado no dicionário ao mesmo tempo que armazena o item(chave, valor) dele na variável
vendas_ult = vendas_mes.popitem() 
print(vendas_mes)
print(vendas_ult)


# - setdefault(chave, valor) - Retorna o valor da chave passada, mas caso a chave não exista, cria no dicionário o item com a chave e valor passados.
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_fev = vendas_mes.setdefault('fev', 500)
print(vendas_fev)
# repare que como fevereiro existe na lista, ele procura pelo valor de fevereiro e ignora o 500 passado
#agora quando não existe na lista:
vendas_abr = vendas_mes.setdefault('abr', 600)
#repare que agora além de vendas_abr retornar o 600 como valor, ele adicionou um item no dicionario
print(vendas_abr)
print(vendas_mes)


# - update(dicionario) - Adiciona o dicionário passado como parâmetro ao dicionário original
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_2tri = {'abr': 400, 'mai': 600, 'jun': 500}
vendas_mes.update(vendas_2tri)
print(vendas_mes)







