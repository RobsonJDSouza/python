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
            'preco': 299.00
        },

        {   
            'id': 14,
            'produto': 'roupa',
            'preco': 299.00
        }
    ]
}

# print(cadastro)
# print(cadastro['compra'])
# print(cadastro['compra'][0])
# print(cadastro['compra'][1]['preco'])
# print(f'cadastro["compra"][0]["produto"]') #usando F-string com aspas simples, terei que informar o conteúdo do dicionário com as aspas duplas.


########## METODO GET ####'######
# filhos_get = cadastro.get('compra', None) 
# print(filhos_get)

# altura_get = cadastro.get('altura', None)#com o parametro none, caso passei um informação errada, o get trata o erro trazendo o resultado none.
# print(altura_get)