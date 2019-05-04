from framework.director import Director
from .menu_scene import MenuScene
from .game_scene import GameScene


class Game:
    def __init__(self):
        self.director = Director((1280, 720), 'TicTacToe')

        self.menu_scene = MenuScene(self.director)
        self.game_scene = GameScene(self.director)

        self.director.scene_list = {
            'menu': self.menu_scene,
            'game': self.game_scene,
        }

        self.director.set_scene('menu')

    def play(self):
        self.director.loop()
