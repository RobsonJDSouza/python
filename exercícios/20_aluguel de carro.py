dias = int(input('Quantos dias ficou com o carro? '))
km = int(input('Quantos quilômetros foi usado? '))

custo_diario = 60
km_rodado = 0.15
preco_pagar = km * km_rodado + dias * custo_diario

print(f"O Valor a pagar: R${preco_pagar:.2f} ")