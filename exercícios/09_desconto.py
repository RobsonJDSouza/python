'''
Escreva um programa
  Desconto de uma valor
'''
valor = float(input('Valor da compra: '))
porcentagem = int(input('Valor do desconto: '))

desconto = (valor * porcentagem)/100
desconto_real = valor - desconto

print(f"Com {porcentagem}% de desconto, você irá pagar {desconto_real:.2f}R$ na compra")