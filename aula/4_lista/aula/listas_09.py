
# Alterações de Variáveis



'''
Estrutura:
- variavel = variavel + outro_valor

ou então

- variavel += outro_valor

Exemplo: vamos adicionar às variáveis criadas o Produto IPad, 500 vendas
'''


lista = ['mac', 'iphone']
vendas = [100, 200]
#adicionando IPad na lista


soma_vendas = 300
#adicionando na soma a quantidade de IPad


email = 'Esse mês vendemos um total de {} produtos, sendo:\n{} unidades de {}\n{} unidades de {}'.format(soma_vendas, vendas[0], lista[0], vendas[1], lista[1])
#adicionando no fim do texto o Ipad

print(email)