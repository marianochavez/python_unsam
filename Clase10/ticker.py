from vigilante import vigilar
import csv


def elegir_columnas(rows, indices):
    return ( (row[index] for index in indices) for row in rows)

def cambiar_tipo(rows, types):
    return ( (func(val) for func, val in zip(types, row)) for row in rows)

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filtrar_datos(rows, nombres):
    rows = (row for row in rows if row['nombre'] in nombres)

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def ticker(camion_file, log_file, fmt):
    import informe_final
    from formato_tabla import crear_formateador
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = filtrar_datos(rows, camion)
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        rowdata = [row['nombre'], str(row['precio']), str(row['volumen'])]
        formateador.fila(rowdata)

if __name__ == '__main__':
    import informe_final
    camion = informe_final.leer_camion('../Data/camion.csv')
    rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
    rows = filtrar_datos(rows, camion)
    for row in rows:
        print(row)