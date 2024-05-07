# Criando uma tupla
minha_tupla = (1, 2, 3, 4, 5)

# Acessando elementos da tupla
print(minha_tupla[0])  # Saída: 1

# Tentativa de modificar um elemento da tupla (vai gerar um erro)
# minha_tupla[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Concatenando tuplas
outra_tupla = (6, 7, 8)
nova_tupla = minha_tupla + outra_tupla
print(nova_tupla)  # Saída: (1, 2, 3, 4, 5, 6, 7, 8)

# Desempacotando uma tupla
a, b, c = minha_tupla
print(a, b, c)  # Saída: 1 2 3