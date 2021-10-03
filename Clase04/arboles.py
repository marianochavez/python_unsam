# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 19:30:38 2021

@author: mariano
"""
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