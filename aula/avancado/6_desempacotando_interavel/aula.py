'''O asterisco (*) em Python é usado para desempacotar iteráveis, como listas ou conjuntos, em argumentos individuais em chamadas de função. Isso é útil quando você tem uma coleção de valores que deseja passar como argumentos para uma função que espera argumentos '''

#lista
def minha_funcao(a, b, c):
    print(a, b, c)

lista = [1, 2, 3]
minha_funcao(*lista)


# conjunto
def minha_funcao(a, b, c):
    print(a, b, c)

conjunto = {'x', 'y', 'z'}
minha_funcao(*conjunto)


