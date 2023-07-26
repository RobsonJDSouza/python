'''
Escreva um programa
  Mostre o dobro
  Mostre o triplo
  Mostre a raiz
'''
n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('Vocẽ digitou {}'.format(n))
print('O dobro de {} é: {}'.format(n, d))
print('O triplo de {} é: {}'.format(n, t))
print('A raiz quadrada de {} é: {:.3f}'.format(n, r))