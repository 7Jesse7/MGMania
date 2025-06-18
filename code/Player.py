import pygame
from code.Const import PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_WIDTH
from code.Entity import Entity
from code.PlayerShot import PlayerShot

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.health = 3  # Vida do jogador
        self.shooting = False  # Estado de disparo inicializado corretamente
        self.shot_timer = 0  # Inicializa temporizador do tiro

    def take_damage(self):
        """ Reduz a vida do jogador ao receber dano """
        self.health -= 1
        print(f"⚠️ Jogador sofreu dano! Vida restante: {self.health}")
        if self.health <= 0:
            print("💀 Jogador eliminado!")
            self.kill()  # Remove o jogador do jogo ao chegar a 0 de vida

    def handle_event(self, event):
        """ Captura eventos de teclado para tiro """
        if event.type == pygame.KEYDOWN and event.key == PLAYER_KEY_SHOOT:
            self.shooting = True  # Marca que o jogador está atirando
        elif event.type == pygame.KEYUP and event.key == PLAYER_KEY_SHOOT:
            self.shooting = False  # Para de atirar ao soltar SPACE

    def update(self):
        keys = pygame.key.get_pressed()

        # Movimentação horizontal com limites da tela
        if keys[PLAYER_KEY_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        elif keys[PLAYER_KEY_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        # Reduz o temporizador a cada frame
        if self.shot_timer > 0:
            self.shot_timer -= 1  # Agora sempre decrementa, permitindo tiros contínuos

        # Se SPACE estiver pressionado, atira continuamente respeitando o temporizador
        if self.shooting and self.shot_timer <= 0:
            self.shot_timer = ENTITY_SHOT_DELAY[self.name]  # Reinicia o atraso de tiro
            shot = PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.top))
            self.groups()[0].add(shot)  # Adiciona o tiro ao grupo de sprites
