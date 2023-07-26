'''
Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:

Primeiro os Pares
Depois os Ímpares
Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.

Entrada
A primeira linha de entrada contém um único inteiro positivo N (1 < N <= 105) Este é o número de linhas de entrada que vem logo a seguir. As próximas N linhas conterão, cada uma delas, um valor inteiro não negativo.

numero = int(input())
numero_par = []
numero_impar = []

for i in range (numero):
    n = int(input())
    if n%2==0:
        numero_par.append(n)
    else:
        numero_impar.append(n)

numero_par = sorted(numero_par)
numero_impar= sorted(numero_par, reverse=True)

for i in range(len(numero_par)):
    print(numero_par[i])

for l in range(len(numero_impar)):
    print(numero_impar[l])

'''
n = int(input())
pares = []
impares = []
for lista in range(0,n):
    numero = int(input())
    if (numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)
pares.sort()
impares.sort(reverse=True)

for lista in pares:
    print(lista)
for lista in impares:
    print(lista)