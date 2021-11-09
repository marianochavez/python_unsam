def ord_burbujeo(lista):
    # comp = 0
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            # comp += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista