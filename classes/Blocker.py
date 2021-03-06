from pygame import *

from constant import *

class Blocker(sprite.Sprite):
    def __init__(self, size, color, row, column, game):
        self.game = game
        sprite.Sprite.__init__(self)
        self.height = size
        self.width = size
        self.color = color
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column

    def update(self, keys, *args):
        self.game.screen.blit(self.image, self.rect)
