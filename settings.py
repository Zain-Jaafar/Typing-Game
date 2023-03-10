import pygame, json


clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

FLAGS = pygame.DOUBLEBUF | pygame.HWSURFACE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FLAGS)
pygame.display.set_caption('Typing Game')

FONT = pygame.font.Font('Fonts/Pixeltype.ttf', 32)

with open('data.json') as file:
    data = json.load(file)

word_group = pygame.sprite.Group()
word_list = []
word_speed = 1
spawn_counter = 0

spawn_word = pygame.USEREVENT
pygame.time.set_timer(spawn_word, 2000)

speed_up = pygame.USEREVENT + 1
pygame.time.set_timer(speed_up, 20000)

game_states = {
    "Main Menu": False,
    "Gameplay": False,
    "Options": False,
    "Highscore": False,
    "Game Lose": False
}

score_multiplier = 1

new_highscore = False

def draw_text(font, colour, text, position, text_size=32):
    font = pygame.font.Font('Fonts/Pixeltype.ttf', text_size)
    text_surf = font.render(text, False, colour)
    text_rect = pygame.Rect((0, 0), (text_surf.get_size()))
    text_rect.center = position
    SCREEN.blit(text_surf, text_rect)