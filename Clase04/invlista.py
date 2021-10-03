# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:45:49 2021

@author: mariano
"""

def invertir_lista(lista):
    invertida = []
    for i,e in enumerate(lista):
        invertida.insert(-i, e)
    return invertida

lista_invertida = invertir_lista([1,2,3,4,5,6])
print(lista_invertida)

lista_invertida = invertir_lista(['Holanda','Mexico','Argentina','Afganistan'])
print(lista_invertida)
# ['Afganistan', 'Argentina', 'Mexico', 'Holanda']