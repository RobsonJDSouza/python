numero = int(input("Digite um número "))
print('''Escolha um número!
[1] = Binário
[2] = Octal
[3] = Hexadecimal
''')
opcao = int(input("Escolha a sua opção "))

if opcao == 1:
   print(f"Binário: {bin(numero)}")
elif opcao == 2:
   print(f"Octodecimal: {oct(numero)}")
elif opcao == 3:
   print(f"Hexadecimal: {hex(numero)}")
else:
   print("Não digitou uma opção válida")