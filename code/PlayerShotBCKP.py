from code.Const import ENTITY_SPEED
from code.Entity import Entity

class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery -= ENTITY_SPEED[self.name]  # Movimento dos tiros do jogador para cima
# O que foi ajustado: ✔ Movimentação vertical dos tiros, subindo pela tela como no Megamania. ✔ Herança da classe Entity, garantindo que os tiros do jogador interajam corretamente no jogo.

# Onde substituir assets: 🔹 Imagem dos tiros (PNG) → ./asset/PlayerShot.png. 🔹 Som dos disparos (MP3) → ./asset/PlayerShoot.mp3.