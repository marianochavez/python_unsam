#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de semántica y estaba ubicado en el condicional else: return False,
#               al contener ese código solo evaluaba la primer letra del contenido.
#    Lo corregí ubicando el return False al final del bucle while.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de sintáxis ya que no contenia ":" en la declaranción de la función
#               ni en el bucle while ni condicional if. Ademas, la exprecion de comparación
#               del condicional if era incorrecta("=") y el return contenia la variable
#               Falso, lo cual es incorrecto .
# Se soluciona colocando los elementos faltantes
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era que el tipo int no posee la propiedad len() por lo tanto la llamada
#               tiene_uno(1984) va a causar error.
# Se soluciona llamando a la función correctamente
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')
# %%
#Ejercicio 3.4. Función suma()
#Comentario: El error es que no se retorna el valor de la suma
#               por lo tanto al momento de imprimirla no está
#               inicializada.
# Se soluciona colocando un return del valor de c en la funcion
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
# %%
#Ejercicio 3.5. Función suma()
#Comentario: append añade un unico elemendo al final de la lista, siempre se estaría agregando
#               el primer diccionario que es el de Naranja
# Se corrige
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            # registro[encabezado[0]] = fila[0]
            # registro[encabezado[1]] = int(fila[1])
            # registro[encabezado[2]] = float(fila[2])
            registro = {
                encabezado[0]:fila[0],
                encabezado[1]:int(fila[1]),
                encabezado[2]:float(fila[2])}
            camion.append(registro)
            registro[encabezado[0]] = 'mod'
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
# %%
