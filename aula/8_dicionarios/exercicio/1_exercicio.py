
### Exercício 1
'''Crie um sistema de consulta de preços
Seu sistema deve:
- Pedir para o usuário o nome de um produto
- Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
       - Ex: O produto celular custa R$1500
- Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente'''

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

usuario = input('Qual o nome do produto? ')
usuario = usuario.lower()
if usuario in precos:
    precos = precos[usuario]
    print(f'O produto {usuario} custa R${precos}')
else:
    print('Usuário tentar novamente')
