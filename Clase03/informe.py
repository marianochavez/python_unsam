import csv

#! no existe la funcion costo_camion, etc
#! https://mail.google.com/mail/u/0/#inbox/FMfcgzGkbDccmCVVcSFMvttQhdrRbTDw

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # lote = {headers[0]: row[0], headers[1]: int(
            #     row[1]), headers[2]: float(row[2])}
            lote = dict(zip(headers,row))
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
        ncajones = int(item['cajones'])
        precio = float(item['precio'])
        total_compra += ncajones*precio

    for item_camion in camion:
        for item_precio in precios:
            if item_camion['nombre'] == item_precio:
                ncajones = int(item_camion['cajones'])
                precio = float(precios[item_precio])
                total_venta += ncajones*precio

    print(f"Ganancia: {total_venta} \nPerdida: {total_compra}")

    if total_compra < total_venta:
        print(f"Se obtuvo GANANCIAS por {round(total_venta-total_compra,2)}.")
    else:
        print(f"Se obtuvo PERDIDAS por {round(total_compra-total_venta),2}.")


camion_compra = leer_camion('../Data/fecha_camion.csv')
lista_venta = leer_precios('../Data/precios.csv')
balance(camion_compra, lista_venta)

""" OUTPUT
Ganancia: 62986.1 
Perdida: 47671.15
Se obtuvo GANANCIAS por 15314.95.
"""