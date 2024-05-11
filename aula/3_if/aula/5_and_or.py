# Estrutura
'''
if condicao_1 and condicao_2:
    vai ser executado se as 2 condições forem verdadeiras ao mesmo tempo

outro caso:

if condicao_1 or condicao_2:
    vai ser executado se pelo menos uma das condições forem verdadeiras
'''

# Exemplo 1

'''
Vamos voltar ao exemplo de cálculo de meta de vendas dos funcionários. Muitas empresas atribuem bonificação do salário dos funcionários de acordo com o resultado do funcionário e também com o resultado da empresa como um todo.

Nesse caso, a regra funciona da seguinte forma:
- Se o funcionário vendeu mais do que a meta de vendas e a loja bateu a meta de vendas da loja, o funcionário ganha 3% do que ele vendeu em forma de bônus.
- Caso o funcionário tenha batido a meta de vendas individual dele, mas a loja não tenha batido a meta de vendas da loja como um todo, o funcionário não ganha bônus.
'''

meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 15000
vendas_loja = 0

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print('Bonus do funcionário foi de {}'.format(bonus))
else:
    print('Funcionário não ganhou bônus')



#Exemplo 2

'''
Agora vamos levar essa análise mais a fundo.
Nessa empresa, existe um outro caso também que garante que o funcionário ganhe um bônus, independente das vendas que ele fez naquele mês.

Todo mês os diretores da empresa fazem uma avaliação qualitativa de todos os funcionários. Nessa avaliação os diretores dão uma nota de 0 a 10 para cada funcionário. Se a nota do funcionário for 9 ou 10, ele também ganha o bônus de 3% do valor de vendas. (os bônus não são cumulativos)
'''

nota_funcionario = 5
meta_nota = 9

if nota_funcionario >= meta_nota or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja):
    bonus = 0.03 * vendas_funcionario
    print('Bonus do funcionario foi de {}'.format(bonus))
else:
    print('Funcionário não ganhou bônus')