class MyClass:
    class_attribute = 0

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

# Atributo de classe é acessado pela classe diretamente
print(MyClass.class_attribute)  # Saída: 0

# Alterando o valor do atributo de classe
MyClass.class_attribute = 1
MyClass.class_attribute = 2

# Criando instâncias
obj1 = MyClass(10)
obj2 = MyClass(20)

# Acessando o atributo de classe através das instâncias
print(obj1.class_attribute)  # Saída: 1
print(obj2.class_attribute)  # Saída: 1

# Acessando o atributo de instância
print(obj1.instance_attribute)  # Saída: 10
print(obj2.instance_attribute)  # Saída: 20