import pygame
from code.Const import PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShotBCKP import PlayerShot

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = 0
        self.shooting = False  # Estado de disparo

    def handle_event(self, event):
        """ Captura eventos de teclado para controle de tiro """
        if event.type == pygame.KEYDOWN and event.key == PLAYER_KEY_SHOOT:
            self.shooting = True
        elif event.type == pygame.KEYUP and event.key == PLAYER_KEY_SHOOT:
            self.shooting = False

    def update(self):
        keys = pygame.key.get_pressed()

        # Movimentação horizontal
        if keys[PLAYER_KEY_LEFT]:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if keys[PLAYER_KEY_RIGHT]:
            self.rect.centerx += ENTITY_SPEED[self.name]

        # Disparo controlado via eventos
        if self.shooting:
            if self.shot_delay <= 0:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]
                shot = PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.top))
                self.groups()[0].add(shot)  # Adiciona o tiro ao grupo de sprites
        else:
            self.shot_delay -= 1 if self.shot_delay > 0 else 0  # Reduz delay apenas quando não está atirando

    def shoot(self):
        """ Só atira se a tecla SPACE estiver pressionada """
        keys = pygame.key.get_pressed()
        if keys[PLAYER_KEY_SHOOT]:  # Agora verifica se SPACE está pressionado
            if self.shot_delay <= 0:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]
                shot = PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.top))
                return shot
        return None

