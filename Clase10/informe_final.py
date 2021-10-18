import fileparse
from lote import Lote
import formato_tabla
from camion import Camion


def leer_camion(nombre_archivo):
    '''Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(nombre_archivo) as file:
        camiondicts = fileparse.parse_csv(file, select = ['nombre', 'cajones', 'precio'],types = [str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)


def leer_precios(nombre_archivo):
    """Lee un archivo csv con precios y lo convierte en una lista"""
    precios = fileparse.parse_csv(open(nombre_archivo), types=[str, float], has_headers=False)
    return precios


def balance(camion, precios):
    """Imprime si se obtuvieron ganancias o perdidas en relacion a las ventas con el precio
    del camion y los descriptos en el archivo precios"""
    total_compra = 0.0
    total_venta = 0.0

    for item in camion:
        # total_compra += item.cajones * item.precio
        total_compra += item.costo()
    for item_camion in camion:
        for item_precio in precios:
            if item_camion.nombre == item_precio:
                n_cajones = item_camion.cajones
                precio = precios[item_precio]
                total_venta += n_cajones*precio

    print(f"Ganancia: {total_venta} \nPerdida: {total_compra}")

    if total_compra < total_venta:
        print(f"Se obtuvo GANANCIAS por {round(total_venta-total_compra,2)}.")
    else:
        print(f"Se obtuvo PERDIDAS por {round(total_compra-total_venta,2)}")


def hacer_informe(camion, precios):
    """Retorna una lista con los productos del camion, cajones, precio y la diferencia 
    entre el precio de compra y venta"""
    lista_prod = []
    for item_camion in camion:
        for item_precio in precios:
            if item_camion.nombre == item_precio[0]:
                nombre = item_camion.nombre
                cajones = item_camion.cajones
                precio = item_camion.precio
                cambio = item_precio[1] - item_camion.precio
                lista_prod.append((nombre, cajones, precio, round(cambio, 2)))
    return lista_prod


def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es txt
    Alternativas: csv o html
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Obtener los datos para un informe
    data_informe = hacer_informe(camion, precios)

    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)


def f_principal(argv):
    if len(argv) == 4:
        informe_camion(argv[1], argv[2], argv[3])
    else:
        informe_camion(argv[1], argv[2])



if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
