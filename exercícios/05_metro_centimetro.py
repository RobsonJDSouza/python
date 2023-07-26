'''
Escreva um programa
  Converta dentímetro e milímetro
'''
metro = float(input('Digite o valor em metros: '))

cent = metro *100
milim = metro * 1000

print('Você digitou {} Metros'.format(metro))
print('{} Metro e igual a {} Centímetro'.format(metro, cent))
print('{} Metro e igual a {} Milímetro'.format(metro, milim))