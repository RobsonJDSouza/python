

nota = []
while True:
    nota_valida = int(input('Passa uma nota de 0 a 10. '))
    if nota_valida < 11:
        nota.append(nota_valida)
    else:
        print('Nota invalida digitada')
        break
print(f'Suas notas digitadas foram {nota}')
