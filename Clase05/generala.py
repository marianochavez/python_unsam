import random

from numpy.core.numeric import count_nonzero

def tirar(n):
    tirada = []
    for i in range(n):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    if tirada.count(tirada[0]) == 5:
        return True
    return False

def prob_generala(N):
    cant_generala = 0

    for i in range(N):
        primer_tirada = tirar(5)
        num_repeticiones = 0
        num_elegido = 0
        
        # Verifico qué numero se repite en la primer tirada
        for i in range(len(primer_tirada)):
            if primer_tirada.count(i) > num_repeticiones:
                # Si no hay ninguna repeticion igual elige un numero
                num_repeticiones = primer_tirada.count(i)
                num_elegido = i
        
        # Realizo la segunda tirada pero sacando los dados elegidos
        segunda_tirada = tirar(5-num_repeticiones)
        # Verifico que todos los dados sean iguales
        if segunda_tirada.count(num_elegido) == len(segunda_tirada):
            cant_generala += 1
        elif segunda_tirada.count(num_elegido) == 1:
            num_repeticiones += 1
    
        # Realizo la tercer tirada pero sacando los dados elegidos
        tercer_tirada = tirar(5-num_repeticiones)
        # Verifico que todos los dados sean iguales
        if tercer_tirada.count(num_elegido) == len(tercer_tirada):
            cant_generala += 1

    prob = cant_generala/N
    return prob

# PROBABILIDAD GENERALA SERVIDA
# N = 1000000
# G = sum([es_generala(tirar(5)) for i in range(N)])
# prob = G/N
# print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

"""La probabilidad de obtener una generala es:
    Fijamos un numero, la prob de obtener ese num es 1/6
    Para repetir ese numero 5 veces es (1/6)**5 = 1/1296 = 
"""

print(prob_generala(1000))