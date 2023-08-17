'''
def- Palavra reservada para a função
chama_nome - Nome da função
(nome) - Parametro da função
return - Palavra reservada do que queremos retornar 
'''


# def teste():
    # print("Valor que eu quero")
# teste()

# def teste_1(nome, sobrenome):
#     print(nome, sobrenome)
# teste_1("Robson", "Souza")


# def teste_2 (x):
#     return x

# y = teste_2("Valor que eu quero")
# print(y)


# def teste_3(*args):
#     print(args)
# lista = [1, 2, 3, 4, 5]
# n1, n2, *n3 = lista
# print(n1, n2, n3)
# print(*lista, sep='-') #desempacotar uma lista #sep comando para separar algo 


#******************************************
# def teste():
#     print('Estou testando as funções')
# teste()


# def chama_nome (nome): #    
#     return(f'Meu nome é {nome}')
# retorno_1 = chama_nome("Robson") #Robson aqui é um argumento. Há diferença entre parametro para argumento
# retorno_2 = chama_nome(nome='Ana') #nesse caso, temos um parametro e um argumento 
# print(retorno_1)
# print(retorno_2)


# def emigres (nome, idea, igreja):
#     print(f'Nome: {nome}, Idade: {idade}, Igreja: {igreja}')
# igrejas('Robson', 39, 'Ass. de Deus')

# def soma(num_1, num_2):
#     return(num_1 + num_2)
# adicao = soma(10, 40)
# print(adicao)

# def calcula_media(nota):
#     media = sum(nota) / len(nota)
#     return media


# teste = calcula_media([10])
# print(teste)

# def soma (*num):
#     resultado = 0
#     for numeros in num:
#         resultado += numeros
#     return resultado

# soma_tudo = soma(1,1)
# print(soma_tudo)

def nome (n, **outros_nomes):
    print(f'{n}')
    print(f'{outros_nomes}')
    for nome, valor in outros_nomes.items():
            print({nome}, {valor})

nome (n = 'Robson', nome = 'Sofia', nome_1 = 'Ana')


