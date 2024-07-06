import sys
import os

# Añadir el directorio base del proyecto a sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.images import Images
from api.interaction import Interaction
import cv2
import time

img = Images()
interact = Interaction()

def route(moveType="walk"):
    interact.move(f"{moveType}", f"{interact.button['UP']}", 1)
    interact.hotKey(f"{interact.button['A']}", 8.5)
    interact.move(f"{moveType}", f"{interact.button['UP']}", 9)
    interact.move(f"{moveType}", f"{interact.button['RIGHT']}", 6)
    interact.move(f"{moveType}", f"{interact.button['UP']}", 2)

def magikarpSafariZone(fightInterface=9042, coord=img.fightInterfaceCoord, quitPokemonCoord=[1193,390]):
    route()
    safariBall = 30 # total de safariBalls
    capture = False # True/False = safariBall/roca
    
    interact.fish() # Tira la caña
    
    while safariBall > 0:
        
        img.imgProcessing(coord,50,255,cv2.THRESH_BINARY_INV,45,45,cv2.MORPH_CLOSE,100,255)
        
        if fightInterface in img.contourAreas: # estamos peleando
            if not capture: # tiramos una roca
                interact.hotKey(interact.button['DOWN']) # selecciona la roca
                interact.hotKey(interact.button['A']) # arroja la roca (se puede escapar)
                
                capture = True # cambiamos el tipo de turno
                
                time.sleep(3.5) # espera el siguiente turno
            
            else: # tiramos safariBall
                interact.hotKey(interact.button['A']) # arroja safariBall
                safariBall -= 1 # perdemos una safariBall
                capture = False # turno roca
                time.sleep(13) # espera el final del combate
                interact.click(quitPokemonCoord) # quita la interfaz del pokemon capturado
                
                if safariBall > 0: # si aún nos quedan safariBall
                    interact.fish() # vuelve a pescar
                
                else: # si ya no nos quedan safariBall
                    interact.hotKey(interact.button['A'], 2.3) # quita el dialogo del fin del safari
        
        else: # no estamos peleando
            capture = False # resetea el turno
            interact.fish() # pesca de nuevo
    
if __name__ == "__main__":
    magikarpSafariZone()