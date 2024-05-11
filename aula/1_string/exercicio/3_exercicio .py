#### 1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

'''Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.'''

print('Compara duas strings')

s1 = input('String 1: ')
s2 = input('String 2: ')
print(f'Tamanho de "{s1}": {len(s1)} caracteres')
print(f'Tamanho de "{s2}": {len(s2)} caracteres')

if len(s1) == len(s2):
    print('As strings são de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')
    
if s1 == s2:
    print('As strings possuem conteúdos iguais.')
else:
    print('As duas strings possuem conteúdo diferente.')



#### 2. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

'''Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133'''

print('Valida e corrige número de telefone')

tel = input('Telefone: ')
tel = tel.replace('-', '')
if len(tel) == 7:
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    tel = '3' + tel
    print(f'Telefone corrigido sem formatação: {tel}')
    print(f'Telefone corrigido com formatação: {tel[:4]}-{tel[4:]}')
else:
    print('O telefone não tem 7 dígitos.')