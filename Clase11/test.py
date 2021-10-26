def fib(n):
    """Precondición: n >= 0.
       Devuelve: el número de Fibonacci número n."""
    if n == 0 or n == 1:
        return n
    ant2 = 0
    ant1 = 1
    for i in range(2, n + 1):
        fibn = ant1 + ant2
        ant2 = ant1
        ant1 = fibn
    return fibn

fib(5)

def maximo(lista, debug_extra_str=''):
    if len(lista) == 1:
        res = lista[0]
        print(f'{debug_extra_str}En el caso base')
    else:
        primero = lista[0]
        max_del_resto = maximo(lista[1:])
        res = max(primero,max_del_resto)
        
    return res

def permutaciones(lista):
    if len(lista)==0:
        res = []
    elif len(lista)==1:
        res = [lista]
    else:
        res = []
        for idx, elem in enumerate(lista):
            permut_resto = permutaciones(lista[0:idx] + lista[idx+1:])
            res = [[elem] + p for p in permut_resto]
    return res