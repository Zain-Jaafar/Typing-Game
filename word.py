from pygame import sprite, Surface, Rect

class Word(sprite.Sprite):
    def __init__(self, font, colour, word, position, scale):
        super().__init__()
        self.word = word
        self.text_surf = font.render(self.word, False, colour)
        self.image = Surface(scale).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = Rect(position, scale)
        
        self.image.blit(self.text_surf, (10, 10))
    
    def update(self):
        self.rect.x -= 2

