
produtos = []
quantidades = []

while True: #loop infinito
    produto = input('Produto: ')
    if not produto:
        break #Mas com uma condição que para o Looping.
    quantidade = int(input('Quantidade '))
    if not quantidade:
        break
    produtos.append(produto)
    quantidades.append(quantidade)
    print(f'Você comprou {quantidade} {produto}')

print(f'{quantidades} {produtos}')
