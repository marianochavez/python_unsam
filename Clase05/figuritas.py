import random
import numpy as np
import matplotlib.pyplot as plt

'''
Álbum con 670 figuritas.
Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
Cada paquete trae cinco figuritas.
'''

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=int)
    return album

def album_incompleto(A):
    if 0 in A:
        return True
    else:
        return False

def comprar_figu(figus_total):
    figu = random.randint(0,figus_total-1)
    return figu

def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        paquete.append(random.randint(0,figus_total-1))
    return paquete

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    compras = 0
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        compras += 1
        album[figu] += 1
    return compras

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    compras = 0
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total,figus_paquete)
        compras += 1
        for figu in paquete:
            album[figu] += 1
    return compras

def experimento_figus(n_repeticiones, figus_total):
    promedio = random.mean([cuantas_figus(figus_total) for i in range(n_repeticiones)])
    return promedio

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

# album = crear_album(670)
# print(album_incompleto(album))
# cuantas_figus(300)
# promedio = random.mean([cuantas_figus(6) for i in range(1000)])
# print(experimento_figus(100,670))
# print(cuantos_paquetes(670,5))
# promedio = random.mean([cuantos_paquetes(670,5) for i in range(1000)])
# print(promedio)