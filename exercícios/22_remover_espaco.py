nome = input("Digite algo: ").strip()
nome = nome.title()
if nome in "Robson":
    print(nome)
else:
    print(f"Não tem o nome Robson, mas tem o nome {nome}")