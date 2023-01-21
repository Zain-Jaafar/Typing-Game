from pygame import sprite, Rect, Surface

class Counter(sprite.Sprite):
    def __init__(self, font, text, value, colour, position, scale):
        super().__init__()
        self.font = font
        self.text = text
        self.value = value
        self.colour = colour
        self.scale = scale
        self.text_surf = self.font.render(f"{self.text}:  {self.value}", False, self.colour)
        self.image = Surface(scale).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = Rect(position, scale)
        
        self.image.blit(self.text_surf, (10, 10))
    
    def update(self):
        self.text_surf = self.font.render(f"{self.text}:  {self.value}", False, self.colour)
        self.image = Surface(self.scale).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(self.text_surf, (10, 10))