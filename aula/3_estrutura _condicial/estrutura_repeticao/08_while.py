from random import randint

capacidade_maxima = 100
balde = 0

while balde <= capacidade_maxima:
    volume__copo = randint(50, 100)
    print(f'Copo enchido: {volume__copo}mls')
    balde += volume__copo
    print(f'Volume do balde: {balde}mls')