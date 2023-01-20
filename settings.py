import pygame, json


clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

FLAGS = pygame.DOUBLEBUF | pygame.HWSURFACE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Typing Game')

FONT = pygame.font.Font('Fonts/Pixeltype.ttf', 32)

with open('data.json') as file:
    data = json.load(file)

word_group = pygame.sprite.Group()
word_list = []
spawn_counter = 0

spawn_word = pygame.USEREVENT
pygame.time.set_timer(spawn_word, 2000)