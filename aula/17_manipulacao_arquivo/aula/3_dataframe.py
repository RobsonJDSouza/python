## Resumo
'''É como se fosse uma tabela.
- As colunas funcionam "como chaves de dicionário"
- As linhas funcionam "como listas"'''

import pandas as pd

vendas_df = pd.read_csv('2.1_cadastro_rodutos.csv', sep=';')
print(vendas_df) 

vendas_df['coluna_x'] #Uma lista com os valores da coluna_x (em formato dataframe, é um dataframe com 1 coluna só)
#vendas_df[0] # NÃO FUNCIONA ASSIM PARA DATAFRAMES
vendas_df[:3] # pega até a linha de índice 3 do dataframe
vendas_df[['coluna_x', 'coluna_y', 'coluna_z']] #Cria um novo dataframe com as colunas coluna_x, coluna_y e coluna_z
vendas_df['coluna_x'][0] #Pega o item da 1ª linha da coluna coluna_x