## 1. Criando um mini sistema de controle de estoque

'''- Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
- Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto, o time deve ser avisado (print) para fazer um novo pedido daquele produto.
- Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:

- alimentos -> Estoque mínimo: 50
- bebidas -> Estoque mínimo: 75
- limpeza -> Estoque mínimo: 30

Para isso vamos criar um programa que pede 3 inputs do usuário: nome do produto, categoria e quantidade atual em estoque.

Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"

Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem.<br>
Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.

Obs: lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.<br>
Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo de preencher corretamente.'''

# - alimentos -> Estoque mínimo: 50
# - bebidas -> Estoque mínimo: 75
# - limpeza -> Estoque mínimo: 30


produto = input('Qual produto? ') 
categoria = input('Qual categoria? ')
quantidade = input('Qual a quantidade? ')

if produto and categoria and quantidade:
    quantidade = int(quantidade)
    if categoria == 'bebida':
        if quantidade < 75:
            print(f'O seu estoque de {produto} está abaixo')
    elif categoria == 'limpeza':
        if quantidade < 30:
            print(f'O seu estoque de {produto} está abaixo')
    else:
        if quantidade < 50:
            print(f'Solicitar {produto} à equipe de compras, temos apenas {quantidade} unidades em estoque')
else:
    print('Preencha todas as informações')
