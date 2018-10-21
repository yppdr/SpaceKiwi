from random import randint

from pygame import *
from os.path import abspath, dirname

from constant import *

BASE_PATH = abspath(dirname(__file__))
FONT_PATH = BASE_PATH + '/../fonts/'
IMAGE_PATH = BASE_PATH + '/../images/'
SOUND_PATH = BASE_PATH + '/../sounds/'

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (124, 57, 2)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)
SHIP = str(randint(1,3))

SCREEN = display.set_mode((800, 600))
FONT = FONT_PATH + 'space_invaders.ttf'
IMG_NAMES = [SHIP , 'mystery',
             'enemy1_1', 'enemy1_2',
             'enemy2_1', 'enemy2_2',
             'enemy3_1', 'enemy3_2',
             'explosionblue', 'explosiongreen', 'explosionpurple',
             'laser', 'laserfraise', 'laserbanane', 'laserkiwi', 'enemylaser']
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES}
