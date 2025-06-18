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

# O que foi mantido e ajustado: ✔ Classe Entity usada como base, permitindo que Player, Enemy, PlayerShot e EnemyShot herdem dela. ✔ Método move() pode ser sobrescrito, garantindo flexibilidade para diferentes tipos de entidades. ✔ Método update() chamado no loop do jogo, permitindo atualização automática da posição. ✔ Cada entidade carrega sua imagem automaticamente, baseada no nome (./asset/{name}.png).

# Onde substituir assets: 🔹 Imagens das entidades (PNG) → ./asset/Player.png, ./asset/Enemy.png, ./asset/PlayerShot.png, ./asset/EnemyShot.png.