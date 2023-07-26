from datetime import date
nascimento = int(input("Ano de nascimento "))

data_atual = date.today().year
a = data_atual - nascimento

if a > 18:
   print(f"Seu período de alistamento já passou  por {a - 18} anos")
else:
   print(f"Faltam {18 - a} anos para se alistar ")