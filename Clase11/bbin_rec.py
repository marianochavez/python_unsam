def bbinaria_rec(lista, e):
    """	Busqueda binaria de un elemento. Devuelve true
    si el elemento esta en la lista, false en caso contrario.
    """
    if len(lista) == 0:
        return False
    elif len(lista) == 1:
        return lista[0] == e
    else:
        mitad = len(lista) // 2
        if lista[mitad] == e:
            return True
        else:
            if e < lista[mitad]:
                return bbinaria_rec(lista[:mitad], e)
            else:
                return bbinaria_rec(lista[mitad:], e)
