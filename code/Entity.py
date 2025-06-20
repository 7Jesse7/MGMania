import pygame
from utils import resource_path

class Entity(pygame.sprite.Sprite):
    def __init__(self, name: str, position: tuple):
        super().__init__()
        self.name = name
        image_path = resource_path("asset/" + name + ".png")  # ✅ Sem "../" e sem "code/"
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=position)

    def move(self):
        pass

    def update(self):
        self.move()


