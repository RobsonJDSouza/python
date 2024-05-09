vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 15720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

# - Quais produtos venderam mais de 5000 unidades?

for vendas in vendas_tecnologia:
    if vendas_tecnologia[vendas] >= 17000:
        print(vendas, vendas_tecnologia[vendas])

print('-' * 50)

for produto, qtde in vendas_tecnologia.items():
    if qtde >= 15000:
        print(produto, qtde)