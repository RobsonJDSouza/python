r1 = float(input("Primeiro número: "))
r2 = float(input("Segundo número: "))
r3 = float(input("Terceiro número: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print(f"Os números digitados podem forma im triangulo")
else:
   print(f"Os números gigitados não podem formar um triangulo")
