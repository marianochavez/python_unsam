# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 08:49:45 2021

@author: mariano
"""
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from scipy import signal # para procesar señales
import matplotlib.pyplot as plt
from datetime import timedelta


""" Ejercicio 8.11 """
# Cada cuarto de hora
df=pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'],parse_dates=True)
dh =df['10-01-2014':].copy() #ultimo trimestre
freq_horaria = 60 # 4 para 15min, 60 para 1min
cant_horas = 24
N = cant_horas * freq_horaria
#resampleo cada tantos minutos
dh = dh.resample(f'{int(60/freq_horaria)}T').mean()
#rellenos los NaNs suavemente
dh =dh.interpolate(method='quadratic')
# genero vector de desplazamientos (enteros)
ishifts = np.arange(-N,N+1)
# y su desplamiento horario asociado
shifts=ishifts/freq_horaria
# finalmente calculo las correlaciones correspondientes
corrs = np.zeros(shifts.shape)
for i, sh in enumerate(ishifts):
    corrs[i] = pearsonr(dh['H_SF'].shift(sh)[N:-N],dh['H_BA'][N:-N])[0]
# y grafico
max_value_index = np.argmax(corrs)
print(f'Tiempo de desplazamiento entre San Fernando y BsAs: {abs(shifts[max_value_index]*60)} min')
# plt.plot(shifts, corrs)

"""Ejercicios OPTATIVOS
"""

def calcular_fft(y, freq_sampleo = 24.0):
    '''y debe ser un vector con números reales
    representando datos de una serie temporal.
    freq_sampleo está seteado para considerar 24 datos por unidad.
    Devuelve dos vectores, uno de frecuencias 
    y otro con la transformada propiamente.
    La transformada contiene los valores complejos
    que se corresponden con respectivas frecuencias.'''
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1/freq_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran
"""
inicio = '2014-01'
fin = '2014-06'
alturas_sf = df[inicio:fin]['H_SF'].to_numpy()
alturas_ba = df[inicio:fin]['H_BA'].to_numpy()

freq_sf, fft_sf = calcular_fft(alturas_sf)
plt.plot(freq_sf, np.abs(fft_sf))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.show()
"""
# print(signal.find_peaks(np.abs(fft_sf), prominence = 8))

# plt.plot(freq_sf, np.abs(fft_sf))
# plt.xlabel("Frecuencia")
# plt.ylabel("Potencia (energía)")
# plt.xlim(0,4)
# plt.ylim(0,20)
# # me quedo solo con el último pico
# pico_sf = signal.find_peaks(np.abs(fft_sf), prominence = 8)[0][-1]
# # es el pico a analizar, el de la onda de mareas
# # marco ese pico con un circulito rojo
# plt.scatter(freq_sf[pico_sf], np.abs(fft_sf)[pico_sf], facecolor = 'r')
# plt.show()

# ESPECTROS DE POTENCIA Y DE ANGULOS PARA BUENOS AIRES
"""
freq_ba, fft_ba = calcular_fft(alturas_ba)
plt.plot(freq_ba, np.abs(fft_ba))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.xlim(0,4)
plt.ylim(0,20)
# me quedo solo con el último pico
pico_ba = signal.find_peaks(np.abs(fft_ba), prominence = 8)[0][-1]
#se grafican los picos como circulitos rojos
plt.scatter(freq_ba[pico_ba], np.abs(fft_ba)[pico_ba], facecolor='r')
plt.title("Espectro de Potencias Bs.As.")
plt.show()
"""

""" Ejercicio 8.14 """
dzarate = pd.read_csv('../Data/OBS_Zarate_2013A.csv',index_col=['Time'],parse_dates=True)
dbsas = pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'],parse_dates=True)
dh_zarate = dzarate.copy()
dh_bsas = dbsas['2012-07-01':'2013-06-30'].copy()

freq_horaria = 4 # 4 para 15min, 60 para 1min
cant_horas = 24
N = cant_horas * freq_horaria
#resampleo cada tantos minutos
dh_zarate = dh_zarate.resample(f'{int(60/freq_horaria)}T').mean()
dh_bsas = dh_bsas.resample(f'{int(60/freq_horaria)}T').mean()
#rellenos los NaNs suavemente
dh_zarate = dh_zarate.interpolate(method='quadratic')
dh_bsas = dh_bsas.interpolate(method='quadratic')

# genero vector de desplazamientos (enteros)
ishifts = np.arange(-N,N+1)
# y su desplamiento horario asociado
shifts=ishifts/freq_horaria
# finalmente calculo las correlaciones correspondientes
corrs = np.zeros(shifts.shape)
for i, sh in enumerate(ishifts):
    corrs[i] = pearsonr(dh_zarate['H_Zarate'].shift(sh)[N:-N],dh_bsas['H_BA'][N:-N])[0]
max_value_index = np.argmax(corrs)
time_result = abs(shifts[max_value_index])
str_time = str(timedelta(hours=time_result))
print(f'Tiempo de desplazamiento entre BsAs y Zarate: {str_time}')