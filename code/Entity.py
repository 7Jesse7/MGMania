import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, name: str, position: tuple):
        super().__init__()
        self.name = name
        self.image = pygame.image.load("../asset/" + name + ".png").convert_alpha()
        self.rect = self.image.get_rect(center=position)

    def move(self):
        """ Método de movimentação a ser sobrescrito nas classes filhas. """
        pass

    def update(self):
        """ Atualiza posição no jogo, chamado pelo grupo de sprites. """
        self.move()
