# Estrutura de dados: Um dicionário é uma coleção de dados que permite armazenar pares de chave-valor. Cada chave em um dicionário é única e é usada para acessar seu valor correspondente.

# Chave e valor: Cada entrada no dicionário consiste em uma chave e um valor associado. A chave é usada como um identificador exclusivo para o valor correspondente. Os valores podem ser de qualquer tipo de dado, incluindo inteiros, strings, listas, outros dicionários, etc.

# Acesso aos valores: Para acessar um valor em um dicionário, você usa sua chave correspondente. Isso significa que você não precisa percorrer todos os elementos do dicionário para encontrar um valor específico, como faria em uma lista. Em vez disso, você simplesmente fornece a chave e o dicionário retorna o valor associado a essa chave.



# SINTAXE
# {chave:valor for item in sequencia}


clientes = {
    'Robson': '20/01.1984',
    'ana': '24.01.1982',
    'soFia': '21/03.2016' 
}

# FORMA SEM A COMPREENSÃO
# clientes_resultado = {}
# for chave, valor in clientes.items():
#     clientes_resultado =chave.capitalize(), valor.replace('.','/')
#     print(clientes_resultado)


# FORMA COM A COMPREENSÃO
resultado = {chave.capitalize():valor.replace('.','/') for chave, valor in clientes.items() }
print(resultado)


# FORMA COM A COMPREENSÃO COM UMA CONDIÇÃO
# {chave:valor for item in sequencia if condição}
resultado = {chave.capitalize():valor.replace('.','/') for chave, valor in clientes.items() if chave == 'Robson'}
print(resultado)