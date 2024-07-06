import pydirectinput as pd
import time
import numpy as np
import cv2
from api.images import Images

class Interaction():
    def __init__(self):
        self.img = Images()
        
        # Configuración de botones
        self.button = { 
            'A' : 'z',
            'B' : 'x',
            'Rod' : '4',
            'UP' : 'up',
            'DOWN' : 'down',
            'LEFT' : 'left',
            'RIGHT' : 'right'
        }
    
    def randomWait(self, wait, center=.3, dispersion=.3, maxLimit = 1): # Randomiza el tiempo de espera
        media = wait + center # centro de la distribución
        desviacionEstandar = dispersion # disperción
        
        while True: # genera un número aleatorio
            num = np.random.normal(loc=media, scale=desviacionEstandar)
            
            if wait <= num <= wait + maxLimit: # verifica que esté en el rango [N, N + 1.5]
                time.sleep(num)
                break
    
    def switchWindow(self):
        pd.keyDown('alt')
        pd.press('tab')
        pd.keyUp('alt')
    
    def hotKey(self, key, hold_time=.1, coolodwn=True): # Presionar botones
        if coolodwn:
            self.randomWait(0)

        pd.keyDown(key)
        time.sleep(hold_time)
        pd.keyUp(key)
    
    def click(self, coordenates): # clickea en una coordenada específica
        x, y = coordenates[0], coordenates[1]
        self.randomWait(0)
        pd.click(x, y)

    def move(self, moveType, directionKey, squares): # movimiento de personaje
        parameters = {
        "walk": {"factor": 0.2346, "marginOfError": - 0.009},
        "run": {"factor": 0.18325, "marginOfError": - 0.13},
        "bike": {"factor": 0.08286, "marginOfError": - 0.016}
        }
        
        params = parameters[moveType] # entramos a un diccionario
        squares = params["factor"] * squares + params["marginOfError"] # de tiempo a casillas
        
        self.hotKey(directionKey, squares, coolodwn=False) # mueve al personaje
    
    def fish(self, area=2482.5, marginOfError=50): # Pescar (el parametro "area" nos indica si no pican)
        self.hotKey(self.button['Rod']) # tira la caña de pescar
        time.sleep(4.5) # espera a que aparezca el mensaje

        coord = self.img.dialogInterfaceCoord
        self.img.imgProcessing(coord,245,255,cv2.THRESH_BINARY_INV,10,10,cv2.MORPH_CLOSE,200,255)
        # hay que procesar la imagen hasta que el mensaje "Hoy no pican" sea un solo contorno
        
        self.hotKey(self.button['A']) # quita la burbuja de dialogo
        
        if self.img.contourAreas: # si hay elementos en la lista
            if (area - marginOfError) <= self.img.contourAreas[0] <= (area + marginOfError): # Hoy no pican
                self.fish() # volvemos a pescar
            else:
                self.randomWait(5.5) # esperamos a que aparezca la interfaz de pelea
        else:
            self.randomWait(5.5)