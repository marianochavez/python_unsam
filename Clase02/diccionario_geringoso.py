def convertir_geringoso(lista_palabras):
    d = {}
    for item in lista:
        traduccion = ''
        for c in item:
            traduccion += c
            if c == "a":
                traduccion += "pa"
            elif c == "e":
                traduccion += "pe"
            elif c == "i":
                traduccion += "pi"
            elif c == "o":
                traduccion += "po"
            elif c == "u":
                traduccion += "pu"
        d[item] = traduccion
    print(d)


lista = ['banana', 'manzana', 'mandarina']

convertir_geringoso(lista)

'''
{'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}
'''
