from pygame import *

from constant import *

class Ship(sprite.Sprite):
    def __init__(self, game):
        sprite.Sprite.__init__(self)
        self.game = game
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(375, 540))
        self.speed = 5

    # def rot_center(image, rect, angle):
    #     rot_image = pygame.transform.rotate(image, angle)
    #     rot_rect = rot_image.get_rect(center=rect.center)
    #     return rot_image,rot_rect

    def update(self, keys, *args):
        if keys[K_d] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_q] and self.rect.x < 740:
            self.rect.x += self.speed
        if keys[K_z] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
        # change rotation of image
        # if keys[K_a]
        #     self.image
        # if keys[K_e]

        self.game.screen.blit(self.image, self.rect)
