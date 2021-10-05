# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:18:17 2021

@author: mariano
"""
import os
import pandas as pd
import seaborn as sns


directory = '../Data'
fname_parques = os.path.join(directory, 'arbolado-en-espacios-verdes.csv')
fname_veredas = os.path.join(directory, 'arbolado-publico-lineal-2017-2018.csv')

df_parques = pd.read_csv(fname_parques)
df_veredas = pd.read_csv(fname_veredas)


df_tipas_parques = df_parques[df_parques['nombre_cie'] =='Tipuana Tipu'][['diametro', 'altura_tot']].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico']== 'Tipuana tipu'][['diametro_altura_pecho', 'altura_arbol']].copy()

df_tipas_parques = df_tipas_parques.rename(index=str, columns={'diametro':'diametro_altura_pecho','altura_tot':'altura'})
df_tipas_veredas = df_tipas_veredas.rename(index=str, columns={'diametro_altura_pecho':'diametro_altura_pecho','altura_arbol':'altura'})

df_tipas_parques = df_tipas_parques.assign(ambiente='parque')
df_tipas_veredas = df_tipas_veredas.assign(ambiente='vereda')

df_tipas = pd.concat([df_tipas_parques,df_tipas_veredas])

df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
df_tipas.boxplot('altura', by = 'ambiente')