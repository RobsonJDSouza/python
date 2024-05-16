# import requests

# username = 'Robson'

# url = f'https://api.github.com/users/{username}'

# response = requests.get(url)
# data = response.json()

# if response.status_code == 200:
#     # print(data)
#     print(data['login'])
#     print(data['id'])


import requests
import csv

# file deepcode ignore NoHardcodedCredentials: <please specify a reason of ignoring this>
username = 'Robson'

url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    with open('response_git.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'ID'])
        writer.writerow([data['login'], data['id']])
    print("Dados salvos em github_data.csv")
else:
    print("Erro ao obter dados do GitHub")

# with open('response_git.csv', mode='w', newline='') as file::
# Esta linha abre um arquivo CSV chamado 'response_git.csv' no modo de escrita ('w'). Se o arquivo não existir, ele será criado. O parâmetro newline='' é usado para garantir que não haja adição de linhas em branco entre as linhas gravadas no arquivo CSV.

# A declaração with é usada aqui para garantir que o arquivo seja fechado automaticamente após a conclusão das operações dentro do bloco with. Isso é útil para garantir que os recursos sejam liberados corretamente, mesmo em caso de exceção.

# writer = csv.writer(file):
# Aqui, criamos um objeto csv.writer chamado writer, que nos permitirá escrever no arquivo CSV especificado (file).


# writer.writerow(['Username', 'ID']):
# Este comando escreve uma linha no arquivo CSV. No caso, estamos escrevendo os cabeçalhos das colunas 'Username' e 'ID'.

# writer.writerow([data['login'], data['id']]):
# Aqui, escrevemos uma linha no arquivo CSV contendo os dados obtidos da resposta da solicitação à API do GitHub.
# data['login'] fornece o nome de usuário obtido da resposta JSON.
# data['id'] fornece o ID do usuário obtido da resposta JSON.