#PROGRAMA DE CONCESSÃO DE APOSENTADORIA

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
sexo = (input('Qual o seu sexo? (M) ou (F) '))

if sexo.upper() == 'M':
    if int(idade) >= 72:
        print(f'{nome},\nVoce tem direito a aposentadoria')
    else:
        print(f'{nome},\nVocê não tem direito a aposentadoria. Faltam {72 - int(idade)}')

elif sexo.upper() == 'F':
    if int(idade) >= 62:
        print(f'{nome},\nVoce tem direito a aposentadoria')
    else:
        print(f'{nome},\nVocê não tem direito a aposentadoria. Faltam {72 - int(idade)}')

else:
    print('Digite os dados corretos')


