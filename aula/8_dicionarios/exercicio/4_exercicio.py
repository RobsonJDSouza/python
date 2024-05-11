# Exercício 4

''' Edite o programa antigo para ter os 2 dicionários, o de preços originais e o de novos preços
   Em seguida calcule o valor total de reajuste em R$ que teve entre a lista de produtos original e a lista final'''


precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
novos_precos = {}
for produto in precos:
    precos_produto = precos[produto]
    if precos_produto <= 1000:
        novo_preco = precos_produto * 1.1
    elif precos_produto <= 2000:
        novo_preco = precos_produto * 1.15
    else:
        precos_produto > 200
    print(f'{produto} {novo_preco:.2f}') 
    novos_precos[produto] = novo_preco
    precos_sem_ajuste = sum(precos.values())
    precos_com_ajuste = sum(novos_precos.values())
    ajuste = precos_sem_ajuste - precos_com_ajuste
    print(f'valor do preço: {ajuste}')