import pandas as pd
import matplotlib.pyplot as plt



'''
encoding='latin1'
encoding='ISO-8859-1'
encoding='utf-8'
encoding='cp1252
'''

# "r" antes do caminho do arquivo em Python significa "raw string" (cadeia de caracteres bruta). Ele indica que os caracteres especiais dentro da string não devem ser interpretados de forma especial. 
planilha_cliente = pd.read_csv(r'/home/robson.jose/Documentos/cursos/python/python/aula/11_manipulação de arquivo/aula/2_pandas/planilha/clientes.csv', sep=';', encoding='latin1')
# print(planilha_cliente)

quantidade_email = planilha_cliente['E-mail'].value_counts()
print(quantidade_email)
quantidade_email[:100].plot(figsize=(15,5))
plt.show()