'''
Escreva um programa em python que receba uma lista de 10 números e retorne:
a média desses valroes
a mediana desses valores
a moda desses valores

def valores():
    lista_re = [2, 4, 6, 2, 4, 6, 8, 12, 34, 50]
    soma_lista = sum(lista_re)
    print(f"A media da lista é:{soma_lista/10}")
    print(f"A mediana da lista é:{}")
    print(f"A moda da lista é:{}")
valores()
'''
#from statistics import median
import statistics as sta

def d():
    valores = []
    while True: 
        valores  (int(x) for x in range(0,10))

        # valores.append(int(input('Digite 10 números:')))
        #continuar = str(input('Você quer continuar? [S/N]'))
        #if continuar in 'Nn':
        #break
    print(f'A média da lista é: {sta.mean(valores) }') #{sum(valores)/2 }')
    print(f'A Mediana da lisara é o número {sta.median(valores)}')
    print(f"A moda da lista é: {sta.mode(valores)}")
d()


