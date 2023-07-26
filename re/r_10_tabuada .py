while True:
    tabuada = int(input())
    if tabuada < 0:
        break
        print('Tabuada do número',tabuada)
    for x in range(1,11):  
        print(tabuada, 'x', x, '=', (tabuada*x))
print('Digitou número menor que zero!!')