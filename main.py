import threading

from game.main import Game
from twitch.main import *

input = []


def startGame():
    game = Game()

    game.play()


def connectToChat():
    connectToTwitch()


if __name__ == "__main__":
    threading.Thread(target=startGame).start()
    threading.Thread(target=connectToChat).start()
