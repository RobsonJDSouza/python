import base64

with open("./logo.png", "rb") as arquivo:
    arquivo_b64 = base64.b64decode(arquivo.read())
print(arquivo_b64)
