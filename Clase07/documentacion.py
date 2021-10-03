def valor_absoluto(n):
    '''Devuelve el valor absoluto de un numero n.
    
    Pre: n es un numero
    Pos: Se devuelve n con signo positivo
    '''
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    '''Devuelve la sumatora de los numeros pares de una lista.

    Pre: l es una lista de numeros enteros
    Pos: devuelve un res igual a la sumatoria de numero pares de la lista
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''Devuelve la sumatoria de b veces el numero a.

    Pre: b>=0
    Pos: res = a * b
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

def collatz(n):
    '''Sea cual sea el número n inicial, tras un número finito de repeticiones de la operación se llega a 1.
    Devuelve el numero de repeticiones de la operacion. Si n es par se aplica division entera entre 2, si es
    impar realiza 3*n+1.
    
    Pre: n>0
    Pos: res = cantidad de operaciones aplicadas
    '''
    res = 1

    while n!=1:
        print(f'n={n}, res={res}')
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res