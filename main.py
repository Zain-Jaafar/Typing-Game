import pygame, sys
pygame.init()

from settings import *
from textbox import Textbox

textbox = Textbox(FONT, SCREEN, "lightskyblue", (100, 600))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                textbox.text = textbox.text[0:-1]
            elif event.key == pygame.K_RETURN:
                print(textbox.text)
                textbox.text = ""
            else:
                if len(textbox.text) <= 10:
                    textbox.text += event.unicode
    
    SCREEN.fill((0, 0 ,0))
    
    textbox.render()
    
    pygame.display.flip()
    clock.tick(FPS)
