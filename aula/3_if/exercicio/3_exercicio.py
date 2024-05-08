#### 1. Faça um Programa que peça dois números e imprima o maior deles.

valor_1 = (input('Valor 1: '))
valor_2 = (input('Valor 2: '))

if valor_1 and valor_2:
    valor_1 = int(valor_1)
    valor_2 = int(valor_2)
    if valor_1 > valor_2:
        print(f'O valor {valor_1} é maior que o {valor_2}')
    else:
        print(f'O valor {valor_2} é maior que o {valor_1}')
else:
    print(f'Digite os dois valores')
