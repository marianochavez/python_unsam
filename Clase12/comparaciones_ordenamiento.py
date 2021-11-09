import numpy as np
import matplotlib.pyplot as plt
import random


def generar_lista(N):
    lista = []
    for i in range(1, N):
        lista.append(random.randint(1, 1000))
    return lista


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    # comparaciones
    comps = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p, c = buscar_max(lista, 0, n)

        # guardo las comparaciones
        comps += c

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

    return comps


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a

    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i

    # comparaciones
    comps = b-a

    return pos_max, comps


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # comparaciones
    comps = 0

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]

        if lista[i + 1] < lista[i]:
            comps += reubicar(lista, i + 1)
        else:
            comps += 1
        # print("DEBUG: ", lista)

    return comps


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    # comparaciones
    comps = 0

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p

    comps += 1
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        comps += 1

    lista[j] = v

    return comps


def ord_burbujeo(lista):
    """Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    lenLista = len(lista)
    # comparaciones
    comps = 0

    # recorro los elementos de la lista
    for i in range(lenLista):

        # Como el ultimo j de cada iteracion i queda ordenado fijo al final, en cada vuelta de i ordeno
        # los valores de la lista sin tener en cuenta el ultimo valor.
        for j in range((lenLista-i)-1):
            comps += 1
            # comparo dos elementos contiguos de la lista
            # si el orden es el adecuado los deja como están, si no, los intercambio.
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return comps


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
        comps = 0
    else:
        medio = len(lista) // 2
        izq, c_izq = merge_sort(lista[:medio])
        der, c_der = merge_sort(lista[medio:])
        lista_nueva, c_merge = merge(izq, der)

        comps = c_izq + c_der + c_merge
    return lista_nueva, comps


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comps = 0

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
            comps += 1
        else:
            resultado.append(lista2[j])
            j += 1
            comps += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comps


def experimento(N, k):
    '''A partir de un largo de lista (N) y cierta cantidad de iteraciones (k) devuelve el promedio de las comparaciones
    de los algoritmos de ordenamiento.
    pre: N, k enteros positivos
    post: regresa una tupla con los promedios de cada comparacion
    '''
    comps_burb = 0.0
    comps_ins = 0.0
    comps_sel = 0.0

    for _ in range(k):
        lista = generar_lista(N)
        comps_burb += ord_burbujeo(lista.copy())
        comps_ins += ord_insercion(lista.copy())
        comps_sel += ord_seleccion(lista.copy())

    return comps_burb/k, comps_ins/k, comps_sel/k


def experimento_vectores(Nmax):
    '''Calcula la cantidad de comparaciones realizadas por cada método de ordenamiento
    para listas de longitud 1 a Nmax, y grafica los resultados.
    pre: Nmax entero positivo
    post: grafica las comparaciones realizadas por cada método de ordenamiento
    '''
    # array cargado con longitudes de listas entre 1 y Nmax
    largoLista = np.arange(Nmax) + 1

    comparaciones_seleccion = np.zeros(Nmax)
    comparaciones_insercion = np.zeros(Nmax)
    comparaciones_burbujeo = np.zeros(Nmax)
    comparaciones_merge = np.zeros(Nmax)

    for i, n in enumerate(largoLista):
        lista = generar_lista(n)
        comparaciones_seleccion[i] = ord_seleccion(lista.copy())
        comparaciones_insercion[i] = ord_insercion(lista.copy())
        comparaciones_burbujeo[i] = ord_burbujeo(lista.copy())
        comparaciones_merge[i] = merge_sort(lista.copy())[1]

    plt.plot(comparaciones_seleccion, c='blue', label='Ord. Secuencial')
    plt.plot(comparaciones_insercion, c='green', label='Ord. Inserción')
    plt.plot(comparaciones_burbujeo, c='red',
             linestyle='dashed', label='Ord. Burbujeo')
    plt.plot(comparaciones_merge, c='orange', label='Merge Sort')
    plt.ylabel("Comparaciones")
    plt.xlabel("Longitud de lista")
    plt.title("Cantidad de comparaciones de cada método")
    plt.legend()
    plt.show()
