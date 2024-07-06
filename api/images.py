import pyautogui as pg
import cv2
import numpy as np
import os

class Images():
    def __init__(self):
        pg.FAILSAFE = False # previene errores
        self.ss_path = "Photos\\foto.png" # ruta para guardar screenshots
        
        # Siguiendo este orden: [x, y, height, with]
        # Interfaz de dialogo, juego pantalla completa sin bordes: [521, 109, 878, 126]
        # Interfaz de dialogo, juego pantalla completa sin bordes recortado: [555, 135, 799, 97]
        self.dialogInterfaceCoord = [555, 135, 799, 97]
        
        # Interfaz de pelea, juego pantalla completa sin bordes: [290, 673, 425, 110]
        self.fightInterfaceCoord = [290, 673, 425, 110]
        
    def imgProcessing(self, coordinates, thresh, maxval, th_type, shape1, shape2, morph_type, th1, th2):
        if coordinates: # si hay coordenadas  
            x , y, height, width = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            ss = pg.screenshot(region=(x, y, height, width)) # toma una foto en tales coordenadas
        else:
            ss = pg.screenshot()

        ss.save(self.ss_path)

        img = cv2.imread(self.ss_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, th = cv2.threshold(gray, thresh, maxval, th_type)

        kernel = np.ones((shape1, shape2), np.uint8)
        closing = cv2.morphologyEx(th, morph_type, kernel)

        border = cv2.Canny(closing, th1, th2)
        contours, _ = cv2.findContours(border, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        self.contourAreas = [] # guarda las áreas de los contornos

        for contour in contours:
            area = cv2.contourArea(contour) # saca el área del contorno
            self.contourAreas.append(area) # guarda el área
        
        os.remove(self.ss_path)
