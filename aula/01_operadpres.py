"""
ordem de precedência
1 - ()
2 - **
3 - * - / - // - %
4 = + OU -
""""""  """

n1 = 5
n2 = 2
n3 = 'Robson'
d = n1 / n2

print('A soma de {} + {} é igual:'.format(n1, n2, n1 + n2))
print('A subtração de {} + {} é igual:'.format(n1, n2, n1-n2))
print('A multiplicação de {} + {} é igual:'.format(n1, n2, n1*n2))
print('A divisão de {} + {} é igual:'.format(n1, n2, n1/n2))
print('A divisão inteira de {} + {} é igual:'.format(n1, n2, n1//n2))
print('A exponenciação {} elevado {} é igual:'.format(n1, n2, n1**n2))  #potência feita com o operador dela
print('A exponenciação {} elevado {} é igual:'.format(n1, n2), pow(3, 2)) #potência feita com a função dela
print('O modulo {} + {} é igual:'.format(n1, n2, n1%n2))
print('A Raiz quadrada de {} é igual:'.format(n1, n1 ** (1/2))) #calculo de raiz quadrada
print('='*20)
print('oi'*5)
print('Meu nom é: {:>20} '.format(n3))
print('Meu nom é: {:<20} '.format(n3))
print('Meu nom é: {:^20} '.format(n3))
print('Meu nom é: {:=^20} '.format(n3))
print('Divião é {:.1f}'.format(d)) #Coloca a quantidade de casas decimais na divisão
print('Robson' , end=' ') #A funnão end coloca nesse caso, os prints na mesma linha
print('Souza')
print('Robson \nJosé \nde \nSouza') #A função \n, ela faz pular uma linha