from main import Automovel

VALOR_PEDAGIO_MOTO = 2.90
VALOR_KM_RODADO_MOTO = 1.5

class Moto(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi uma moto")

    def gerar_valor_fatura(self, numero_pedagio, km_rodado ):
        self.valor_fatura = (numero_pedagio * VALOR_PEDAGIO_MOTO) + (VALOR_KM_RODADO_MOTO * km_rodado)
        print(f'Valor da fatura moto: {self.valor_fatura}')
        

