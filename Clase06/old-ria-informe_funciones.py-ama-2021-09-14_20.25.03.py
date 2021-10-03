import csv
import fileparse

def leer_camion(nombre_archivo):
    camion = fileparse.parse_csv(nombre_archivo)
    return camion


def leer_precios(nombre_archivo):
    precios = fileparse.parse_csv(nombre_archivo)
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


def hacer_informe(camion, precios):
    lista_prod = []
    for item_camion in camion:
        for item_precio in precios:
            if item_camion['nombre'] == item_precio:
                nombre = item_camion['nombre']
                cajones = int(item_camion['cajones'])
                precio = float(item_camion['precio'])
                cambio = float(precios[item_precio]) - \
                    float(item_camion['precio'])
                lista_prod.append((nombre, cajones, precio, cambio))
    return lista_prod


def imprimir_informe(informe):

    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    to_print = ''

    for r in headers:
        to_print += f'{r:>10s} '

    # print headers
    print(to_print)
    # print separators
    print(f'{"---------":>10s} {"---------":>10s} {"---------":>10s} {"---------":>10s}')
    # print products
    for nombre, cajones, precio, cambio in informe:
            precio = '$'+ str(precio)
            print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(dir_camion, dir_precio):
    camion_compra = leer_camion(dir_camion)
    lista_venta = leer_precios(dir_precio)
    informe = hacer_informe(camion_compra, lista_venta)
    imprimir_informe(informe)

informe_camion('../Data/camion.csv', '../Data/precios.csv')