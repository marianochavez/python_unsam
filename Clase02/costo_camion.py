import csv


def costo_camion(nombre_archivo):
    costo_total = 0.0
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                costo_total += (int(row[1])*float(row[2]))
            except:
                print(f"Atención! Existe un campo vacío en la fila {row[0]}.")
    return costo_total


costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)

'''
Costo total: 47671.15
'''