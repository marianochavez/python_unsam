# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 08:49:45 2021

@author: mariano
"""
import pandas as pd
import numpy as np
from scipy.stats import pearsonr


def calc_desplazamiento_tiempo(df):
    """Retorna el desplazamiento de tiempo en horas entre dos mareas"""
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
    t_value = shifts[max_value_index]
    return t_value


df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)
dh = df['12-25-2014':].copy()

delta_t = round(calc_desplazamiento_tiempo(df)) # tiempo que tarda la marea entre ambos puertos = -1
delta_h = 19.2 # diferencia de los ceros de escala entre ambos puertos

pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()