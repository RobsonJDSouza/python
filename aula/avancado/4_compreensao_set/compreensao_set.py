
# Compreensão de set (set comprehension) em Python é uma construção que permite criar conjuntos de forma concisa e eficiente, semelhante à compreensão de lista e compreensão de dicionário. Ela segue uma sintaxe semelhante e pode ser usada para criar conjuntos a partir de iteráveis de maneira elegante./

# SINTAXE
# conjunto = {expressão for item in iterável}

class Pessoa:
    def __init__(self, nome, idade, cidade, genero):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.genero = genero
    
    #arrumando o retorno do objeto pessoas_com_r
    def __repr__(self) -> str:
        return f'Pessoa: {self.nome}'

pessoas =[
    Pessoa('Robson', 40, 'Osasco', 'M'),
    Pessoa('Ana', 42, 'Carapicuíba', 'F'),
    Pessoa('Sofia', 8, 'Itaquera', 'f'),
]

cidades = {pessoa.cidade for pessoa in pessoas}
pessoas_com_r = {pessoa for pessoa in pessoas if pessoa.nome[0]== 'R'}
pessoas_menor_40 = {pessoa for pessoa in pessoas if pessoa.idade < 41}
pessoas_sexo_f = {pessoa for pessoa in pessoas if pessoa.genero.upper() == 'F'}

print(cidades)
print(pessoas_com_r)
print(pessoas_menor_40)
print(pessoas_sexo_f)
