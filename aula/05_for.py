# sequencia = [1, 2, 3]

# for i in(sequencia):
#     print(i)

# for i in range(0, 10):
#     print(i)

# for i,  in range(0, 11, 2):
#     print(i)

set_ = {1, 2, 3}
tupla = (1, 2, 3)
lista = [1, 2, 3]
dicionario = {'a': 1, 'b': 2}

for elemento in set_:
    print(f'[SET] Elemento: {elemento}')

for elemento in tupla:
    print(f'[Tupla] Elemento: {elemento}')

for elemento in lista:
    print(f'[Lista] Elemento: {elemento}')

for elemento in dicionario.items():
    print(f'[Dicionario] Elemento: {elemento}')