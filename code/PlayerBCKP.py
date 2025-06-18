import pygame
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT
from code.Entity import Entity
from code.PlayerShotBCKP import PlayerShot

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[PLAYER_KEY_LEFT]:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if keys[PLAYER_KEY_RIGHT]:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.top))
        return None

# O que foi ajustado: ✔ Movimentação horizontal apenas (esquerda/direita), como no Megamania. ✔ Sistema de disparo funcional, ativado pelo botão de tiro (K_SPACE). ✔ Limitação de taxa de tiro com shot_delay, equilibrando o combate.

# Onde substituir assets: 🔹 Imagem do jogador (PNG) → ./asset/Player.png. 🔹 Som dos tiros (MP3) → ./asset/PlayerShoot.mp3.