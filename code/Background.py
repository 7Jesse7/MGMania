from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity
import pygame

class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.image = pygame.image.load("../asset/Menu.png").convert_alpha()  # Carrega o fundo
        self.rect = self.image.get_rect(topleft=position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

