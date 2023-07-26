a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

#verificando o maior número
if a>b and a > c:
   maior = a
elif b > a and b > c:
   maior = b
elif c > a and c > b:
   maior = c

#analisando o meno número
if a < b and a < c:
   menor = a
elif b < a and b < c:
   menor = b
elif c < a and c < b:
   menor = c

#resultado
print(f"O menor número foi: {menor}\nO maior número foi: {maior}")

#Posspível erro: O usuário digitar o mesmo número. O código irá quebrar