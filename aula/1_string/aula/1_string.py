#fatiando string
#analise de string
#transformação de string
#Divisão

#https://www.w3schools.com/python/python_strings.asp

a = 'robson jose de souza'

#fatiamento
print(a[3])
print(a[2:9])
print(a[:10])
print(a[2:])
print(a[2::2])# Não sei o final da string
print(a[::19])# Não sei o começo e o final da string

#Transformação de string
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.strip()) #remove os espaços inúteis no começo e no fim
print(a.rstrip())
print(a.lstrip())
print(a.split()) #dividir a string em uma lista - Divisão
print(' '.join(a))
print(a.count('o'))
print(a.title().count('J'))
print(a.replace('robson jose de souza', 'ana claudia de souza')) #trocar a string
a = a.replace('robson jose de souza', 'ana claudia de souza')
print(a)
print('robson' in a) #Se tem o nome robson digitado no programa
print(a.find('ana'))
a = a.split()
print(a[3][4])

print('oi'*5)
print('Meu nom é: {:>20} '.format(n3))
print('Meu nom é: {:<20} '.format(n3))
print('Meu nom é: {:^20} '.format(n3))
print('Meu nom é: {:=^20} '.format(n3))
print('Divião é {:.1f}'.format(a)) #Coloca a quantidade de casas decimais na divisão
print('Robson' , end=' ') #A funnão end coloca nesse caso, os prints na mesma linha
print('Souza')
print('Robson \nJosé \nde \nSouza') #A função \n, ela faz pular uma linha


# \t - Tabulação
# \n - Pula uma linha


# TIPO
a = input('Digite algo: ')

print("O tipo primitivo desse valor é ", type(a))
print("Só tem espaço ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumerico ", a.isalnum())
print("Está em maiuscula? ", a.isupper())
print("Está em minuscula? ", a.islower())
print ("Está capitalizada "), a.istitle() #primeira letra em maiúscula


# Sem F string
print('A soma de {} + {} é igual:'.format(n1, n2, n1 + n2))
print('A subtração de {} + {} é igual:'.format(n1, n2, n1-n2))

#Com F String
print(f'A multiplicação de {n1}  {n2}')
print('A divisão de {} + {} é igual:'.format(n1, n2, n1/n2))
print('A divisão inteira de {} + {} é igual:'.format(n1, n2, n1//n2))
print('A exponenciação {} elevado {} é igual:'.format(n1, n2, n1**n2))  #potência feita com o operador dela
print('A exponenciação {} elevado {} é igual:'.format(n1, n2), pow(3, 2)) #potência feita com a função dela
print('O modulo {} + {} é igual:'.format(n1, n2, n1%n2))
print('A Raiz quadrada de {} é igual:'.format(n1, n1 ** (1/2))) #calculo de raiz quadrada
print('='*20)