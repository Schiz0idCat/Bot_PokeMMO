import pydirectinput as pd
import pyautogui as pg
import time
import cv2
import numpy as np
import os
import random
import math


pg.FAILSAFE = False

def hotkey(key, hold_time=.1):
    pd.keyDown(key)
    time.sleep(hold_time)
    pd.keyUp(key)


class Bot():
    def __init__(self):
        self.ss_path = "Others\\Photos\\screenshot.png"
        
        # Set your own configurations here
        self.button = { 
            'A' : 'z',
            'B' : 'x',
            'Rod' : '4',
            'UP' : 'up',
            'DOWN' : 'down',
            'LEFT' : 'left',
            'RIGHT' : 'right'
        }

        # For magikarp bot
        self.safariballs = 30
        self.turn = False

    def move(self, move_type, direction_key, squares=1):
        if move_type == "walk":
            pd.keyDown(direction_key)
            time.sleep(0.2346 * squares - 0.009)
            pd.keyUp(direction_key)

        elif move_type == "run":
            pd.keyDown(direction_key)
            time.sleep(0.18325 * squares - 0.13)
            pd.keyUp(direction_key)

        elif move_type == "bike": # Likely to fail (because of high speed and delay of server)
            pd.keyDown(direction_key)
            time.sleep(0.08286 * squares - 0.016)
            pd.keyUp(direction_key)

    def image_processing(self, thresh, maxval, th_type, shape1, shape2, morph_type, th1, th2):
        ss = pg.screenshot()
        ss.save(self.ss_path)

        self.img = cv2.imread(self.ss_path)
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        _, th = cv2.threshold(gray, thresh, maxval, th_type)

        kernel = np.ones((shape1, shape2), np.uint8)
        closing = cv2.morphologyEx(th, morph_type, kernel)

        border = cv2.Canny(closing, th1, th2)
        self.countours, _ = cv2.findContours(border, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        self.contour_area = []

        for i in range(len(self.countours)):
            area = cv2.contourArea(self.countours[i])
            self.contour_area.append(area)


    def pixel_counter(self, img, contour, BGR_color):
        total = 0

        if len(contour) >= 3:
            x, y, w, h = cv2.boundingRect(contour)
            x, y, w, h = max(0, x), max(0, y), w, h

            x, y, w, h = min(x, img.shape[1]), min(y, img.shape[0]), min(w, img.shape[1] - x), min(h, img.shape[0] - y)

            contour_region = img[y:y+h, x:x+w]

            for row in contour_region:
                for pixel in row:
                    if all(pixel[:3] == BGR_color):
                        total += 1

        return total


    def random_wait(self, initial_number, negative_exponential_distribution=4.5, num_increments=11, base_increase=0.2):
        increments = [round(base_increase * i, 1) for i in range(0, num_increments)]
        probabilities = [2 * negative_exponential_distribution * math.exp(-negative_exponential_distribution * x) for x in increments]
        probabilities_sum = sum(probabilities)
        probabilities = [p / probabilities_sum for p in probabilities]

        increase = random.choices(increments, probabilities)[0]

        time_to_wait = max(initial_number, initial_number + increase)

        time.sleep(time_to_wait)

    def fish(self):
        pg.hotkey(self.button['Rod'], self.button['Rod'], interval=.1)

        time.sleep(4.5) ### TEXTO
        self.image_processing(245, 255, cv2.THRESH_BINARY_INV, 10, 10, cv2.MORPH_CLOSE, 200, 255)

        dialog_interface = 108400 # Discriminates the area of ​​the dialog box

        for i, contour in enumerate(self.countours): # Checks if we fish or not
            area = self.contour_area[i]

            if area > dialog_interface:
                bgr = np.array([34, 34, 34])
                quantity = self.pixel_counter(self.img, contour, bgr)

                if quantity < 1000: # If we are not fighting
                    self.random_wait(0)
                    pg.hotkey(self.button['A'], self.button['A'], interval=.1)
                    self.fish() # We fish again
                    break

                else: # If we are fighting
                    pg.hotkey(self.button['A'], self.button['A'], interval=.1)
                    self.random_wait(5.5) # We wait to the fight interface
                    break

    def magikarp(self):
        fight_interface = 9042 # Discriminates the fighting interface area
        self.image_processing(50,255,cv2.THRESH_BINARY_INV,45,45,cv2.MORPH_CLOSE,100,255)

        if fight_interface in self.contour_area: # Checks if we are fighting or not
            if self.turn == False: # You have to throw a rock
                self.random_wait(0)
                hotkey(self.button['DOWN']) # Selects the rock

                self.random_wait(0)
                pg.hotkey(self.button['A'], self.button['A'], interval=.1) # Throws the rock

                self.turn = True # Switches to the capture turn

                self.random_wait(3.5) # Waits for the next turn
                self.magikarp() # Checks if we are still in combat

            else: # You have to capture
                pg.hotkey(self.button['A'], self.button['A'], interval=.1) # Throws a safariBall

                self.safariballs -= 1 # We lost a ZafariBall
                self.turn = False # Switches to the rock turn

                self.random_wait(13) # Waits for the fight to end

                if self.safariballs != 0: # Prevents the end of the safari
                    self.random_wait(0)
                    pg.moveTo(1193,390) # Coordinate to remove the interface
                    pg.click()

                    self.magikarp() # Returns to fishing

                else: # Reacts to the end of the safari
                    self.random_wait(0)
                    pg.hotkey(self.button['A'], self.button['A'], interval=1) # Remove the dialogue

                    self.random_wait(0)
                    pg.moveTo(1193,390) # Coordinate to remove an interface
                    pg.click()

                    self.safariballs = 30 # This prepare for an infinite loop

                    os.remove(self.ss_path) # Delete the photo

        else: # If we are not fighting
            self.turn = False # Switches to the rock turn

            self.random_wait(0)
            self.fish() # Go fishing again

            self.magikarp() # Activates the bot
