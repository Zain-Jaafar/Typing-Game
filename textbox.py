from pygame import Rect, draw

class Textbox():
    def __init__(self, font, display_surface, colour, position, scale):
        self.font = font
        self.text = ''
        self.colour = colour
        self.display = display_surface
        
        self.rect = Rect(position, scale)
    
    def render(self):
        self.image = self.font.render(self.text, False, 'black')
        draw.rect(self.display, self.colour, self.rect)
        self.display.blit(self.image, (self.rect.x + 5, self.rect.y + 10))
        