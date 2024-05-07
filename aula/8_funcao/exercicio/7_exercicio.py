'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\\$ 80,00 ou em galões de 3,6 litros, que custam R\\$ 25,00.'''

# Qual a área a ser pintada (m²): 50
# Quantidade de latas  1
# Preço:  80


##### Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações.

'''Dica: lembre dos operadores // e % mostrados em exercícios anteriores<br>
Dica1: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10.<br>
Dica2: numero % 10 vai te dar o resto da divisão do número por 10.'''

##### 1. Comprar apenas latas de 18 litros: (apenas latas inteiras)

# calcular quantas latas e quanto custa comprar a tinta
    # descobrir a area a ser pintada
    # calcular quantos litros de tinta o cliente precisa (area / 6)
    # quantas latas eu vou precisar para a quantidade de litros
        # calcular quantas latas (litros / 18)
        # se deu um número "quebrado" de latas
            # adiciona 1 lata
        # se não
            # dê a quantidade de latas
    # calcular o preço das latas (quantidade de latas * R$80)

def pegar_area_usuario():
    area = int(input("Qual a área a ser pintada (m²): "))
    return area

def calcular_litros_precisamos(area):
    litros = area / 6
    return litros
    
def calcular_latas(litros):
    latas = litros / 18
    if int(latas) != latas:
        latas = int(latas) + 1
    return latas

def calcular_preco(latas):
    preco = latas * 80
    return preco
    

area = pegar_area_usuario()
litros = calcular_litros_precisamos(area)
latas = calcular_latas(litros)
preco = calcular_preco(latas)


print("Quantidade de latas ", latas)
print("Preço: ", preco)


#2. Comprar apenas galões de 3,6 litros: (apenas galoes inteiros)

# calcular o preço e a quantidade de galoes para comprar
    # saber a área do cliente
area = int(input("Qual a área a ser pintada(m²): "))
litros_tinta = area / 6
                
if litros_tinta % 3.6 > 0:
    galoes = int(litros_tinta / 3.6) + 1
else:
    galoes = litros_tinta / 3.6
    # calcular o preço dos galoes -> quantidade de galoes * 25
preco = galoes * 25

print("Quantidade galões: ", galoes)
print("Preço: ", preco)



##### 3. Misturar latas e galões, de forma que o desperdício de tinta seja menor. Sempre arredonde os valores para cima, isto é, considere latas cheias.

'''O custo da lata é 80/18 = 4,44 R\\$/L

O custo do galão é 25/3,6 = 6,94 R\\$/L

A lata é mais econômica, então todas as latas inteiras que pudermos usar devemos comprar em latas. Se ficar faltando alguma coisa para completar devemos avaliar se é melhor comprar latas ou galões. Exemplo:

Se queremos comprar 90 litros. 5 latas dão exatamente 90 litros. Então devemos comprar tudo em latas.

Se queremos comprar 95 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.

Para os 5 litros faltantes precisamos de 2 galões que custam 50 reais no total. Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar 2 galões.

Se queremos comprar 107 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.

Para os 17 litros faltantes precisamos de 5 galões que custam 125 reais no total. Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar uma lata.

3 galões custam 75 reais, 4 galões custam 100 reais. Então, se for possível completar com até 3 galões escolhe-se galões. Qualquer quantidade maior que 3 galões, usa-se latas.

Podemos ir ao exercício:'''

# calcular o menor preço possível de latas e galoes para pintar uma parede
    # descobrir a área a ser pintada (pegar um input do usuário)
galoes = 0
latas = 0
area = int(input("Qual a área a ser pintada (m²):"))
    # calcular quantos litros vamos precisar (area / 6)
litros = area / 6
    # calcular quantas latas e galoes vamos precisar
        # calcular quantas latas inteiras vamos precisar
latas = int(litros / 18)
        # calcular quanto vai sobrar de litros de tinta
litros_faltam = litros % 18
        # se sobrar tinta:
            # quantos galoes vamos precisar para essa sobra    
if litros_faltam > 0:
        if litros_faltam % 3.6 > 0:
            galoes = int(litros_faltam / 3.6) + 1
        else:
            galoes = litros_faltam / 3.6
            
    # calcular o preço
        # qtde_latas_inteiras * 80
preco_latas = latas * 80
        # se qtde_galoes * 25 > 80:
            # preço anterior + 80
        # caso contrario
            # preco anterior + qtde_galoes * 25
preco_galoes = galoes * 25
if preco_galoes > 80:
    latas = latas + 1
    preco_latas = latas * 80
    galoes = 0
    preco_galoes = 0
            
preco_final = preco_latas + preco_galoes
print("Latas: ", latas)
print("Galoes: ", galoes)
print("Preço Final: ", preco_final)