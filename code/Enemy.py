import pygame
from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED
from code.Entity import Entity
from code.EnemyShot import EnemyShot

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_timer = ENTITY_SHOT_DELAY[self.name]  # Tempo inicial entre disparos
        self.health = 1  # Vida do inimigo

    def take_damage(self):
        """ Reduz a vida do inimigo ao receber dano """
        self.health -= 1
        if self.health <= 0:
            self.kill()  # Remove o inimigo do jogo

    def update(self):
        """ Movimenta o inimigo e dispara automaticamente """
        self.rect.centery += ENTITY_SPEED[self.name]  # Movimenta o inimigo para baixo

        # Reduz o temporizador de tiro a cada frame
        if self.shot_timer > 0:
            self.shot_timer -= 1

        # Se o tempo de recarga zerar, dispara um tiro
        if self.shot_timer <= 0:
            self.shot_timer = ENTITY_SHOT_DELAY[self.name]  # Reinicia o atraso entre tiros
            shot = EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.bottom))
            self.groups()[0].add(shot)  # Adiciona o tiro ao grupo de sprites
