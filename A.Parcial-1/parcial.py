# a = [ 'n','e','p']
# b = ['R',43,78]
# d= dict(zip(a,b))
# print(d)
# if (d['e'])%2 == 0:
#     print('Par')
# else:
#     print('impar')

# lista = ['uno','dos','tres']
# print(lista[1])

# a = [1]
# b = [2,3]
# c= [4,5,6]
# k=[a,b,c]
# m=k.copy()
# m[1].append(7)
# print(k)

# var={'cero':0,'uno':1}
# print(var[0])

# lista = [1,2,3]
# n = 2
# for k in range(10):
#     try:
#         if k < n and lista[k] == 3:
#             print('caso 1')
#     except Exception:
#         print('Caso 2')

# import csv
# f = open('../Data/camion.csv', 'rt')
# headers = next(f)
# print(type(headers))

# d = {}
# dias = ['lunes','martes','miercoles','jueves','viernes','sabado', 'domingo']
# dias_abr = ['lu','mar','mier','jue','vier','sa', 'dom']
# while len(d) < 6:
#     dia = dias[len(d)]
#     abr=dias_abr[ len(d)]
#     d[dia]=abr
# print(d['sabado'])


# r=[ x *y for x in range(-10,10) if x > 0 and x%2==1 for y in [1,0,-1] if y!=0]
# print(r)

# n = 5
# lista = [1] * n
# print(lista)
# for i in range(1, n):
#     try:
#         lista[i] = lista[i-1] + lista[i] + lista[i+1]
#     except Exception:
#         pass
# print( lista)

# frutas = 'Manzana, asdad'
# print(type(frutas))
# print(type(frutas[0]))
# print(type('m'))


# def func(a):
#     a += 1

# a = 1
# print(type(a))
# a = func(a)
# print(type(a))
# a = a + 1
# print(type(a))
# print(a)


# import numpy as np
# a = np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12],[ 13,14,15,16]])
# b = a[0:3]
# print(b)

# for i,c in enumerate('pavada'):
#     if i != (i//2)*2:
#         print(c,end='')

# i = 0
# suma = 0
# while i <= 10:
#     suma += i
#     print(suma)
# print(suma)

# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# print(mat[1][1])
# suma = 0
# n=3
# for i in range(n):
#     for j in range(i+1,n):
#         suma += mat[i][j]
# print(suma)

# lista = [ 2,4,6,8,10]
# mia = {x: x**2 for x in range(10) if x in lista}
# print(mia.items())

# def funct(a,b):
#     c = a + b
# c = 3
# c = funct(2,3)
# print(type(c),c)


# n= 5
# lista = [1] * n
# for i in range(n):
#     if i + 1 < n and lista[i+1]==1:
#         lista[i]+=lista[i+1]
# lista[4]=2
# print(lista)

# def una_funcion():
#     if 'a' or 'e' in 'casa':
#         return True
#     else:
#         return False
# print(una_funcion())