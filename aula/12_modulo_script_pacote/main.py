
# 1º forma - Importar o módulo inteiro
# import matematica
# from matematica import * #Importa todas funções dentro do módulo

# resultado = matematica.soma(10, 3)
# print(f'O valor da soma é: {resultado}')
# print(matematica.subtracao(10, 3))



# 2º forma - Importar apenas a função
# from matematica import soma, subtracao

# print(soma(10, 3))
# print(subtracao(10, 3))



# 3º forma - Importar apenas a função com Alias
# from matematica import soma as funcao_de_soma
# from matematica import subtracao as funcao_de_subtrair

# print(funcao_de_soma(10, 3))
# print(funcao_de_subtrair(10, 3))



# 4º forma - Importar o pacote criado
# from operacoes.soma import soma_dois_numeros
# from operacoes.subtracao import subtraindo_dois_numeros

# print(soma_dois_numeros(10, 3))
# print(subtraindo_dois_numeros(10, 3))


# 4.1º forma - Importar o pacote criado com Alias
from operacoes.soma import soma_dois_numeros as soma
from operacoes.subtracao import subtraindo_dois_numeros as subtracao

print(soma(10, 3))
print(subtracao(10, 3))



