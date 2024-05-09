# Adicionar, Remover e Modificar Itens no Dicionário

### Estrutura:

#- Adicionar itens:

'''
dicionario = {}

dicionario[chave] = valor

outra opção:

dicionario.update({chave: valor, chave: valor})
'''
dicio = {}

# Definindo o número de nomes que você quer adicionar
num_nomes = input('quantos nomes')

# Loop para adicionar os nomes e idades ao dicionário
for i in range(num_nomes):
    nome = input("Nome: ")
    idade = input("Idade: ")
    dicio[nome] = idade
    num_nomes += num_nomes
    if nome.lower() == 'pare':
        break

print("Dicionário atualizado:", dicio)