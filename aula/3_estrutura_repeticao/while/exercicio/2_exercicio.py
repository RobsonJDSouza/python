
compra = []
print('Vocẽ pode parar a compra digitando Não')
venda = input('Produto: ').lower()

while venda != 'não':
    compra.append(venda)
    venda = input('Produto ').lower()
    if venda == 'nao':
        print('\O/\O/\O/ ATENÇÃO \O/\O/\O/ - Digite o não com acento!!!')

print(f'Lita de produtos {compra}')

