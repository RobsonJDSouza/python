# Listas de Listas

### Estrutura:

'''
Cada item de uma lista pode ser qualquer tipo de variável. Inclusive, uma lista.
Quando dentro de uma lista temos cada item como sendo uma outra lista, temos uma "nested list", ou seja, uma lista de listas.
Todas as regras de lista e tudo que vimos até agora funciona exatamente igual, mas vamos ver como isso funciona na prática
'''

vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]

'''- Quanto João vendeu de IPad?'''
print(f'O Vendedor {vendedores[1]} vendeu {vendas[1][0]} unidades do {produtos[0]}.')

'''- Quanto Diego vendeu de IPhone'''
print(f'O Vendedor {vendedores[2]} vendeu {vendas[2][0]} unidades do {produtos[1]}.')

'''- Qual o total de vendas de IPhone?'''
vendas_iphone = vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1]
print(f'O total de vendas do {produtos[1]} foi de: R${vendas_iphone}')


"""- E se Lira na verdade fez apenas 50 vendas de IPhone, como eu modifico na minha lista o valor de vendas dele?"""
vendas[0][1] = 50
print(f'O valor real do vendedor {vendedores[0]} em vendas de {produtos[1]} foi de: R${vendas[0][1]}')


"""- E se agora eu tenho um novo produto 'mac', como eu adiciono as vendas em cada um dos vendedores?"""
produtos.append('mac')
vendas_mac = [0, 0]
vendas.append(vendas_mac)

print(f'Acrescentado o produto {produtos[2]} com os valores {vendas[4]}')

