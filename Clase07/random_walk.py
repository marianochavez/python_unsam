import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)    
    return pasos.cumsum()

def max_randomwalk(caminatas):
    '''Devuelve el camino con mas desviacion en cualquier momento
    '''
    maximo = max(abs(caminatas[0]))
    caminata_max = caminatas[0]
    for i in range(12):
        if maximo < max(abs(caminatas[i])):
            maximo = max(abs(caminatas[i]))
            caminata_max = caminatas[i]
    return caminata_max

def min_randomwalk(caminatas):
    '''Devuelve el camino con menos desviacion en cualquier momento
    '''
    minimo = max(abs(caminatas[0]))
    caminata_min = caminatas[0]
    for i in range(12):
        if minimo > max(abs(caminatas[i])):
            minimo = max(abs(caminatas[i]))
            caminata_min = caminatas[i]
    return caminata_min


N = 100000
doce_caminatas = [randomwalk(N) for i in range(12)]
minima_caminata = min_randomwalk(doce_caminatas)
maxima_caminata = max_randomwalk(doce_caminatas)

# DOCE CAMINATAS
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plot_caminatas = [plt.plot(doce_caminatas[i]) for i in range(12)]
plt.title('12 Caminatas al azar')
plt.xlabel('Distancia al origen',loc='right')
plt.ylabel('Tiempo')
plt.xticks([])
plt.yticks([-500,0,500])
plt.ylim(1000, -1000)

# MAS ALEJADA
plt.subplot(2, 2, 3)
plt.plot(maxima_caminata)
plt.title('La caminata que más se aleja')
plt.xlabel('Distancia al origen',loc='right')
plt.ylabel('Tiempo')
plt.xticks([])
plt.yticks([-500,0,500])
plt.ylim(1000, -1000)

# MENOS ALEJADA
plt.subplot(2, 2, 4)
plt.plot(minima_caminata)
plt.title('La caminata que menos se aleja')
plt.xlabel('Distancia al origen',loc='right')
plt.ylabel('Tiempo')
plt.xticks([])
plt.yticks([-500,0,500])
plt.ylim(1000, -1000)

plt.show()