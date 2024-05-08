#### 3. Faça um Programa que verifique o estado civil de uma pessoa. Se a letra digitada é "C" (Casado), "S" (Solteiro), "D" (Divorciado), "V" (Viúvo) ou "O" (outros). Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil, exemplo:



estado = input('Digite aqui: ').lower()

C = 'Casado'
S = 'Solteiro'
D = 'Divorciado'
V = 'Viúvo'
O = 'outros'

if 'c' and 's' and 'd' and 'v' and 'o':
    if estado == 'c':
        print(f'Vocẽ é um pessoa {C}')
    elif estado == 's':
        print(f'Vocẽ é um pessoa {S}')    
    elif estado == 'd':
        print(f'Vocẽ é um pessoa {D}') 
    elif estado == 'v':
        print(f'Vocẽ é um pessoa {V}')
    elif estado == 'o':
        print(f'Vocẽ é um pessoa {O}')
    else:
        print('Não digitou uma informação válida')