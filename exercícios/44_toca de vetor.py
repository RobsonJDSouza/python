'''
Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

Entrada
A entrada contém 20 valores inteiros, positivos ou negativos.

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.
'''

posicao = 20
n = [0]*posicao
for i in range(posicao):
    n[i] = int(input())
final = 0
inicio = posicao - 1
while final < inicio:
    n[final], n[inicio] = n[inicio], n[final]
    final += 1
    inicio -=1
for i in range(posicao):
    print(f"N[{i}] = {n[i]}")

#posicao.reverse()