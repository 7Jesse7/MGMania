from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.image = pygame.image.load("./asset/Background.png").convert_alpha()  # Carrega o fundo
        self.rect = self.image.get_rect(topleft=position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

#💡 O que foi mantido: ✔ Sistema de movimentação do fundo. ✔ Posicionamento correto para dar a sensação de deslocamento contínuo.

# Imagem a ser substituída: 🔹 Arquivo PNG no diretório ./asset/Background.png