def busqueda_lineal_lordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    lista_ord = sorted(lista)
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista_ord): # recorremos la lista
        if z == e and e > lista_ord[i+1]:
            break    # y salimos del ciclo
    return pos

busq = busqueda_lineal_lordenada([1,2,4,5,5,5,6,3,5,3],3)
print(busq)
