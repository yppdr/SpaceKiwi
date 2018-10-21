import platform
from random import randint

from pygame import *

from constant import *
import os

class Ship(sprite.Sprite):
    def __init__(self, game):
        sprite.Sprite.__init__(self)
        self.game = game
        self.image = IMAGES[SHIP]
        self.rect = self.image.get_rect(topleft=(375, 540))
        self.speed = 5
        self.orientation = 'UP'
        self.placement = 'BOTTOM'

    def update(self, keys, *args):
        # if self.rect.y + 200 > self.rect.y and self.rect.y - 200 < self.rect.y and self.rect.x < self.rect.y:
        #     self.placement = 'LEFT_SIDE'
        # elif self.rect.y + 200 > self.rect.y and self.rect.y - 200 < self.rect.y and self.rect.x > self.rect.y:
        #     self.placement = 'RIGHT_SIDE'
        # elif self.rect.y < self.rect.y:
        #     self.placement = 'ABOVE'
        # elif self.rect.y > self.rect.y:
        #     self.placement = 'BOTTOM'
        
        random_placement = randint(0, 4)
        if random_placement == 0:
            self.placement = 'BOTTOM'
        elif random_placement == 1:
            self.placement = 'LEFT_SIDE'
        elif random_placement == 2:
            self.placement = 'ABOVE'
        elif random_placement == 3:
            self.placement = 'RIGHT_SIDE'

        if platform.system() == 'Windows':
            if keys[K_q]:
                self.image = transform.rotate(self.image, -90)
                if self.orientation == 'UP':
                    self.orientation = 'LEFT'
                elif self.orientation == 'LEFT':
                    self.orientation = 'DOWN'
                elif self.orientation == 'DOWN':
                    self.orientation = 'RIGHT'
                elif self.orientation == 'RIGHT':
                    self.orientation = 'UP'
            if keys[K_e]:
                self.image = transform.rotate(self.image, 90)
                if self.orientation == 'UP':
                    self.orientation = 'RIGHT'
                elif self.orientation == 'RIGHT':
                    self.orientation = 'DOWN'
                elif self.orientation == 'DOWN':
                    self.orientation = 'LEFT'
                elif self.orientation == 'LEFT':
                    self.orientation = 'UP'
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
                if self.orientation == 'UP':
                    self.orientation = 'LEFT'
                elif self.orientation == 'LEFT':
                    self.orientation = 'DOWN'
                elif self.orientation == 'DOWN':
                    self.orientation = 'RIGHT'
                elif self.orientation == 'RIGHT':
                    self.orientation = 'UP'
            if keys[K_e]:
                self.image = transform.rotate(self.image, 90)
                if self.orientation == 'UP':
                    self.orientation = 'RIGHT'
                elif self.orientation == 'RIGHT':
                    self.orientation = 'DOWN'
                elif self.orientation == 'DOWN':
                    self.orientation = 'LEFT'
                elif self.orientation == 'LEFT':
                    self.orientation = 'UP'
            if keys[K_q] and self.rect.x > 10:
                self.rect.x -= self.speed
            if keys[K_d] and self.rect.x < 740:
                self.rect.x += self.speed
            if keys[K_z] and self.rect.y > 10:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < 550:
                self.rect.y += self.speed

        self.game.screen.blit(self.image, self.rect)
