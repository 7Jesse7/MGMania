from code.Const import ENTITY_SPEED
from code.Entity import Entity

class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]  # Movimento dos tiros dos inimigos para baixo

# O que foi ajustado: ✔ Movimentação vertical, fazendo com que os tiros do inimigo desçam pela tela. ✔ Herança da classe Entity, garantindo que os disparos interajam corretamente no jogo.

# Onde substituir assets: 🔹 Imagem do tiro dos inimigos (PNG) → ./asset/EnemyShot.png. 🔹 Som dos disparos (MP3) → ./asset/EnemyShoot.mp3.