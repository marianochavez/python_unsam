# camion_commandline.py
import csv
import sys


def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    costo_total = 0
    for row in rows:
        try:
            costo_total += (int(row[1])*float(row[2]))
        except:
            print(f"Atención! Existe un campo vacío en la fila {row[0]}.")
    f.close()
    return costo_total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)

'''
Costo total: 47671.15
'''