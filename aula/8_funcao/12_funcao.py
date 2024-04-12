'''
Definição de Função: 
Uma função em Python é um bloco de código reutilizável que executa uma tarefa específica. Elas são utilizadas para modularizar o código, tornando-o mais organizado, legível e fácil de manter. As funções ajudam a evitar a repetição de código, permitindo que você defina uma tarefa uma vez e a reutilize sempre que necessário.

Observações
def- Palavra reservada para a função
return - Palavra reservada do que queremos retornar 
saudacao - Nome da função
(nome) - Parametro da função

Escopo po de Variáveis: 
As variáveis definidas dentro de uma função têm um escopo local, o que significa que elas só podem ser acessadas dentro da própria função. Variáveis definidas fora de uma função têm escopo global e podem ser acessadas de qualquer lugar do programa, incluindo dentro de funções.Esco

Parâmetros: 
São variáveis que você passa para a função quando ela é chamada. As funções podem ter zero ou mais parâmetros. No exemplo acima, nome é um parâmetro da função saudacao.

Corpo da Função: 
É o bloco de código que contém as instruções que a função executa quando é chamada. O corpo da função é indentado em relação à definição da função. Por exemplo:

'''

# Para definir uma função em Python, você utiliza a palavra-chave def, seguida pelo nome da função e, opcionalmente, parâmetros entre parênteses. Por exemplo:
def saudacao(nome):
    print("Olá,", nome)

def saudacao(nome):
    print("Olá,", nome)  # Corpo da função


# Chamada de Função: Para executar o código dentro de uma função, você a chama pelo seu nome, seguido pelos parênteses contendo os argumentos (se houver). Por exemplo:
saudacao("Maria") # Neste exemplo, "Maria" é o argumento passado para a função saudacao.


# Valor de Retorno: Uma função pode opcionalmente retornar um valor utilizando a palavra-chave return. Por exemplo:
def soma(a, b):
    return a + b # Neste exemplo, a função soma retorna a soma dos dois argumentos a e b.
print( soma(2, 3))


# Aqui está um exemplo simples de uma função em Python que calcula o quadrado de um número:
def quadrado(numero):
    return numero ** 2

resultado = quadrado(5)
print(resultado)  # Saída: 25


###############################
# def teste_3(*args):
#     print(args)
# lista = [1, 2, 3, 4, 5]
# n1, n2, *n3 = lista
# print(n1, n2, n3)
# print(*lista, sep='-') #desempacotar uma lista #sep comando para separar algo 



# def nome (n, **outros_nomes):
#     print(f'{n}')
#     print(f'{outros_nomes}')
#     for nome, valor in outros_nomes.items():
#             print({nome}, {valor})

# nome (n = 'Robson', nome = 'Sofia', nome_1 = 'Ana')

# #Aula 01/02/2024
# def monta_computador(cpu, memoria, hd, monitor= 4, **outros_atributos): 
# #cpu, memoria e hd são parametros da função
# #Paramentros com valores. Acrescentado o monitor com o valor
# #Colocar varios atributos. Acrescentado 2 asterisco com parametros da função. Teremos um dicionario na chamada.
#     print('Informações do computador')
#     print(f"CPU: {cpu}, Memoria: {memoria}, HD: {hd}, Tela {monitor}")
#     print(f"outros_atributos: ")

#     for chave, valor in outros_atributos.items():
#         print(f'{chave}: {valor}')

# # monta_computador(1, 2, 3) #Argumento posicional
# # monta_computador(hd=1, memoria=2, cpu=3) #Argumento nomeados
# # monta_computador(hd=1, memoria=2, cpu=3, monitor= 4) #Troque o valor do argumento monitor
# monta_computador(1, 2, 3, monitor= 4, mouse= 5, note= 6) 