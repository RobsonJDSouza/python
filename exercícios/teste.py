'''
dic = {
    "nome": "Robson",
    "idade": 38,
    "cor": "Moreno"
}

dic["cabelo"] = "preto"
dic["nasc"] = 1984

print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
dic.update({"nasc" : 2000})
dic.update({"nome" : "Ana"})
print(dic)
'''
class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
p1 = Pessoa("robson")
print(p1.nome)