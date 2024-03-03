"""
ordem de precedência
1 - ()
2 - **
3 - * - / - // - %
4 = + OU -
""""""  """

# https://www.w3schools.com/python/python_operators.asp

n1 = 5
n2 = 2

# Operadores aritméticos 
print('Soma -',n1 + n2)
print('Subtração -',n1 - n2)
print('Multiplicação -',n1 * n2)
print('Divisão -',n1 / n2)
print('Divisão inteira -', n1 // n2)
print('Modulo -', n1 % n2)
print('Exponenciação -', n1 ** n2)

# Operadores de atribuição 
x = 2
x+= 1 # x = x + 1
print(x)

# Operadores de comparação
x = 2
y = 3
print('Igual -',x == y )
print('Não igua -',x != y )
print('Maior -',x > y )
print('Menor -',x < y )
print('Maior ou Igual -',x >= y )
print('Menor ou Igual -',x <= y )