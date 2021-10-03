def buscar_precio(nombre_fruta):
    try:
        f = open('../Data/precios.csv', 'rt')
        for line in f:
            row = line.split(",")
            if row[0] == nombre_fruta:
                precio_fruta = float(row[1])
        f.close()
        print(f'El precio de un cajón de {nombre_fruta} es: {precio_fruta}')
    except:
        print(f"{nombre_fruta} no figura en el listado de precios.")


precio = buscar_precio('Frambuesa')

'''
El precio de un cajón de Frambuesa es: 34.35
'''