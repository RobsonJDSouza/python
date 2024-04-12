'''
Classe - É um model para construção de um objeto

    Atributo == Que coisas eu tenho? 
    Metodo == Que coisas eu faço 

Atributos: 
São variáveis que pertencem à classe e que descrevem as características dos objetos que serão criados a partir dela. Por exemplo, em uma classe Carro, os atributos podem incluir cor, modelo, ano, etc.

Métodos: 
São funções definidas dentro de uma classe e que podem ser chamadas nos objetos criados a partir dessa classe. Eles representam os comportamentos associados aos objetos da classe. Por exemplo, uma classe Carro pode ter métodos como ligar(), acelerar(), frear(), etc.

Objetos: 
São instâncias de uma classe. Quando uma classe é instanciada, isto é, quando um objeto é criado a partir dela, o objeto adquire as características definidas pelos atributos da classe e pode utilizar os métodos associados.

Por exemplo, vamos criar uma classe simples em Python chamada Pessoa que tem atributos para o nome e a idade, e um método para imprimir uma saudação com o nome da pessoa:

'''
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
    def saudacao(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

'''
Aqui estão alguns conceitos importantes no exemplo acima:

__init__:
É um método especial em Python chamado de construtor. Ele é chamado automaticamente quando um novo objeto da classe é criado. É usado para inicializar os atributos do objeto.

self: 
É uma referência ao próprio objeto. Ele é usado para acessar os atributos e métodos do objeto dentro da classe.

nome e idade: 
São os atributos da classe Pessoa.

saudacao: 
É um método da classe Pessoa que imprime uma saudação com o nome e a idade da pessoa.
'''

# Para criar um objeto da classe Pessoa e chamar o método saudacao, fazemos o seguinte:

# Criando um objeto da classe Pessoa
p1 = Pessoa('Robson', 40)
# Chamando o método saudacao
p1.saudacao()


# PILARES DA POO
# - Encapsulamento - Isolar/esconder dados em Classes, evitando acesso externo
# - Abstração - Características que o usuário não precisa saber
# - Herança - É o pilar da POO que permite que Classes derivem de outras Classes para aproveitar e reutilizar código.
# - Polimorfismo - Caracteristica que métodos possuem de ssumir várias(poli) formas(morfismo)


# Observaçõe da aula
#  @ - anotetion
# Caso tenhamos um getter, teremos um setter. Caso não tenhamos, diremos que não queremos a modificação ex CPF
