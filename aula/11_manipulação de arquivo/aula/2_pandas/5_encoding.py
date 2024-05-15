import pandas as pd

'''
encoding='latin1'
encoding='ISO-8859-1'
encoding='utf-8'
encoding='cp1252
'''

# "r" antes do caminho do arquivo em Python significa "raw string" (cadeia de caracteres bruta). Ele indica que os caracteres especiais dentro da string não devem ser interpretados de forma especial. 
planilha_cliente = pd.read_csv(r'11_manipulação de arquivo/aula/2_pandas/planilha/clientes.csv', sep=';', encoding='latin1')
print(planilha_cliente)