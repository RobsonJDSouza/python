
# Forma Básica
precos = "Jan: 25, Fev: 27, Mar: 29"
preco_janeiro = precos[5:7]
print(preco_janeiro)

preco_marco = precos[-2:]
print(preco_marco)


# Posição Inicial e Final
preco_fev = precos[14:16]
print(preco_fev)

preco_fev2 = precos[-11:-9]
print(preco_fev2)


# Posição Inicial e Final com Step
codigo = "1.2.3.4,5,1,2.3.4,7.9"
num_codigos = codigo[-1::-1]
print(num_codigos)