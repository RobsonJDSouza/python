'''
Escreva um programa
   Quantas letras 'A' tem? 
   Em que posição aparece 'A' pela primeira vez
   Em que posição ela o 'A' aparece na última vez
'''


nome = str(input('Digite o seu nome: ')).strip().upper()

print('Seu nome tem {} letras O'.format(nome.count('O')))
print('Letra O aparece na posição {} pela primeira vez'.format(nome.find('O')))
print('Letra O aparece na posição {} pela última vez'.format(nome.rfind('O')))

nome = str(input('Digite o seu nome: ')).strip()
nomesp = nome.split()

print('Seu primeiro nome é {} e o seu último nome é {}'.
      format(nomesp[0], nomesp[len(nomesp)-1]))