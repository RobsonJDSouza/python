# Adicionar, Remover e Modificar Itens no Dicionário

### Estrutura:

#- Adicionar itens:

'''
dicionario = {}

dicionario[chave] = valor

outra opção:

dicionario.update({chave: valor, chave: valor})
'''
# Add
dicionario = {}
dicionario['Robson'] = [39, 'Brasileiro']
print(dicionario)

# For
num_nomes = int(input('Quantos nomes você deseja adicionar? '))

for i in range(num_nomes):
    dicio = {}
    nome = input("Nome: ")
    if nome.lower() == 'pare':
        break
    idade = input("Idade: ")
    dicio[nome] = idade

print("Dicionário atualizado:", dicio)


# While
num_nomes = int(input('Quantos nomes você deseja adicionar? '))

contador = 0
while contador < num_nomes:
    nome = input("Nome: ")
    if nome.lower() == 'pare':
        break
    idade = input("Idade: ")
    dicio[nome] = idade
    contador += 1

print("Dicionário atualizado:", dicio)