# Exercício 2
# Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente

produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]

novo_produto = input('Qual produto devo adicionar na lista? ').lower()

if novo_produto in produtos:
    index_produto = produtos.index(novo_produto)
    preco_produto = precos[index_produto]
    print(f'O produto {novo_produto} já existe na lista e custa R${preco_produto}')
else:
    novo_preco = float(input('Qual é o preço do novo produto? '))
    produtos.append(novo_produto)
    precos.append(novo_preco)
    print(f'O novo produto foi adicionado: {produtos}')
    print(f'Os preços atualizados são: {precos}')
