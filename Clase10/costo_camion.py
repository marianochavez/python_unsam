import informe_final

def costo_camion(nombre_archivo):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(nombre_archivo)
    return camion.precio_total()

def f_principal(argv):
    costo = costo_camion(argv[1])
    print(f'Costo total: {costo}')

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)

'''
Costo total: 47671.15
'''
