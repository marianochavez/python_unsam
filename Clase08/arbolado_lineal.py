# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:51:19 2021

@author: mariano
"""
import os
import pandas as pd
import seaborn as sns

directory = '../Data'
file = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directory, file)
df = pd.read_csv(fname)

cols_sel = ['nombre_cientifico', 'ancho_acera',
            'diametro_altura_pecho', 'altura_arbol']


df_lineal = df[cols_sel].copy()

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')