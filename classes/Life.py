from pygame import *

from spaceinvaders import *
from constant import *

class Life(sprite.Sprite):
    def __init__(self, xpos, ypos, game):
        sprite.Sprite.__init__(self)
        self.game = game
        self.image = IMAGES['ship']
        self.image = transform.scale(self.image, (23, 23))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, keys, *args):
        self.game.screen.blit(self.image, self.rect)
