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
2
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

###### CRIANDO ARQUIVO/ESCREVENDO DENTRO DO ARQUIVO######
# texto = 'Robson José de Souza'
# arquivo = open('./aula/aula_python.csv', 'w') #aula_python.csv - inicialmente, cria um arquivo
# arquivo.write(texto) --Posso colocar uma string ou variável
# arquivo.close() #Todo arquivo aberto tem que ser fechado para não corrompe-lo

###### Lendo o arquivo
# arquivo = open('./aula/aula_python.csv', 'r')
# retorno = arquivo.read()
# print(retorno)
# arquivo.close() #Todo arquivo aberto tem que ser fechado para não corrompe-lo

###### Acrescentando dados sem apagar o anterior
# texto = '\nAna Souza' #\n é para pular uma linha 
# arquivo = open('./aula/aula_python.csv', 'a')
# arquivo.write(texto)
# arquivo.close() #Todo arquivo aberto tem que ser fechado para não corrompe-lo





with open('./aula/relatorio.csv', 'r') as arquivo_entrada:
#with - gerenciado de contexto. Não precisa fechar o arquivo no final
#as - alias “pseudônimo”, “apelido” para o arquivo  
    linhas = arquivo_entrada.readlines()[1:] 
    # readlines - Lê todas linhas do arquivo
    # [1:] como o arquivo é uma lista retirei o cabeçalho
    for linha in linhas:
        dados = linha.split(',')
        arquvivo_resultado.append(f'{dados[1]}, {dados[2]}')

with open('./aula/arquivo_saida.csv', 'w') as arquivo_de_saida:
    for resultado in arquvivo_resultado:
        arquivo_de_saida.write(resultado) 