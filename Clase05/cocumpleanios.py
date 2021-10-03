def mismo_dia(N):
    cant_pers = N
    dias = 365
    
    casos_posibles = dias**cant_pers

    casos_favorables = 365
    for i in range(1,cant_pers):
        casos_favorables = casos_favorables*(dias-i)

    prob = 1 - (casos_favorables/casos_posibles)
    return prob

print(mismo_dia(30))