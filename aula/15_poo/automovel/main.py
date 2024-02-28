
VALOR_PEDAGIO_MOTO = 2.90

class Automovel:
    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente= ""
        print(f'Automóvel {self.montadora} {self.modelo} adquirido pela Locadora')


    def alugar(self, nome_cliente):
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f'O automóvel {self.montadora} {self.modelo} foi alugado pelo {self.nome_cliente}')

    def devolver_carro(self):
        self.alugado = False
        print(f'O automóvel {self.montadora} {self.modelo} foi devolvido pelo {self.nome_cliente}')
        self.nome_cliente = ""

    def gerar_valor_fatura(self, numero_pedagio, km_rodado):
        raise  NotImplementedError #Exceção. Quem herdar essa classe terar que implementar esse metodo 
    


