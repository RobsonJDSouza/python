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
# texto = '\nAna Souza' #\n é para pular uma linha 
# arquivo = open('/home/robson.jose/Documentos/cursos/python/aula/aula_python.txt', 'a')
# arquivo.write(texto)
# arquivo.close() #Todo arquivo aberto tem que ser fechado para não corrompe-lo

arquvivo_resultado = []

with open('./aula/aula_python.csv', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()[1:] 
    #Lê linha por linha do arquivo
    # [1:] como o arquivo é uma lista retirei o cabeçalho
    for linha in linhas:
        dados = linha.split(',')
        arquvivo_resultado.append(f'{dados[1]}, {dados[2]}')

with open('./aula/arquivo_saida.csv', 'w') as arquivo_de_saida:
    for resultado in arquvivo_resultado:
        arquivo_de_saida.write(resultado) 