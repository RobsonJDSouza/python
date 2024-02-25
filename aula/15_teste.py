'''
MANIPULANDO LISTA
teste = ["Robson", "Ana", "Sofia"]
teste_atual = []
for lista in teste:
    teste_atual.append(lista.upper().split())

primeira = teste_atual[0]
print(primeira)
'''

'''
MANIPULAÇÃO DE ARQUIVO
texto = 'Robson'
arquivo = open('./aula/aula_python.csv','w')
arquivo.write(texto)

arquivo = open('./aula/aula_python.csv', 'r')
retorno = arquivo.read()
print(retorno)

texto = '\n Ana'
arquivo = open('./aula/aula_python.csv','a')
arquivo.write(texto)
'''
texto = 'id,nome,sobrenome,email,\n1,Robson,Souza,robson@hotmail.com\n2,Ana,Souza,ana@gmail.com\n3,Soso,Rosa,sofi@gmail.com'
arquivo = open('./aula/relatorio.csv', 'a')
arquivo.write(texto)