from pygame import *

from constant import *

class Bullet(sprite.Sprite):
    def __init__(self, xpos, ypos, orientation, speed, filename, side, game, placement):
        sprite.Sprite.__init__(self)
        self.game = game
        self.image = IMAGES[filename]
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.speed = speed
        self.orientation = orientation
        self.side = side
        self.filename = filename
        if filename == 'enemylaser':
            if placement == 'LEFT_SIDE':
                self.orientation = 'RIGHT'
            elif placement == 'RIGHT_SIDE':
                self.orientation = 'LEFT'
            elif placement == 'ABOVE':
                self.orientation = 'UP'
            elif placement == 'BOTTOM':
                self.orientation = 'DOWN'

    def update(self, keys, *args):
        self.game.screen.blit(self.image, self.rect)
        
        # gestion orientation du tir
        if self.orientation == 'UP':
            self.rect.y += self.speed * -1
        elif self.orientation == 'LEFT':
            self.rect.x += self.speed
        elif self.orientation == 'DOWN':
            self.rect.y += self.speed
        elif self.orientation == 'RIGHT':
            self.rect.x += self.speed * -1

        if self.rect.y < 15 or self.rect.y > 600 or self.rect.x < 15 or self.rect.x > 800:
            self.kill()
