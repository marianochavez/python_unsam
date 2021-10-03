import csv


def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)  # headers
        for row in rows:
            lote = {'nombre': row[0], 'cajones': int(
                row[1]), 'precio': float(row[2])}
            camion.append(lote)
    return camion


def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = row[1]
            except:
                pass
    return precios


def balance(camion, precios):
    total_compra = 0.0
    total_venta = 0.0

    for item in camion:
        total_compra += item['cajones']*item['precio']

    for item_camion in camion:
        for item_precio in precios:
            if item_camion['nombre'] == item_precio:
                n_cajones = int(item_camion['cajones'])
                precio = float(precios[item_precio])
                total_venta += n_cajones*precio

    print(f"Ganancia: {total_venta} \nPerdida: {total_compra}")

    if total_compra < total_venta:
        print(f"Se obtuvo GANANCIAS por {round(total_venta-total_compra,2)}.")
    else:
        print(f"Se obtuvo PERDIDAS por {round(total_compra-total_venta,2)}")


camion_compra = leer_camion('../Data/camion.csv')
lista_venta = leer_precios('../Data/precios.csv')
balance(camion_compra, lista_venta)

""" OUTPUT
Ganancia: 1358.24 
Perdida: 47671.15 
Se obtuvo PERDIDAS en el balance.
"""