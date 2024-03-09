# Em Python, um atributo de classe é uma variável associada à classe em vez de a uma instância específica dessa classe. Isso significa que o valor do atributo de classe é compartilhado entre todas as instâncias dessa classe. Aqui está um exemplo:

# class MyClass:
#     class_attribute = 0

#     def __init__(self, instance_attribute):
#         self.instance_attribute = instance_attribute

# # Atributo de classe é acessado pela classe diretamente
# print(MyClass.class_attribute)  # Saída: 0

# # Alterando o valor do atributo de classe
# MyClass.class_attribute = 1
# MyClass.class_attribute = 2

# # Criando instâncias
# obj1 = MyClass(10)
# obj2 = MyClass(20)

# # Acessando o atributo de classe através das instâncias
# print(obj1.class_attribute)  # Saída: 1
# print(obj2.class_attribute)  # Saída: 1

# Acessando o atributo de instância
# print(obj1.instance_attribute)  # Saída: 10
# print(obj2.instance_attribute)  # Saída: 20


class Carro:
    # Atributo de classe para contar o número de carros
    quantidade_carros = 0

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Carro.quantidade_carros += 1  # Incrementa a quantidade de carros toda vez que um novo objeto Carro é criado

# Criando algumas instâncias da classe Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")
carro3 = Carro("Ford", "Focus")

# Acessando o atributo de classe quantidade_carros usando a classe Carro
print("Quantidade total de carros:", Carro.quantidade_carros)  # Saída: 3

# quantidade_carros é um atributo de classe da classe Carro.
# Sempre que um novo objeto Carro é criado usando o método __init__, o atributo de classe quantidade_carros é incrementado.
# Podemos acessar o valor de quantidade_carros usando a classe Carro, e não uma instância específica, já que o atributo de classe é compartilhado entre todas as instâncias.
# Isso ilustra como os atributos de classe podem ser usados para armazenar dados que são compartilhados por todas as instâncias de uma classe em Python.
