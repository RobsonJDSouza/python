# Condições no Python -> If

## Estrutura:

'''
if condição:
    o que fazer caso a condição seja verdadeira
'''

### Exemplo Real:

'''Digamos que você trabalha na Amazon (que tem centenas de milhares, se não milhões de produtos) e está analisando o resultado de vendas dos produtos.

Você precisa criar um programa que vai analisar o resultado de vendas dos produtos da Amazon em um mês. Para simplificar vamos pensar em um único produto: um Iphone.

Meta de Vendas do Iphone = 50.000 unidades
Quantidade vendida no Mês = 65.300 unidades

O seu programa deve avisar (usaremos o print por enquanto) caso o produto tenha batido a meta do mês. Então devemos fazer:
- Caso o produto tenha batido a meta, devemos exibir a mensagem: "Batemos a meta de vendas de Iphone, vendemos {} unidades" 
- Se ele não bateu a meta do mês, o seu programa não deve fazer nada'''

meta_mes = 50.000
qtde_mes = 65.300

if  meta_mes >= 50.00:
    print(f'Batemos a meta de vendas de Iphone. Vedido R${meta_mes} quantidade{qtde_mes}')
else:
    print('Não bateu a meta')