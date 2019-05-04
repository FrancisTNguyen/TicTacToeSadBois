import pygame

from framework.scene import Scene
from framework.text import Text


class MenuScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director, background)

        menu_rect = pygame.Rect(0, 0, 100, 30)

        menu_rect.center = director.screen.get_rect().center

        self.play = Text(
            menu_rect, 30, director.regular_text_color, director.screen, "WAITING FOR OPONENTS TYPE !play TO PLAY")

    def keydown(self, key):
        if key == pygame.K_p:
            self.director.set_scene("game")

    def render(self):
        super().render()

        self.play.render()
