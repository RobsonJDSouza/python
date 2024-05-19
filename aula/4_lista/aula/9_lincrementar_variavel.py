
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
lista = lista + ['ipad']
print(f'Incrementei {lista[2]} na lista {lista}')

#adicionando na soma a quantidade de 300 IPad 
vendas.append(300)
print(f'Incrementei {vendas[2]} na lista {vendas}')

#adicionando no fim do texto o Ipad
soma = sum(vendas)
email = f'Esse mês vendemos um total de {soma} produtos, sendo:\n{vendas[0]} unidades de {lista[0]}\n{vendas[1]} unidades de {lista[1]}'

print(email)

