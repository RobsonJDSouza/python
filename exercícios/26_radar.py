velocidade = int(input('Qual velocidade? '))
multa = (velocidade -30) * 7

if velocidade <= 30:
   print(" Está dentro da velocidade da via!")
else:
   print(f"Você tomou multa! O valor da multa é de R$ {multa:.2f}")
