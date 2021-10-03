import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

def calc_envido(puntos,repeticion):
    salida_puntos = 0
    for i in range(repeticion):
        mano = random.sample(naipes,k=3)
        mismo_palo = mano.copy()
        tengo_puntos = 0

        # *-----------------
        if mano[0][1] == mano[1][1]: 
            del mismo_palo[2]

            if mismo_palo[0][0] in (10,11,12):
                del mismo_palo[0]
                tengo_puntos = 20

            elif mismo_palo[1][0] in (10,11,12):
                del mismo_palo[1]
                tengo_puntos = 20

            if len(mismo_palo) == 2:
                tengo_puntos += (mismo_palo[0][0] + mismo_palo[1][0] + 20)

            if len(mismo_palo) == 1:
                tengo_puntos += mismo_palo[0][0]


        # *-----------------
        elif mano[0][1] == mano[2][1]:
            del mismo_palo[1]

            if mismo_palo[0][0] in (10,11,12):
                del mismo_palo[0]
                tengo_puntos = 20

            elif mismo_palo[1][0] in (10,11,12):
                del mismo_palo[1]
                tengo_puntos = 20

            if len(mismo_palo) == 2:
                tengo_puntos += (mismo_palo[0][0] + mismo_palo[1][0] + 20)

            if len(mismo_palo) == 1:
                tengo_puntos += mismo_palo[0][0]


        # *-----------------
        elif mano[1][1] == mano[2][1]:
            del mismo_palo[0]

            if mismo_palo[0][0] in (10,11,12):
                del mismo_palo[0]
                tengo_puntos = 20

            elif mismo_palo[1][0] in (10,11,12):
                del mismo_palo[1]
                tengo_puntos = 20

            if len(mismo_palo) == 2:
                tengo_puntos += (mismo_palo[0][0] + mismo_palo[1][0] + 20)

            if len(mismo_palo) == 1:
                tengo_puntos += mismo_palo[0][0]

        if tengo_puntos == puntos:
            salida_puntos += 1

    prob = salida_puntos/repeticion
    return prob

print(calc_envido(33,1000000))