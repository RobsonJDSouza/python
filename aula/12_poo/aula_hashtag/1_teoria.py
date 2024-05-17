
'''
Qual a vantagem da Orientação a Objeto?
Aproveitar o código sem precisar refazer/copiar tudo


PILARES DA POO
Herança - É o pilar da POO que permite que Classes derivem de outras Classes para aproveitar e reutilizar código.
Encapsulamento - Isolar/esconder dados em Classes, evitando acesso externo - Proteção a mudanças indesejadas (ex: TV – você não pode desligar a tv no botão de mudar o volume)
Abstração - Características que o usuário não precisa saber
Polimorfismo - Caracteristica que métodos possuem de asumir várias(poli) formas(morfismo) - ex: Animais -> Gatos x Cachorros

Atributos: 
São variáveis que pertencem à classe e que descrevem as características dos objetos que serão criados a partir dela. Por exemplo, em uma classe Carro, os atributos podem incluir cor, modelo, ano, etc.

Métodos: 
São funções definidas dentro de uma classe e que podem ser chamadas nos objetos criados a partir dessa classe. Eles representam os comportamentos associados aos objetos da classe. Por exemplo, uma classe Carro pode ter métodos como ligar(), acelerar(), frear(), etc.

Objetos: 
São instâncias de uma classe. Quando uma classe é instanciada, isto é, quando um objeto é criado a partir dela, o objeto adquire as características definidas pelos atributos da classe e pode utilizar os métodos associados.

__init__:
É um método especial em Python chamado de construtor. Ele é chamado automaticamente quando um novo objeto da classe é criado. É usado para inicializar os atributos do objeto.

self: 
É uma referência ao próprio objeto. Ele é usado para acessar os atributos e métodos do objeto dentro da classe.

'''

# Por exemplo, vamos criar uma classe simples em Python chamada Pessoa que tem atributos para o nome e a idade, e um método para imprimir uma saudação com o nome da pessoa:

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
    def saudacao(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')


robson = Pessoa('Robson', 39)

print(robson.saudacao())