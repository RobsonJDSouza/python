#### 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor_1 = (input('Valor 1: '))

if valor_1:
    valor_1 = int(valor_1)
    if valor_1 > 0:
        print(f'O valor {valor_1} é posito')
    else:
        print(f'O valor {valor_1} é negativo')
else:
    print(f'Digite o valor')
