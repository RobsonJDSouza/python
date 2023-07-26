'''
Escreva um programa
  Acrescentar porcentagem no salário
'''
salario = float (input('Digite o seu salário: '))
acresc = float (input('Digite o valor de acrescimo: '))


novo_salario = salario + (salario * acresc) / 100
print('O Novo salário será de: {:.2f}'.format(novo_salario))