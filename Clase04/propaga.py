# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:56:16 2021

@author: mariano
"""

def propagar(lista):

    for i,e in enumerate(lista):
        if e == 1:
            # Elementos a izquierda del 1
            recorrida = lista[0:i]
            recorrida.reverse()
            for n,a in enumerate(recorrida,1):
                if a == 0:
                    lista[i-n] = 1
                else:
                    break
            # Elementos a derecha del 1
            restante = lista[i+1:]
            for n,a in enumerate(restante,1):
                if a == 0:
                    lista[i+n] = 1
                else:
                    break
    return lista
            
fosforos = propagar([0,-1,0,1,0,0,0,0,0,-1,0,0,1,0,-1,0])
print(fosforos)
# [0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 0]