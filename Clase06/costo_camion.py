import csv
import informe_funciones

def costo_camion(nombre_archivo):
    costo_total = 0.0
    camion = informe_funciones.leer_camion(nombre_archivo)
    
    for producto in camion:
        cajones = int(producto['cajones'])
        precio = float(producto['precio'])
        costo_total += (cajones*precio)
    

    return costo_total

costo = costo_camion('../Data/fecha_camion.csv')
print(costo)

'''
Costo total: 47671.15
'''
