# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:16:21 2021

@author: mariano
"""

def buscar_u_elemento(lista,n):
    '''
    Devuelve la ultima posicion de un elemento en la lista, sino -1
    '''
    pos = -1
    for i, num in enumerate(lista):
        if num == n:
            pos = i
    return pos

def buscar_n_elementos(lista,n):
    '''
    Devuelve la cantidad de veces que aparece un numero en la lista, sino 0
    '''
    cant = 0
    for num in lista:
        if num == n:
            cant += 1
    return cant

def maximo(lista):
    '''
    Devuelve el maximo valor de una lista
    '''
    m = lista[0]
    for e in lista:
        if e > m:
            m = e
    return m

def minimo(lista):
    '''
    Devuelve el minimo valor de una lista    
    '''
    m = lista[0]
    for e in lista:
        if e < m:
            m = e
    return m

posicion = buscar_u_elemento([1,2,3,4,5,6], 2)
print(posicion)
# 1

cantidad  = buscar_n_elementos([1,1,1,2,3,4,4,5], 4)
print(cantidad)
# 2

mayor = maximo([-5,-9])
print(mayor)
# -5

menor = minimo([-9,0,2,-19])
print(menor)
# -19