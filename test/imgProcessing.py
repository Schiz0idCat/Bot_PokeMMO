import pyautogui as pg
import pydirectinput as pd
import cv2
import numpy as np
import os

def switchWindow():
    pd.keyDown('alt')
    pd.press('tab')
    pd.keyUp('alt')

def imgProcessing(coordinates, thresh, maxval, th_type, shape1, shape2, morph_type, th1, th2):
    ss_path = "Photos\\photoExp.png"
    
    if coordinates: # si hay coordenadas  
        x , y, height, width = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
        ss = pg.screenshot(region=(x, y, height, width)) # toma una foto en tales coordenadas
    else:
        ss = pg.screenshot()

    ss.save(ss_path)

    img = cv2.imread(ss_path)
    imgCopy = cv2.imread(ss_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, thresh, maxval, th_type)
    
    kernel = np.ones((shape1, shape2), np.uint8)
    closing = cv2.morphologyEx(th, morph_type, kernel)
    
    border = cv2.Canny(closing, th1, th2)
    contours, _ = cv2.findContours(border, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    contourAreas = [] # guarda las áreas de los contornos

    for contour in contours:
        area = cv2.contourArea(contour) # saca el área del contorno
        contourAreas.append(area) # guarda el área
        
        cv2.drawContours(img, [contour], -1, (0, 255, 0), 2) # dibuja contornos
        M = cv2.moments(contour) # Momento de los contornos
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"]) # coordenada x
            cY = int(M["m01"] / M["m00"]) # coordenada y
            # Muestra el área del contorno en la imagen
            cv2.putText(img, f'{int(area)}', (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    print(f"Las áreas encontradas son: \n{contourAreas}")

    # Mostrar imágenes
    cv2.imshow('Original', imgCopy)
    cv2.imshow('Escala de Grises', gray)
    cv2.imshow('Umbralización', th)
    cv2.imshow('Operación Morfológica', closing)
    cv2.imshow('Bordes', border)
    cv2.imshow('Original con bordes', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    os.remove(ss_path)

switchWindow()
imgProcessing([555, 135, 799, 97], 245, 255, cv2.THRESH_BINARY_INV, 10, 10, cv2.MORPH_CLOSE, 200, 255)
