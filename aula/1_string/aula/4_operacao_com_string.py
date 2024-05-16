# Operações com String

'''
str -> transforma número em string<br>
in -> verifica se um texto está contido dentro do outro
operador + -> concatenar string
format e {} -> substitui valores
%s -> substitui textos
%d -> substitui números decimais
'''

faturamento = 1000
custo = 500
lucro = faturamento - custo

#Uso do str() e do concatenar com +
# file deepcode ignore addOfStringAndNonString: <please specify a reason of ignoring this>
print ('O faturamento da loja foi de: ' + faturamento)

#Uso do Format
print('O faturamento foi de: ')

#Uso do %s e %d
print ('O faturamento foi de: ')

#Uso do in (mais exercícios práticos nas próximas aulas)
print('@' in 'lira@gmail.com')
# file deepcode ignore incomplete~url~sanitazation: <please specify a reason of ignoring this>
print('@' in 'lira.gmail.com')