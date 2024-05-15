import pandas as pd

vendas_df = pd.read_csv('11_manipulação de arquivo/aula/2_pandas/planilha/cadastro_rodutos.csv', sep=';')
print(vendas_df) 

#Análise de Dados é você entender o que existe na sua base de dados
print(vendas_df.info())

# #Criar uma lista
lista_marca = vendas_df['Nome da Marca']
print(lista_marca)

# Criar uma lista das colunas
colunas = ['Nome da Marca', 'Custo Unitario', 'Preco Unitario']
nova_lista = vendas_df[colunas]
print(nova_lista)