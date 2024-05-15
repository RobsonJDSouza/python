## Resumo
'''
- É como se fosse uma tabela.
- As colunas funcionam "como chaves de dicionário"
- As linhas funcionam "como listas"
'''

import pandas as pd

vendas_df = pd.read_csv('11_manipulação de arquivo/aula/2_pandas/planilha/cadastro_rodutos.csv', sep=';')
print(vendas_df) 

#Uma lista com os valores da coluna_x (em formato dataframe, é um dataframe com 1 coluna só)
vendas_df['coluna_x'] 

#Cria um novo dataframe com as colunas coluna_x, coluna_y e coluna_z
vendas_df[['coluna_x', 'coluna_y', 'coluna_z']] 

#Pega até a linha de índice 3 do dataframe
#vendas_df[0] # NÃO FUNCIONA ASSIM PARA DATAFRAMES
vendas_df[:3] 

#Pega o item da 1ª linha da coluna coluna_x
vendas_df['coluna_x'][0] 

#Análise de Dados é você entender o que existe na sua base de dados
print(vendas_df.info())

