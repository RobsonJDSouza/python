## 1. Function para Cálculo de Carga Tributária
'''Imagine que você trabalha no setor contábil de uma grande empresa de Varejo. 

Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto, dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.'''

preco = 1500
custo = 400
lucro = 785

def calcular_tributo(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto / preco


valor = calcular_tributo(25, 4, 4)
print(f'A carga tributária foi de {valor:.1%} valor')