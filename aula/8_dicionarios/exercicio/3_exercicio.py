### Exercício 3
'''Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos. 
calcule o novo valor dos produtos com base nas seguintes regras:
- Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
- Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%
- Preços acima de 2.000 vão ter reajuste de 20%'''

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}

for produto in precos:
    precos_produto = precos[produto]
    if precos_produto <= 1000:
        novo_preco = precos_produto * 1.1
    elif precos_produto <= 2000:
        novo_preco = precos_produto * 1.15
    else:
        precos_produto > 200
    print(f'{produto} {novo_preco:.2f}') 


