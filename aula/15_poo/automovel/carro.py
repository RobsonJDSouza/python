from main import Automovel
from time import sleep
from random import randint

VALOR_PEDAGIO_CARRO = 5.90
VALOR_KM_RODADO_CARRO = 1.5

class Carro(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Carro,  self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi um carro")

    def gerar_valor_fatura(self, numero_pedagio, km_rodado ):
        self.valor_fatura = (numero_pedagio * VALOR_PEDAGIO_CARRO) + (VALOR_KM_RODADO_CARRO * km_rodado)
        print(f'Valor da fatura carro: R${self.valor_fatura:.2f}')
        

fiesta = Carro("Ford", "fiesta", False)
fiesta.alugar("Robson") #Chmando o método alugar carro

# simulando tempo que o carro ficou alugado.
sleep(randint(2,5))
fiesta.devolver_carro()
fiesta.gerar_valor_fatura(numero_pedagio= 10, km_rodado=300)
