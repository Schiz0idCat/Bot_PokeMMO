This is a bot that automates the capture of magikarps in the Safari Zone in PokeMMO.

## Configurations

### Configure buttons in game_interaction.py
On line 24 in the file named *game_interaction.py* you will see a dictionary named *self.button* that stores the button settings, adjust it to your convenience:
```python
class Bot():
    def __init__(self):
        self.ss_path = "Main\\ss.png"

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
```

### Graphics and game configurations
This is my first project with image management, so the bot is pretty sensitive to what happens on screen, so I recommend the following settings for the correct functioning of the bot.

you have to configure the game in the conditions in which the bot was tested:

1.- The resolution of your monitor has to be 1920x1080.

2.- The game resolution has to be 1024x768 and be in windowed mode.

3.- The fps should be higher than 30.

4.- The game theme has to be the default one.

5.- The text speed has to be x4.

6.- The battle windows size has to set in 100

### Bot operation

1.- The bot has to be run from the *bot.py* file and by default captures only 30 magikarps.

2.- If you don't want the bot to be in an infinite loop you have to make it start in the lake so that the character starts fishing.
![](https://raw.githubusercontent.com/Schiz0idCat/Bot_PokeMMO/main/Others/Photos/lake.png)

But if you want the bot to be in an infinite loop you have to make it start at the entrance of the Safari Zona (before paying for the entrance).
![](https://raw.githubusercontent.com/Schiz0idCat/Bot_PokeMMO/main/Others/Photos/pay.png)

3.- By default the bot considers that the character moves walking (so make sure that your character doesn't move running).

4.- If you configure the bot to be in an infinite loop it could fail after a while by problems with the server lag.