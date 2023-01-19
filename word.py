from pygame import sprite, Surface, Rect

class Word(sprite.Sprite):
    def __init__(self, font, colour, word, position, scale):
        super().__init__()
        self.font = font
        self.text_surf = self.font.render(word, 1, colour)
        self.image = Surface(scale).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = Rect(position, scale)
        
        self.image.blit(self.text_surf, (10, 10))
    
    def update(self):
        self.rect.x -= 2

