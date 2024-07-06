from api.interaction import Interaction
from bot.MagikarpSafariZone import magikarpSafariZone

interact = Interaction()

class Bot():
    def magikarpSafari(moveType="walk",infinite=False, iterations=1):
        if infinite:
            while True:
                magikarpSafariZone()
        else:
            for _ in range(iterations):
                magikarpSafariZone()

bot = Bot()
interact = Interaction()

if __name__ == "__main__":
    interact.switchWindow()
    bot.magikarpSafari(infinite=True)