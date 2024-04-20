
vendas = [20, 30, 9, 11]
nome = ['Robson', 'Ana', 'Sofia', 'Iris']
meta = 10
i = 0

# 1ª Possibilidade
while vendas[i] > meta:
    print(f'Vendedor(a) {nome[i]} bateu a meta. Total de vendas: {vendas[i]}')
    i += 1
    if vendas[i] < meta:
        print(f'Vendedor(a) {nome[i]} não bateu a meta. Total de venda: {vendas[i]}')

# 2ª Possibilidade
while i < len(vendas):
    if vendas[i] >= meta:
        print(f'Vendedor(a) {nome[i]} bateu a meta. Total de vendas: {vendas[i]}')
    else:
        print(f'Vendedor(a) {nome[i]} não bateu a meta. Total de venda: {vendas[i]}')
    i += 1
