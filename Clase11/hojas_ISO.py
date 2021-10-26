def medidas_hoja_A(n):
    '''
    Calcula las medidas de una hoja de papel A
    '''
    if n == 0:
        ancho = 841
        largo = 1189
        return ancho, largo
    else:
        ancho, largo = medidas_hoja_A(n-1)
        ancho_nuevo = int(largo/2)
        largo_nuevo = ancho
        return ancho_nuevo, largo_nuevo
