import platform

from pygame import *

from constant import *
import os

class Ship(sprite.Sprite):
    def __init__(self, game):
        sprite.Sprite.__init__(self)
        self.game = game
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(375, 540))
        self.speed = 5

    def update(self, keys, *args):
        if platform.system() == 'Windows':
            if keys[K_q]:
                self.image = transform.rotate(self.image, -90)
            if keys[K_e]:
                self.image = transform.rotate(self.image, 90)
            if keys[K_a] and self.rect.x > 10:
                self.rect.x -= self.speed
            if keys[K_d] and self.rect.x < 740:
                self.rect.x += self.speed
            if keys[K_w] and self.rect.y > 10:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < 550:
                self.rect.y += self.speed
        else:
            if keys[K_a]:
                self.image = transform.rotate(self.image, -90)
                print(self.image)
            if keys[K_e]:
                self.image = transform.rotate(self.image, 90)
            if keys[K_q] and self.rect.x > 10:
                self.rect.x -= self.speed
            if keys[K_d] and self.rect.x < 740:
                self.rect.x += self.speed
            if keys[K_z] and self.rect.y > 10:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < 550:
                self.rect.y += self.speed

        self.game.screen.blit(self.image, self.rect)
