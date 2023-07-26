comprimento = float(input('Largura da parede: '))
altura = float(input('Largura da parede: '))

area = altura * comprimento
tinta = area / 2

print(f"Sua parede tem {comprimento} x {altura} e a sua área é de {area:.3f}m²")
print(f"Para pintar essa parede, você precisará de {tinta:.3f}L de tinta")