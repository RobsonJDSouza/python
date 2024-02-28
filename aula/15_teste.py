cadastro = {
    'id': 1,
    'nome': 'Robson',
    'filhos':['Sofia'],
    'compra':[           # Compras é um dicionário dentro de uma lista
        {   
            'id': 19,
            'produto': 'tenis',
            'preço': 299.00
        },

        {   
            'id': 19,
            'produto': 'roupa',
            'preço': 299.00
        }
    ]
}

print(f"Robson comprou um {cadastro['compra'][1]['produto']}")