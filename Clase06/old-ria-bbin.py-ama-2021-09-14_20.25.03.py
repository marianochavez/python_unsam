def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos,comps

def donde_insertar(lista, x):
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2

        if lista[len(lista)-1] < x: # el ultimo elemento de la lista es menor a x
            pos = len(lista)
            lista.append(x)
            print(lista)
            return pos

        if medio == izq and medio == der:
            if lista[medio] == x:
                pos = medio
                lista.insert(pos,x)
                print(lista)
                return pos

            else:
                if lista[medio] > x:
                    pos = medio
                    lista.insert(pos,x)
                    print(lista)
                else:
                    pos = medio+1
                    lista.insert(pos,x)
                    print(lista)
                return pos

        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

def insertar(lista,x):
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2

        if lista[len(lista)-1] < x: # el ultimo elemento de la lista es menor a x
            pos = len(lista)
            lista.append(x)
            print(lista)
            return pos

        if medio == izq and medio == der:
            if lista[medio] == x:
                pos = medio
                lista.insert(pos,x)
                print(lista)
                return pos

            else:
                if lista[medio] > x:
                    pos = medio
                    lista.insert(pos,x)
                    print(lista)
                else:
                    pos = medio+1
                    lista.insert(pos,x)
                    print(lista)
                return pos

        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

# pos = donde_insertar([0,1,4,7,8,9],5)
# print(pos)
