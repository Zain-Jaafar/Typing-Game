from pygame import Rect, draw

class Textbox():
    def __init__(self, font, display_surface, colour):
        self.font = font
        self.text = ""
        self.colour = colour
        self.display = display_surface
        
        self.rect = Rect((200, 200), (140, 32))
    
    def render(self):
        self.image = self.font.render(self.text, False, (255, 255, 255))
        draw.rect(self.display, self.colour, self.rect, 2)
        self.display.blit(self.image, (self.rect.x + 5, self.rect.y + 5))
        
        self.rect.w = self.image.get_width() + 10