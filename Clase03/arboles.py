import csv
from pprint import pprint
from collections import Counter


def leer_parque(nombre_archivo, nombre_parque):
    # Devuelve una lista con diccionarios de arboles de un parque
    parque = []
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            if str(record['espacio_ve']) == nombre_parque:
                parque.append(record)
    return parque


def especies(lista_arboles):
    # Devuelve un diccionario con las especies sin repetir de una lista
    especies_total = []
    for item in lista_arboles:
        especies_total.append(item['nombre_com'])
    especies = set(especies_total)
    return especies


def contar_ejemplares(lista_arboles):
    # Devuelve la cantidad de cada ejemplar de la lista
    cantidades = Counter()
    for s in lista_arboles:
        cantidades[s['nombre_com']] += 1
    return cantidades


def obtener_alturas(lista_arboles, especie):
    # Devuelve una lista de las alturas de un arbol
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
    return alturas


def obtener_inclinaciones(lista_arboles, especie):
    # Devuelve una lista de las inclinaciones de un arbol
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(int(arbol['inclinacio']))
    return inclinaciones


def especimen_mas_inclinado(lista_arboles):
    max_incli = 0
    nombre_incli = ''
    for arbol in lista_arboles:
        incli_arbol = int(arbol['inclinacio'])
        if incli_arbol > max_incli:
            max_incli = incli_arbol
            nombre_incli = arbol['nombre_com']
    return(nombre_incli, max_incli)


def especie_promedio_mas_inclinada(lista_arboles):
    max_incli_prom = 0.0
    nombre_incli = ''
    especies_arboles = especies(lista_arboles)

    for arbol_especie in especies_arboles:
        lista_incli = obtener_inclinaciones(lista_arboles, arbol_especie)
        promedio = sum(lista_incli)/len(lista_incli)
        if promedio > max_incli_prom:
            max_incli_prom = promedio
            nombre_incli = arbol_especie
    return(nombre_incli, max_incli_prom)


# Ejercicio 3.18
lista_parque = leer_parque(
    '../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
print(len(lista_parque))
# Salida: 690

# Ejercicio 3.19
lista_especies = especies(lista_parque)
print(lista_especies)
"""
{'Washingtonia', 'Casuarina', 'Ceibo', 'Castaño de Indias común', 'Pindó', 'Acacia blanca', 'Cedro del Líbano  (Cedro de Salomón)', 'Parasol de la china', 'Visco (Viscote, Arca)', 'Azarero', 'Árbol del cielo (Ailanto o Árbol de los dioses)', 'Almez de china', 'Olivo', 'Tuja', 'Bunya-bunya (Araucaria de Bidwill)', 'Ligustro', 'Álamo plateado', 'Brachichiton (Árbol botella, Brachichito)', 'Ginkgo', 'Morera de papel (Moral de China)', 'Falso Alcanforero', 'Lapachillo', 'Criptomeria (Cedro del Japón)', 'Ficus', 'Laurel', 'Tilo', 'Ombú', 'Crataegus', 'Eucalipto (Eucalipto común)', 'Higueron', 'Magnolia', 'Eucalipto', 'Cedro misionero (Cedro colorado o Cedro real)', 'Palo borracho', 'Cedro del Himalaya', 'Juniperus', 'Arce negundo', 'Morera blanca', 'Cedro blanco de California', 'Ciprés', 'Plátano', 'No Determinado', 'Almez (Almecino o Almecina)', 'Acacia de Baile (Mimosa de Baile)', 'Fenix', 'Paulonia (Árbol de la emperatriz)', 'Hibiscus', 'Timbó (Oreja de negro)', 'Gomero', 'Sauce criollo', 'Cotoneaster', 'Paraíso', 'Jacarandá', 'Paraíso umbraculifera', 'Sófora japónica', 'Palo borracho rosado', 'Tipa blanca', 'Falso Guayabo (Guayaba del Brasil)', 'Palma de california', 'Fresno (Fresno común)', 'Espino de fuego', 'Fresno americano', 'Juglans', 'No Determinable', 'Cedro azulado', 'Rosa de Siria', 'Encina', 'Washingtonia (Palmera washingtonia)', 'Ibirá pitá', 'Sota Caballo\xa0'}
"""

# Calculo de arboles populares Ejercicio 3.20
# cantidad_ejemplares = contar_ejemplares(lista_parque)
# pprint(cantidad_ejemplares)
# Prueba en 3 parques
parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
print("Arboles mas populares en:")
for parque in parques:
    print(f'{parque}:')
    populares = contar_ejemplares(leer_parque(
        '../Data/arbolado-en-espacios-verdes.csv', parque)).most_common(5)
    for arbol in populares:
        print(f'\t{arbol[0]}: {arbol[1]}')
"""
Arboles mas populares en:
GENERAL PAZ:
        Casuarina: 97
        Tipa blanca: 54
        Eucalipto: 49
        Palo borracho rosado: 44
        Fenix: 40
ANDES, LOS:
        Jacarandá: 117
        Tipa blanca: 28
        Ciprés: 21
        Palo borracho rosado: 18
        Lapacho: 12
CENTENARIO:
        Plátano: 137
        Jacarandá: 45
        Tipa blanca: 42
        Palo borracho rosado: 41
        Fresno americano: 38
"""


# Ejercicio 3.21
# Calculo de altura maxima y promedio Ejercicio 3.21, se probo en los tres parques definidos anteriormente
arbol_analizar = 'Jacarandá'
for parque in parques:
    alturas_arboles = obtener_alturas(leer_parque(
        '../Data/arbolado-en-espacios-verdes.csv', parque), arbol_analizar)
    altura_max = max(alturas_arboles)
    altura_prom = round(sum(alturas_arboles)/len(alturas_arboles), 2)
    print(
        f'Parque {parque}\n\tAltura máxima: {altura_max}\n\tAltura promedio: {altura_prom}')
"""
Parque GENERAL PAZ
        Altura máxima: 16.0
        Altura promedio: 10.2
Parque ANDES, LOS
        Altura máxima: 25.0
        Altura promedio: 10.54
Parque CENTENARIO
        Altura máxima: 18.0
        Altura promedio: 8.96
"""


# Ejercicio 3.22
inclinaciones_arbol = obtener_inclinaciones(lista_parque, arbol_analizar)
print(inclinaciones_arbol)
# Salida: [23, 10, 8, 5, 15, 0, 5, 15, 0, 43, 25, 0, 0, 41, 21, 20, 26, 5, 10, 8, 5, 4, 19, 10, 20, 15, 0, 45, 35, 0, 9, 0, 0, 0, 24, 28, 19, 0, 15, 15, 16, 0, 26, 0,
# 15]

# Ejercicio 3.23
arbol_mas_inclinado = especimen_mas_inclinado(leer_parque(
    '../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO'))
print(
    f'Nombre:{arbol_mas_inclinado[0]}, Inclinación: {arbol_mas_inclinado[1]}')
# Salida: Nombre:Falso Guayabo (Guayaba del Brasil), Inclinación: 80

# Ejercicio 3.24
arbol_mas_inclinado_prom = especie_promedio_mas_inclinada(lista_parque)
print(
    f'Nombre:{arbol_mas_inclinado_prom[0]}, Inclinación: {arbol_mas_inclinado_prom[1]}')
# Salida: Nombre:Rosa de Siria, Inclinación: 25.0


# PREGUNTAS EXTRAS
def el_mas_inclinado(nombre_archivo):
    parque = []
    max_inclinacion = 0
    arbol_mas_inclinado = {}
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            parque.append(record)
    for arbol in parque:
        if int(arbol['inclinacio']) > max_inclinacion:
            max_inclinacion = int(arbol['inclinacio'])
            arbol_mas_inclinado = arbol
    print(
        f'El arbol mas inclinado de todos es {arbol_mas_inclinado["nombre_com"]} con {arbol_mas_inclinado["inclinacio"]} y se encuentra en LONG: {arbol_mas_inclinado["long"]} LAT: {arbol_mas_inclinado["lat"]}')


def el_mas_alto(nombre_archivo):
    parque = []
    max_altura = 0
    arbol_mas_alto = {}
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            parque.append(record)
    for arbol in parque:
        if int(arbol['altura_tot']) > max_altura:
            max_altura = int(arbol['altura_tot'])
            arbol_mas_alto = arbol
    print(
        f'El arbol mas alto de todos es {arbol_mas_alto["nombre_com"]} con {arbol_mas_alto["altura_tot"]} metros y se encuentra en LONG: {arbol_mas_alto["long"]} LAT: {arbol_mas_alto["lat"]}')


el_mas_inclinado('../Data/arbolado-en-espacios-verdes.csv')
# Salida: El arbol mas inclinado de todos es Timbó (Oreja de negro) con 90 y se encuentra en LONG: -58.39515390060001 LAT: -34.6368768575
el_mas_alto('../Data/arbolado-en-espacios-verdes.csv')
# Salida: El arbol mas alto de todos es Rosa de Siria con 54 metros y se encuentra en LONG: -58.398926961099995 LAT: -34.5818308351
