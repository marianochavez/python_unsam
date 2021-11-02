import random
import matplotlib.pyplot as plt


def generar_lista(N):
    lista = []
    for i in range(1, N):
        lista.append(random.randint(1, 1000))
    return lista


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comp_seleccion = 0

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p, comp_buscar = buscar_max(lista, 0, n)
        comp_seleccion += comp_buscar

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

    return comp_seleccion


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    comp_buscar_max = 0
    pos_max = a
    for i in range(a + 1, b + 1):
        comp_buscar_max += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, comp_buscar_max


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comp_insercion = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        comp_insercion += 1
        if lista[i + 1] < lista[i]:
            comp_reubicar = reubicar(lista, i + 1)
            comp_insercion += comp_reubicar

    return comp_insercion


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    comp_reubicar = 0
    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        comp_reubicar += 1
        lista[j] = lista[j - 1]
        j -= 1
    comp_reubicar += 1
    lista[j] = v
    return comp_reubicar


def ord_burbujeo(lista):
    comp_burbujeo = 0
    for j in range(1, len(lista)):
        for i in range(0, len(lista)-j):
            comp_burbujeo += 1
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return comp_burbujeo

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comp_merge_sort = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva, comp_merge = merge(izq, der)
        comp_merge_sort += comp_merge
    return lista_nueva, comp_merge_sort

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    lista1 = lista1[0]
    lista2 = lista2[0]
    comp_merge = 0
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        comp_merge += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comp_merge


def experimento(N, k):
    """Ejecuta k experimentos para N elementos.
       Devuelve una lista con los k resultados."""
    res_seleccion = 0
    res_insercion = 0
    res_burbujeo = 0
    res_merge_sort = 0
    for i in range(k):
        lista = generar_lista(N)
        res_seleccion += ord_seleccion(lista.copy())
        res_insercion += ord_insercion(lista.copy())
        res_burbujeo += ord_burbujeo(lista.copy())
        res_merge_sort += merge_sort(lista.copy())[1]
    return res_burbujeo/k, res_insercion/k, res_seleccion/k, res_merge_sort/k


def experimento_vectores(Nmax):
    """Ejecuta experimentos para N elementos desde 1 hasta Nmax.
       Devuelve una lista con los resultados."""
    comparaciones_seleccion = []
    comparaciones_insercion = []
    comparaciones_burbujeo = []
    comparaciones_merge_sort = []
    for N in range(1, Nmax + 1):
        res_burbujeo, res_insercion, res_seleccion, res_merge_sort = experimento(N, 100)
        comparaciones_seleccion.append(res_seleccion)
        comparaciones_insercion.append(res_insercion)
        comparaciones_burbujeo.append(res_burbujeo)
        comparaciones_merge_sort.append(res_merge_sort)
    return comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge_sort

n = 100
experimento_vect = experimento_vectores(n)
plt.plot(experimento_vect[0], label="Selección", color = "red")
plt.plot(experimento_vect[1], label="Inserción", color = "orange")
plt.plot(range(1, n+1), experimento_vect[2], label="Burbujeo", linestyle = "--", marker = 5, color = "black")
plt.plot(range(1, n+1), experimento_vect[3], label="Merge_Sort", color = "green")
plt.xlabel("Largo de la lista")
plt.ylabel("Comparaciones")
plt.axis([0,n,0,1200])
plt.legend()
plt.show()