import pygame
from code.Const import ENTITY_SPEED
from code.Entity import Entity

class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def update(self):
        """ Movimenta o tiro para cima """
        self.rect.centery -= ENTITY_SPEED[self.name]  # Move o tiro para cima

        # Remove o tiro se sair da tela
        if self.rect.bottom < 0:
            self.kill()  # Remove o tiro do jogo
