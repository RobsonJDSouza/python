#Python nao consegue ler um código dentro da string. Chamamos a funçao Eval  

numero1 = input('Digite um número: ')
numero2 = input('Digite um número: ')
print('Digite um operaçao:\n\t+ para soma\n\t- para subtraçao\n\t* para multipliaçao\n\t/ para divisao')

operacao = input('Digite um operador: ')

resultado = f'{numero1} {operacao} {numero2}'

# file deepcode ignore CodeInjection: <please specify a reason of ignoring this>
print (eval(resultado))
