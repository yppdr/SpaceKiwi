from pygame import *

from constant import *

class Bullet(sprite.Sprite):
    def __init__(self, xpos, ypos, direction, speed, filename, side, game):
        sprite.Sprite.__init__(self)
        self.game = game
        self.image = IMAGES[filename]
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.speed = speed
        self.direction = direction
        self.side = side
        self.filename = filename

    def update(self, keys, *args):
        self.game.screen.blit(self.image, self.rect)
        
        # gestion direction du tir
        if self.direction == 'UP':
            self.rect.y += self.speed * -1
        if self.direction == 'LEFT':
            self.rect.x += self.speed
        if self.direction == 'DOWN':
            self.rect.y += self.speed
        if self.direction == 'RIGHT':
            self.rect.x += self.speed * -1

        if self.rect.y < 15 or self.rect.y > 600 or self.rect.x < 15 or self.rect.x > 600:
            self.kill()
