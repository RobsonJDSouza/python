vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

for venda in vendas_tecnologia:
    print(venda, vendas_tecnologia[venda])


# Qual o total de notebooks vendidos?

notebook = 0
for venda in vendas_tecnologia:
    if 'notebook' in venda:
        notebook += vendas_tecnologia[venda]
print(f'A quantidade vendido de Notebook é de {notebook} unidades')