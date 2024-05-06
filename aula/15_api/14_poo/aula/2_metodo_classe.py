# Em programação orientada a objetos, "métodos de classes" são funções ou procedimentos associados a uma classe em vez de a uma instância específica da classe. Eles são tipicamente invocados usando o nome da classe, em vez de uma instância da classe.


# Python: Em Python, os métodos de classe são definidos usando o decorador @classmethod. Eles recebem a própria classe como primeiro argumento, convencionalmente nomeado cls, em vez da instância (self). 

# Exemplo
# class MinhaClasse:
#     # decorador
#     @classmethod 
#     def metodo_de_classe(cls, arg1, arg2):
#         # faça algo com cls
#         pass

# # Você pode chamar um método de classe usando o nome da classe, assim:
# MinhaClasse.metodo_de_classe(arg1, arg2)


class Carro:
    quantidade_carros = 0  # Variável de classe para acompanhar o número de carros

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Carro.quantidade_carros += 1  # Incrementa a quantidade de carros toda vez que um novo objeto Carro é criado

    @classmethod
    def mostrar_quantidade(cls):
        print(f"Total de carros: {cls.quantidade_carros}")

# Criando alguns objetos Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")
carro3 = Carro("Ford", "Focus")

# Chamando o método de classe para mostrar a quantidade de carros
Carro.mostrar_quantidade()  # Saída: Total de carros: 3


# A classe Carro possui um método mostrar_quantidade() que é decorado com @classmethod. Este método acessa a variável de classe quantidade_carros para exibir o total de instâncias da classe Carro.
# Cada vez que um novo objeto Carro é criado no método __init__(), a variável de classe quantidade_carros é incrementada.
# Finalmente, o método de classe mostrar_quantidade() é chamado usando o nome da classe Carro, e ele exibe a quantidade total de carros criados.
# Esse é um exemplo simples de como os métodos de classe podem ser usados em Python para operar em variáveis de classe e executar ações que não dependem de instâncias específicas da classe.
