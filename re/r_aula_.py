for numero in range (1,11):
    print (numero)

numero = int(input ()) 
for i in range(1, numero + 1):
    if i % 2 != 0:
        print (i)

for i in range (1,numero+1, 2):
    print(1)

while entrada < 0:
    entrada = int (input("escreva um nº positivo"))
print(f"{entrada} é positivo")

numero = 1
while numero < 11:
    print (numero)
    numero = numero +1

'''
Variável lado direito
Expressões no lado esquerdo
'''

'''
==========================
   Aula Lista e Tuplas
==========================

tupla = ("Robson", "Ana", "Sofia")
lista = ["Robson", "Ana", "Sofia"]
'''

'''
lista = ["Robson", "Ana", "Sofia"]
print(lista[2]) #trazer uma posição
lista.append("Iris") #acrescentar informação na lista
lista[0] = "Robsu" #mudar o dado da posição
lista.pop() # remover a últiima posição
lista.remove(lista[1]) #remove uma posição
print(lista)
'''

'''
lista = ["Robson", "Ana", "Sofia"]
for nome in lista:
    print(nome)
'''

'''
lista = ["Robson", "Ana", "Sofia"]
for p, nome in enumerate(lista):
    print(f"Posição {p} nome {nome}")
'''
'''
raio = float(input())

n = 3.14159
area = n * (raio**2)

print(f"A={area:.4f}")

m1=float(input())
m2=float(input())
pm1 =3.5
pm2 =7.5
media1 = m1*pm1
media2 = m2*pm2
media= (media1+media2)/11
print(f"MEDIA = {media:.5f}")


Salário com Bônus
nome=str(input())
salario=float(input())
vendas=float(input())
vendas = vendas*0.15
total=salario+vendas
print(total)


'''

a = 'jeferson'
b = []
c = 0
for r in range(len(a)):
    if a[r] == 'e':
        b.append(r)
        c = len(b)
print(c) 

#########################################################
valor_recebido = input()
valores = [int(x) for x in valor_recebido.split(" ")]

a = valores[0]
b = valores[1]

teste = a + b

if teste < 20:
    print('menor')
else:
    print('maior')