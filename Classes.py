import pygame

class BaseClass(pygame.sprite.Sprite):
    List = pygame.sprite.Group()
    def __init__(self, x_pos, y_pos, image_string):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.image.load(image_string)
        
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

        BaseClass.List.add(self)


class Human(BaseClass):
    def __init__(self, health, x_pos, y_pos, image_string):
        BaseClass.__init__(self, x_pos, y_pos, image_string)
        self.health = health