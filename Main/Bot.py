from game_interaction import Bot, hotkey
import pyautogui as pg


bot = Bot()

def bot_magikarp(move_type="walk",loop=True):
    if loop:
        while True:
            bot.move(f"{move_type}", f"{bot.button['UP']}")
            hotkey(f"{bot.button['A']}", 8.5)
            bot.move(f"{move_type}", f"{bot.button['UP']}", 9)
            bot.move(f"{move_type}", f"{bot.button['RIGHT']}", 6)
            bot.move(f"{move_type}", f"{bot.button['UP']}", 2)
            bot.magikarp()

    else:
        bot.magikarp()

pg.hotkey("alt", "tab", interval=.1)

bot_magikarp() # Infinite loop
#bot_magikarp(loop=False) # No infinite loop

pg.hotkey("alt", "tab", interval=.1)