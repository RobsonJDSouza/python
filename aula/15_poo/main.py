class Celular:
    def __init__(self, fabricante, modelo, tela, armazenamento, memoria, camera, bateria, tela_ligada ) -> None:
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada

    def ligar_tela(self):
        self.tela_ligada = True

celular_android = Celular("Sansung", "S10", 6.25, 128, 4, 21, 3400, False)
celular_iphone = Celular(fabricante="Apple", modelo="iPhone 13 Pro", tela=6.25, armazenamento=128, memoria=4, camera=16, bateria=3400, tela_ligada= False)

celular_iphone.ligar_tela()

print(celular_iphone.tela_ligada)







'''
Class Pessoa:     
    def __init__(self, nome, cpf, salario, cargo):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo

    def calculaBonus(self):
        if self.cargo == "Gerente":
            bonus = self.salario * 0.3
        else:
            bonus = self.salario * 0.1
        return bonus

funcionario1 = Pessoa("Robson", "32699630845", "100000.00", "gerente") #isso é uma instância
bonus = funcionario1.calculaBonus()

print(bonus)
print(funcionario1.nome)
print(funcionario1.cpf)
print(f"R${funcionario1.salario:.2f})




class Pessoa:     
    def __init__(self, nome, cpf, salario, cargo):
        self.__nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo

    @property
    def nome(self):
        return self.__nome #atributo privado Colocamos dois underline
    
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

funcionario1 = Pessoa("Robson", "32699630845", "100000.00", "gerente")

print(funcionario1.nome)
funcionario1.nome Robson Souza


#Exercício proposto
Crie uma classe chamada "ContaBancaria" que represente uma conta bancária simples com as seguintes características:
Atributos: número da conta (int), titular da conta (string), saldo (float).
Esses atributos devem ser privados, e você deve fazer os getters e setters conforme necessário. Considere que o número da conta não pode ser alterado após a criação, mas titular e saldo sim.



class ContaBancaria:
    def __init__(self, id, nome, saldo):
        self.__id = str(id)
        self.__nome = str(nome)
        self.__saldo = float(saldo)

    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nomeNovo):
        self.__nome = nomeNovo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldoNovo):
        self.__saldo = saldoNovo
try:
    titular = ContaBancaria( "006455", "Robson", 1500.34) #ateção com os valores  para cálculo
    titular.nome = "Robson Souza"
    titular.saldo = 2458.03

    print(f"Número da conta: {titular.id}\nNome do titular da conta: {titular.nome}\nSaldo em conta CC: R${titular.saldo}")

except AttributeError:
        print("Erro de Atributo") 

'''