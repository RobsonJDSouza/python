'''
Dicionarios são criados com "{}"
São mutável
'''

cadastro = {
    'id': 1,
    'nome': 'Robson',
    'filhos':['Sofia'],
    'compra':[           # Compras é um dicionário dentro de uma lista
        {   
            'id': 19,
            'produto': 'tenis',
            'preço': 299.00
        }
    ]
}

# print(cadastro['id'])
# print(cadastro['compra'][0])
# print(cadastro['compra'][0]['produto'])
# print(f'cadastro["compra"][0]["produto"]') #usando F-string com aspas simples, terei que informar o conteúdo do dicionário com as aspas duplas.

# METODO GET
# filhos_get = cadastro.get('filhos') 
# print(filhos_get)
# altura_get = cadastro.get('altura', None)#com o parametro none, caso passei um informação errada, o get trata o erro trazendo o resultado none.
# print(altura_get)

#ACRESCENTANDO OU MODIFICANDO DADOS
# cadastro['nome'] = 'Ana' #aqui eu modifiquei 
# cadastro['idade'] = 40   #aqui eu acrescentei
# print(cadastro)

# cadastro.update({'idade': 39, 'nome' : 'Robson'}) #pode atualizar mais de uma informação 
# print(cadastro)

# EXCLUIR
del cadastro['nome']
print(cadastro)

cadastro.pop('filhos')
print(cadastro)

cadastro.popitem() #exclui o ultimo item do dicionário
print(cadastro)

cadastro.clear() #exclui todos os itens do dicionário
print(cadastro)

