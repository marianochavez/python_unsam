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


camion_compra = leer_camion('../Data/camion.csv')
lista_venta = leer_precios('../Data/precios.csv')
# balance(camion_compra, lista_venta)
informe = hacer_informe(camion_compra, lista_venta)

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

"""out
    Nombre    Cajones     Precio     Cambio
 ---------  ---------  ---------  ---------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84
"""