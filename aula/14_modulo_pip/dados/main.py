import base64

with open("./logo.png", "rb") as arquivo:
    arquivo_base64 = base64.b64decode(arquivo)
print(arquivo_base64)