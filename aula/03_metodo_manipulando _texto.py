#fatiando string
#analise de string
#transformação de string
#Divisão

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