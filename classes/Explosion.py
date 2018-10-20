from pygame import *

from Text import *
from constant import *
class Explosion(sprite.Sprite):
    def __init__(self, xpos, ypos, row, ship, mystery, score, game):
        sprite.Sprite.__init__(self)
        self.isMystery = mystery
        self.game = game
        self.isShip = ship
        if mystery:
            self.text = Text(FONT, 20, str(score), WHITE, xpos + 20, ypos + 6)
        elif ship:
            self.image = IMAGES['ship']
            self.rect = self.image.get_rect(topleft=(xpos, ypos))
        else:
            self.row = row
            self.load_image()
            self.image = transform.scale(self.image, (40, 35))
            self.rect = self.image.get_rect(topleft=(xpos, ypos))
            self.game.screen.blit(self.image, self.rect)

        self.timer = time.get_ticks()

    def update(self, keys, currentTime):
        passed = currentTime - self.timer
        if self.isMystery:
            if passed <= 200:
                self.text.draw(self.game.screen)
            elif 400 < passed <= 600:
                self.text.draw(self.game.screen)
            elif passed > 600:
                self.kill()
        elif self.isShip:
            if 300 < passed <= 600:
                self.game.screen.blit(self.image, self.rect)
            elif passed > 900:
                self.kill()
        else:
            if passed <= 100:
                self.game.screen.blit(self.image, self.rect)
            elif 100 < passed <= 200:
                self.image = transform.scale(self.image, (50, 45))
                self.game.screen.blit(self.image,
                                 (self.rect.x - 6, self.rect.y - 6))
            elif passed > 400:
                self.kill()

    def load_image(self):
        imgColors = ['purple', 'blue', 'blue', 'green', 'green']
        self.image = IMAGES['explosion{}'.format(imgColors[self.row])]
