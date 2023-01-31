import pygame, sys
from random import randint
pygame.init()

from settings import *
from textbox import Textbox
from word import Word
from counter import Counter

textbox = Textbox(FONT, SCREEN, (40, 40, 40), (SCREEN_WIDTH/2, 650), (240, 32))

bottom_section = pygame.Surface((1200, 100))
bottom_section.fill((25, 25, 25))

score_counter = Counter(FONT, "Score", 0, "green", (20, 20), (240, 32))
health_counter = Counter(FONT, "Health", 3, "green", (20, 60), (240, 32))
counter_group = pygame.sprite.Group()
counter_group.add(score_counter, health_counter)

def main():
    global spawn_counter
    game_states["Gameplay"] = True
    
    while True:

        SCREEN.fill((40, 40, 40))
        SCREEN.blit(bottom_section, (0, 600))
        
        textbox.render()
        
        if game_states["Main Menu"]:
            pass
        
        if game_states["Gameplay"]:
            word_group.draw(SCREEN)
            word_group.update()
            
            counter_group.update()
            counter_group.draw(SCREEN)
        
        if game_states["Game Lose"]:
            draw_text(FONT, "green", "You Lose!", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30), 64)
            draw_text(FONT, "green", f"Score: {score_counter.value}", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30), 64)
            
            draw_text(FONT, "green", "Type \"restart\" to play again!", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100))
        
         
        for event in pygame.event.get():
            if game_states["Gameplay"]:
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
                            score_counter.value += len(textbox.text) * 10
                            textbox.text = ''
                    else:
                        if len(textbox.text) < 20:
                            textbox.text += event.unicode
                        else:
                            print(textbox.image.get_width())
                
                if event.type == spawn_word:
                    word = Word(FONT, "green", data["word_list"][randint(0, 999)], (1200, randint(50, 550)))
                    word_group.add(word)
                    word_list.append(word_group.sprites()[spawn_counter].word)
                    spawn_counter += 1
            
                if spawn_counter > 0:
                    if word_group.sprites()[0].rect.x <= 0:
                        word_group.sprites()[0].kill()
                        del word_list[0]
                        spawn_counter -= 1
                        health_counter.value -= 1
                        if health_counter.value == 0:
                            word_group.empty()
                            word_list.clear()
                            spawn_counter = 0
                            game_states["Gameplay"] = False
                            game_states["Game Lose"] = True
            
            
            if game_states["Game Lose"]:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        textbox.text = textbox.text[0:-1]
                    elif event.key == pygame.K_RETURN:
                        if textbox.text == "restart":
                            score_counter.value = 0
                            health_counter.value = 3
                            textbox.text = ''
                            game_states["Gameplay"] = True
                            game_states["Game Lose"] = False
                    else:
                        if len(textbox.text) < 20:
                            textbox.text += event.unicode
                        else:
                            print(textbox.image.get_width())
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
