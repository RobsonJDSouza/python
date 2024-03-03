def trata_texto(texto):
    return texto.replace("'","").strip()

cadastros = [
    "Rosbon, 40, robson'@gmail.com",
    "   Ana,  42, ana@hotmail.com",
    "Sofia,  8, sosorosa@google.com"
]

# resultado_trata_texto = []
# for cadastro in cadastros:
#     resultado_trata_texto.append(trata_texto(cadastro))
# print(resultado_trata_texto)


##Map
# resultado = list(map(trata_texto, cadastros))
# print(resultado)


##Lambda
# resultado = list(map(lambda texto:texto.replace("'","").strip(), cadastros))
# print(resultado)


##Filter
resultado = []

resultado_filter = list(filter(lambda cadastro: 'gmail' in cadastros,resultado))

print(resultado)

