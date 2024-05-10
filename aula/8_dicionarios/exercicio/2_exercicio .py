### Exercício 2

'''
Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto
<br>Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
<br>Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado'''

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

produto_procurado = input('Qual o nome do produto? ')
usuario = produto_procurado.lower()
if usuario in precos:
    precos = precos[produto_procurado]
    print(f'O produto {usuario} custa R${precos}')

elif not produto_procurado in precos:
    quer = input(f'O produto {produto_procurado} não está cadastrado. Você quer cadastrá-lo? S/N').lower()
    if quer == 's':
        novo_produto = input('Nome do produto: ')
        novo_estoque = int(input('Quantidade do estoque '))
        precos[novo_produto] = novo_estoque
        print(precos)
    else:
        print(f'OK. Sua lista é: \n {precos}')
    
