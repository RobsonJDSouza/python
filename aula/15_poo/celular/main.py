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






