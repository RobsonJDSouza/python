print('\nPiramide Normal')
for i in range(5):
    x = ' *'
    x = x*i
    print(f'{x:^10}')


print('\nPiramide invertida')
for i in range(5):
    x = ' *'
    x = x*(5-i)
    print(f'{x:^10}')

print('\nPiramide começando na esquerda')
for i in range(5):
    x = ' *'
    x = x*i
    print(f'{x:<10}')


print('\nPiramide começando na esquerda')
for i in range(5):
    x = ' *'
    x = x*i
    print(f'{x:>10}')