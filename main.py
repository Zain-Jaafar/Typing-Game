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
    global spawn_counter, word_speed, score_multiplier, new_highscore
    game_states["Main Menu"] = True
    
    while True:

        SCREEN.fill((40, 40, 40))
        SCREEN.blit(bottom_section, (0, 600))
        
        textbox.render()
        
        if game_states["Main Menu"]:
            word_group.empty()
            word_list.clear()
            spawn_counter = 0
            draw_text(FONT, "green", "Typing Game", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 200), 72)
            draw_text(FONT, "green", "Type \"start\" to play!", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50), 48)
            draw_text(FONT, "green", "Type \"highscore\" to view the highscore!", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 48)
            
        
        if game_states["Gameplay"]:
            word_group.draw(SCREEN)
            word_group.update()
            
            counter_group.update()
            counter_group.draw(SCREEN)
        
        if game_states["Game Lose"]:
            if data["highscore"] < score_counter.value:
                data["highscore"] = score_counter.value
                new_highscore = True
            
                with open("data.json", "w") as file:
                    json.dump(data, file)
            
            word_group.empty()
            word_list.clear()
            spawn_counter = 0
            draw_text(FONT, "green", "You Lose!", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30), 64)
            draw_text(FONT, "green", f"Score: {score_counter.value}", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30), 64)
            
            draw_text(FONT, "green", "Type \"start menu\" return to the start menu!", (SCREEN_WIDTH/2, 500))
            draw_text(FONT, "green", "Type \"restart\" to play again!", (SCREEN_WIDTH/2, 550))

            if new_highscore:
                draw_text(FONT, "green", "New Highscore!", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 75), 48)
            
        if game_states["Highscore"]:
            draw_text(FONT, "green", f"Highscore: {data['highscore']}", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 64)
            
            draw_text(FONT, "green", "Type \"start menu\" return to the start menu!", (SCREEN_WIDTH/2, 550))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    textbox.text = textbox.text[0:-1]
                elif event.key == pygame.K_RETURN:
                    if game_states["Gameplay"]:
                        if textbox.text in word_list:
                            deleted_word_index = word_list.index(textbox.text)
                            word_list.remove(textbox.text)
                            word_group.sprites()[deleted_word_index].kill()
                            spawn_counter -= 1
                            score_counter.value += len(textbox.text) * 10 * score_multiplier
                            textbox.text = ''
                    
                    elif game_states["Main Menu"]:
                        if textbox.text == "start":
                            game_states["Main Menu"] = False
                            game_states["Gameplay"] = True
                            textbox.text = ''
                        
                        elif textbox.text == "highscore":
                            game_states["Highscore"] = True
                            game_states["Main Menu"] = False
                            textbox.text = ''
                    
                    elif game_states["Game Lose"]:
                        if textbox.text == "restart":
                            score_counter.value = 0
                            health_counter.value = 3
                            word_speed = 1
                            new_highscore = False
                            textbox.text = ''
                            game_states["Gameplay"] = True
                            game_states["Game Lose"] = False
                            
                        elif textbox.text == "start menu":
                            score_counter.value = 0
                            health_counter.value = 3
                            word_speed = 1
                            new_highscore = False
                            game_states["Main Menu"] = True
                            game_states["Game Lose"] = False
                            textbox.text = ''
                    
                    elif game_states["Highscore"]:
                        if textbox.text == "start menu":
                            game_states["Main Menu"] = True
                            game_states["Highscore"] = False
                            textbox.text = ''
                    
                else:
                    if len(textbox.text) < 20:
                        textbox.text += event.unicode
            
            if event.type == spawn_word:
                word = Word(FONT, "green", data["word_list"][randint(0, 999)], (1200, randint(50, 550)), word_speed)
                word_group.add(word)
                word_list.append(word_group.sprites()[spawn_counter].word)
                spawn_counter += 1
        
            if game_states["Gameplay"]:
                if event.type == speed_up:
                    word_speed += 0.5
                    score_multiplier += 1
        
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
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
