from pygame import *

from constant import *

class Ship(sprite.Sprite):
    def __init__(self, game):
        sprite.Sprite.__init__(self)
        self.game = game
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(375, 540))
        self.speed = 5

    def update(self, keys, *args):
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.x > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < 740:
            self.rect.y += self.speed
        self.game.screen.blit(self.image, self.rect)
