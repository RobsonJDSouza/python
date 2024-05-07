'''
Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.

'''

def gorjeta ():
    conta = float(input("Digite o valor da conta: "))
    gorjeta_garcon = conta * 0.10    
    print(f"O garçon tem {gorjeta_garcon:.2f} R$ de gorjeta")

gorjeta()
    