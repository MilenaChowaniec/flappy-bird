import pygame as p
import constants as con

class Application:
    def _init_(self):
        p.init()
        self.screen = p.display.set_mode((con.SCREEN_LENGTH, con.SCREEN_HEIGHT))
        p.display.set_caption("flappy bird")
        