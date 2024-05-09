### O for vai funcionar normal em dict_listas, porque não deixa de ser uma lista de itens que pode ser percorrida (iterable), mas o que aprendemos de lista não necessariamente se aplicam a essas dict_listas.

'''Para transformar as dict_listas em listas normais, usamos a função list:

- lista_chaves = list(dicionario.keys()

- Pode ser útil caso a gente queira fazer alguma organização das chaves. Ex: Imprimir uma lista com os valores em ordem alfabética, de forma que todas as tvs fiquem juntas, todos os iphone/ipad também e assim vai:'''

vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

# for chave in vendas_tecnologia:
#     print(chave, vendas_tecnologia[chave])

chave = vendas_tecnologia.keys()

lista_chave = list(chave)
lista_chave.sort()

for chave in lista_chave:
    print(chave, vendas_tecnologia[chave])
