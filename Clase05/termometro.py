import random
import numpy as np
from numpy.core.fromnumeric import mean

def medir_temp(muestras):
    mediciones = [round(random.normalvariate(37.5,0.2),2) for i in range(muestras)]
    np.save('../Data/temperaturas.npy',mediciones)
    return mediciones

def resumen_temp(cantidad):
    
    mediciones = medir_temp(cantidad)
    mediciones.sort()

    maximo = max(mediciones)
    minimo = min(mediciones)
    promedio = round(mean(mediciones),2)
    media = 0
    if cantidad%2 == 0:
        media = round((mediciones[int(cantidad/2)-1] + mediciones[int(cantidad/2)])/2,2)
    else:
        media = mediciones[int(cantidad/2)]

    resumen = (maximo,minimo,promedio,media)
    return resumen

medir_temp(999)
# print(resumen_temp(7))