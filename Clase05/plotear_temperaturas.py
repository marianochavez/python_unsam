import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy',mmap_mode='r')
    print(len(temperaturas))
    plt.hist(temperaturas,bins=25)
    plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.

plotear_temperaturas()