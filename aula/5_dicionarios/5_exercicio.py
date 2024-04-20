#### Qual o valor do ps5
# vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}
# print(vendas_tecnologia.get('ps5'))


#### Qual o total de notebooks vendidos?
vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

total = 0
for vendas in vendas_tecnologia:
    if 'notebook' in vendas:
        total += vendas_tecnologia[vendas]    
print(total)
        
