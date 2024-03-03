'''
CAPTURAR EXCEÇÕES 

Try: Código a ser testado.
Except: Execute esse código caso o erro ocorrer.
Else: Execute esse código caso nenhum erro ocoorrer.
Finally: Sempre execute esse código.
'''

def dividindo_dois_numeros(divisor, dividendo):
    return divisor/dividendo

try: 
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    resultado = dividindo_dois_numeros(numero_1, numero_2)


except NameError:
    print('Verificar os nomes das variáveis') 

except (TypeError, IndentationError):  #Tratar duas exceções juntas
    print('Erro de tipo ou indentação')

except ZeroDivisionError as execao:  #podemos dar uma Alias para veerificar excelção ocorreu.
    print(f'Não pode fazer divisão por zero {execao}')
    
else:
    print(f'Valor da divisão é {resultado}')

finally:
    print('Obrigado por usar o nosso serviço')

