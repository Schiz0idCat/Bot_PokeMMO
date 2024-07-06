import numpy as np
import matplotlib.pyplot as plt

def randomWait(wait, center=.3, dispersion=.3, maxLimit=1): # Randomiza el tiempo de espera
    media = wait + center # centro de la distribución
    desviacionEstandar = dispersion # dispersión
    
    datos = [] # Lista para almacenar los datos dentro del rango
    while len(datos) < 1000: # Genera 1000 números aleatorios dentro del rango
        num = np.random.normal(loc=media, scale=desviacionEstandar)
        if wait <= num <= wait + maxLimit:
            datos.append(num)
    
    plt.hist(datos, bins=30, density=True, alpha=0.6, color='b') # Histograma con 30 bins
    plt.xlabel('Tiempo de espera')
    plt.ylabel('Densidad de probabilidad')
    plt.title('Distribución Normal')
    plt.show()

# Prueba del código
randomWait(5)