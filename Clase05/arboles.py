import os
import matplotlib.pyplot as plt
import numpy as np
import csv

def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo,'rt',encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            arboleda.append(dict(zip(headers,row)))

    return arboleda

def medidas_de_especies(especies,arboleda):
    alt_diam_especie = {especie:[(arbol['altura_tot'],arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie]  for especie in especies }
    return alt_diam_especie

def scatter_hd(lista_de_pares):
    # altura = [lista_de_pares[i][0] for i in range(len(lista_de_pares))]
    # diametro = [lista_de_pares[i][1] for i in range(len(lista_de_pares))]
    altura = np.asarray(lista_de_pares)[:,0]
    diametro = np.asarray(lista_de_pares)[:,1]
    altura.sort()
    diametro.sort()

    plt.scatter(diametro,altura,alpha=0.5)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto")
    plt.xlim(0,30) 
    plt.ylim(0,100)
    plt.show()

# Ejercicio 4.15
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

# Ejercicio 4.16: Alturas de los Jacarandá
H = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
# print(H)

# Ejercicio 4.17: Altura y Diametro de los Jacarandá
HD = [(arbol['altura_tot'],arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
# print(HD)

# Ejercicio 4.18
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas_especies = medidas_de_especies(especies,arboleda)
#print(len(medidas_especies['Eucalipto']))

# 5.25
nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
altos = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
plt.hist(altos,bins=25)
plt.show()

# 5.26
# scatter_hd(HD)

# 5.27
nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)
for especie in especies:
    scatter_hd(medidas[especie])