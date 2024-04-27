def filtrar_provedor(lista, pedaco):
    lista_filtrada = []
    for item in lista:
        if pedaco in item:
            lista_filtrada.append(item)
    return lista_filtrada
    



lista_textos = ['lira@gmail.com', 'zezinho@hotmail.com', 'joao@gmail.com', 'alon@gmail.com']

lista = filtrar_provedor(lista_textos, 'hotmail')
print(lista)



