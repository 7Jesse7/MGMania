import pygame
import random
from code.Enemy import Enemy
from code.Const import WIN_WIDTH, ENTITY_SPEED

class EntityFactory:
    def __init__(self, sprite_group):
        self.sprite_group = sprite_group

    def spawn_enemy(self):
        enemy_name = "Enemy"
        position = (random.randint(50, WIN_WIDTH - 50), -50)  # Inimigo nasce no topo da tela
        enemy = Enemy(name=enemy_name, position=position)
        self.sprite_group.add(enemy)
        return enemy


#O que foi ajustado: ✔ Criação automática de inimigos, gerando adversários no topo da tela. ✔ Posição aleatória, garantindo variação na movimentação dos inimigos. ✔ Integração com Enemy.py, permitindo que os inimigos se movimentem e ataquem corretamente.

#Onde substituir assets: 🔹 Imagem dos inimigos (PNG) → ./asset/Enemy.png.