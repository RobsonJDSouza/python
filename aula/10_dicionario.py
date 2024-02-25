'''
Dicionarios são criados com "{}"
São mutável
'''

# cadastro = {
#     'id': 1,
#     'nome': 'Robson',
#     'filhos':['Sofia'],
#     'compra':[           # Compras é um dicionário dentro de uma lista
#         {   
#             'id': 19,
#             'produto': 'tenis',
#             'preço': 299.00
#         }
#     ]
# }

# print(cadastro['id'])
# print(cadastro['compra'][0])
# print(cadastro['compra'][0]['produto'])
# print(f'cadastro["compra"][0]["produto"]') #usando F-string com aspas simples, terei que informar o conteúdo do dicionário com as aspas duplas.


########## METODO GET ##########
# filhos_get = cadastro.get('filhos') 
# print(filhos_get)
# altura_get = cadastro.get('altura', None)#com o parametro none, caso passei um informação errada, o get trata o erro trazendo o resultado none.
# print(altura_get)


######### ACRESCENTANDO OU MODIFICANDO DADOS ##########
# cadastro['nome'] = 'Ana' #aqui eu modifiquei 
# cadastro['idade'] = 40   #aqui eu acrescentei
# print(cadastro)

# cadastro.update({'idade': 39, 'nome' : 'Robson'}) #pode atualizar mais de uma informação 
# print(cadastro)

########## EXCLUIR ##########
# del cadastro['nome']
# print(cadastro)

# cadastro.pop('filhos')
# print(cadastro)

# cadastro.popitem() #exclui o ultimo item do dicionário
# print(cadastro)

# cadastro.clear() #exclui todos os itens do dicionário
# print(cadastro)

########## METODOS DO DICIONÁRIO ##########
# familia = {
#     'pai': 'Robson',
#     'mae': 'Ana',
#     'filha': 'Sofia'
# }


# copia_familia = familia.copy()
# print(copia_familia)

# item = familia.items() #pega os dois valores
# print(item)
# for itens in item:
#     print(f'Chave:{itens[0]} Valor:{itens[1]}')

# chaves = familia.keys()#pega apenas as chaves
# print(chaves)
# for i in chaves:
#     print(i)

# valores = familia.values()#pega somente os valores
# print(valores)
# for i in valores:
#     print(i)

# familia.setdefault('sogra', 'Valdite')#insere a chave com o valor passado se a chave não estiver presente n odicionário
# print(familia)                        #retorna o valor da chave se a hchave já estiver presente no dicionário

chaves = ['Robson', 'Ana']
valor = 0
familia1 = dict.fromkeys(chaves, valor)
print(type(familia1))
