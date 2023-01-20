import pygame, sys
from random import randint
pygame.init()

from settings import *
from textbox import Textbox
from word import Word

textbox = Textbox(FONT, SCREEN, 'lightskyblue', (100, 600), (136, 32))


def main():
    global spawn_counter
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    textbox.text = textbox.text[0:-1]
                elif event.key == pygame.K_RETURN:
                    if textbox.text in word_list:
                        deleted_word_index = word_list.index(textbox.text)
                        word_list.remove(textbox.text)
                        word_group.sprites()[deleted_word_index].kill()
                        spawn_counter -= 1
                        textbox.text = ''
                else:
                    if len(textbox.text) < 10:
                        textbox.text += event.unicode
            
            if event.type == spawn_word:
                word = Word(FONT, "green", data["word_list"][randint(0, 999)], (1200, randint(50, 650)), (136, 32))
                word_group.add(word)
                word_list.append(word_group.sprites()[spawn_counter].word)
                spawn_counter += 1
        
        SCREEN.fill((40, 40 ,40))
        
        textbox.render()
        
        word_group.draw(SCREEN)
        word_group.update()
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
