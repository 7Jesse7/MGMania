# Cores
import pygame

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# Eventos
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# Velocidades ajustadas para estilo Megamania
ENTITY_SPEED = {
    'Background': 1,
    'Player': 4,
    'PlayerShot': 6,
    'Enemy': 2,
    'EnemyShot': 3,
}

# Vida das entidades
ENTITY_HEALTH = {
    'Player': 100,
    'PlayerShot': 1,
    'Enemy': 50,
    'EnemyShot': 1,
}

# Dano causado por cada entidade
ENTITY_DAMAGE = {
    'Player': 5,
    'PlayerShot': 20,
    'Enemy': 10,
    'EnemyShot': 15,
}

# Pontuação ao eliminar inimigos
ENTITY_SCORE = {
    'Enemy': 100,
    'EnemyShot': 0,
}

# Tempo de recarga dos tiros
ENTITY_SHOT_DELAY = {
    'Player': 5,
    'Enemy': 50,
}

# duração do jogo
GAME_DURATION = 35  # Tempo total do jogo em segundos


# Opções do Menu
MENU_OPTION = ('NEW GAME', 'SCORE', "EXIT")

# Controles do jogador (Apenas movimentação horizontal)
PLAYER_KEY_LEFT = pygame.K_LEFT
PLAYER_KEY_RIGHT = pygame.K_RIGHT
PLAYER_KEY_SHOOT = pygame.K_SPACE

# Tempo para spawn de inimigos
SPAWN_TIME = 400

# Tempo limite do nível
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 100000

# Tamanho da janela
WIN_WIDTH = 576
WIN_HEIGHT = 800 #324

# Posições do Score
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 58),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 98),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}
