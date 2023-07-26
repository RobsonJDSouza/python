nome = input("Digite algo: ").upper()

if "O" in nome:
    print(f"A letra 'O'aparece {nome.count('O')}x na palavra digitada ")
    print(f"Ela aparece pela primeira vez na posição {nome.find('O')+1}.")
    print(f"Ela aparece pela última vez na posição: {nome.rfind('O')+1}.")
else:
    print(f"Não temos a letra O na palavra {nome.capitalize()}")