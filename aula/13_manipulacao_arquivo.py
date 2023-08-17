'''
--Texto (legível)
TXT
json
xml
html

--Binários (ilegível)
Vídeos
PDF
Imagem
XLSX
Docx
PPTX

--Função
open(arquivo, modo)

arquivo - /robson/python/teste/arquivo.csv
modo - leitura / escrita / anexar

Texto
Leitura - "r"
Leitura / Escrita - "r+"

Escrita - "w"
Escrita / leitura - "w+"

Append
Anexar "a"
Anexar / leitura - "a+"

Binário
Leitura - "rb"
Leitura / Escrita - "rb+"

Escrita - "wb"
Escrita / leitura - "wb+"

Append
Anexar "ab"
Anexar / leitura - "ab+"

Exemplo
arq = open("/robson/python/teste/arquivo.csv", "r")
'''

###### Escrevendo dentro do arquivo ######
# texto = 'Robson José de Souza'
# arquivo = open('/home/robson.jose/Documentos/cursos/python/aula/aula_python.txt', 'w')
# arquivo.write(texto)

###### Lendo o arquivo
# arquivo = open('/home/robson.jose/Documentos/cursos/python/aula/aula_python.txt', 'r')
# retorno = arquivo.read()
# print(retorno)

###### Acrescentando dados sem apagar o anterior
texto = '\nAna Souza'
arquivo = open('/home/robson.jose/Documentos/cursos/python/aula/aula_python.txt', 'a')
arquivo.write(texto)
arquivo.close() #Todo arquivo aberto tem que ser fechado para não corrompe-lo