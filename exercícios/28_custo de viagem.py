a = int(input("Qual a distância: "))

if a <= 200:
   a = a * 0.50
   print("\33[0;31mATENÇÃO:\33[m Viagem abaixo de 200km o custo será de 0,50 centavos por Km")
   print(f"O valor da viagem é de {a:.2f} Reais")
else:
   a = a * 0.45
   print("\33[0;31mATENÇÃO:\33[m Viagem acima de 200km o custo será de 0,45 centavos por Km")
   print(F"Valor da viagem é de {a} Reais")
