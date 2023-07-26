from datetime import date
ano = int(input("Qual o ano: "))
if ano == 0:
   ano = date.today().year # verificar o ano atual da máquina
   print(ano)
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print(f'O ano {ano} é bissexto')
else:
   print(f"O ano {ano} não é bissexto")
