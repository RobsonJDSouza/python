import pandas as pd

'''
encoding='latin1'
encoding='ISO-8859-1'
encoding='utf-8'
encoding='cp1252
'''

# "r" antes do caminho do arquivo em Python significa "raw string" (cadeia de caracteres bruta). Ele indica que os caracteres especiais dentro da string não devem ser interpretados de forma especial. 
planilha_cliente = pd.read_csv(r'11_manipulação de arquivo/aula/2_pandas/planilha/clientes.csv', sep=';', encoding='latin1')
planilha_vendas = pd.read_csv('11_manipulação de arquivo/aula/2_pandas/planilha/vendas.csv', sep=';')

planilha_vendas = planilha_vendas[['ID Cliente']]
planilha_cliente = planilha_cliente[['Primeiro Nome']]

planilha_cliente.rename({'Primeiro Nome': 'ID Cliente'})
print(planilha_vendas)
print(planilha_cliente)

# planilha_vendas = planilha_vendas.merge(planilha_cliente, on='ID Cliente')
# print(planilha_vendas)
