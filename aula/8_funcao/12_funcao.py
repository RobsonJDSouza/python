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

# def nome (n, **outros_nomes):
#     print(f'{n}')
#     print(f'{outros_nomes}')
#     for nome, valor in outros_nomes.items():
#             print({nome}, {valor})

# nome (n = 'Robson', nome = 'Sofia', nome_1 = 'Ana')

#Aula 01/02/2024
def monta_computador(cpu, memoria, hd, monitor= 4, **outros_atributos): 
#cpu, memoria e hd são parametros da função
#Paramentros com valores. Acrescentado o monitor com o valor
#Colocar varios atributos. Acrescentado 2 asterisco com parametros da função. Teremos um dicionario na chamada.
    print('Informações do computador')
    print(f"CPU: {cpu}, Memoria: {memoria}, HD: {hd}, Tela {monitor}")
    print(f"outros_atributos: ")

    for chave, valor in outros_atributos.items():
        print(f'{chave}: {valor}')

# monta_computador(1, 2, 3) #Argumento posicional
# monta_computador(hd=1, memoria=2, cpu=3) #Argumento nomeados
# monta_computador(hd=1, memoria=2, cpu=3, monitor= 4) #Troque o valor do argumento monitor
monta_computador(1, 2, 3, monitor= 4, mouse= 5, note= 6) 