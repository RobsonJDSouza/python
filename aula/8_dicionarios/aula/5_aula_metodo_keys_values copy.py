# Listas importantes a partir do Dicionário

### Métodos importantes:

'''.keys() -> uma "lista" com todas as chaves do dicionario

.values() -> uma "lista" com todos os valores do dicionario

Obs: Se o dicionario for modificado, automaticamente essas variáveis são modificadas, mesmo tendo sido criadas anteriormente'''

vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 15720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()
print(chaves)
print(valores)

vendas_tecnologia['robsonfone'] = 20000
print(list(valores))


