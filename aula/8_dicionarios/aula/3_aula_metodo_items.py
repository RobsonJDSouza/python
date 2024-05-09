# Métodos úteis em dicionários

## items() dos dicionários

### Estrutura:
'''itens_dicionario = dicionario.items()

ou então:

for item in dicionario.items()
    cada item do dicionario em formato de tupla'''


vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

# itens = vendas_tecnologia.items()
# print(itens)

for produto, qtde in vendas_tecnologia.items():
    print(f'{produto} com {qtde} unidades')
