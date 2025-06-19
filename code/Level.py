import pygame
import sys
import sqlite3
import datetime

from code.EnemyShot import EnemyShot
from code.Player import Player
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.Const import EVENT_ENEMY, WIN_WIDTH, WIN_HEIGHT, GAME_DURATION, SPAWN_TIME
from code.PlayerShot import PlayerShot


class Level:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.running = True
        self.background = pygame.image.load("../asset/Background.png").convert()

        # Grupo de sprites para renderização
        self.all_sprites = pygame.sprite.Group()

        # Inicializa o jogador
        self.player = Player(name="Player", position=(WIN_WIDTH // 2, WIN_HEIGHT - 50))
        self.all_sprites.add(self.player)  # Adiciona o jogador ao grupo de sprites

        # Inicializa fábrica de inimigos com referência ao grupo de sprites ✅
        self.entity_factory = EntityFactory(self.all_sprites)

        # Evento de spawn automático de inimigos a cada intervalo
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Inimigos surgem a cada 2 segundos

        # Inicializa Score e temporizador
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.start_time = pygame.time.get_ticks()  # Marca o início do jogo
        self.time_remaining = GAME_DURATION  # Tempo total definido

    def run(self):
        pygame.mixer.music.load('../asset/Level.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == EVENT_ENEMY:
                    enemy = self.entity_factory.spawn_enemy()
                    self.all_sprites.add(enemy)

                self.player.handle_event(event)

            #self.window.fill((0, 0, 0))
            self.window.blit(self.background, (0, 0))

            # Atualiza o tempo restante
            current_time = (pygame.time.get_ticks() - self.start_time) // 1000
            self.time_remaining = max(GAME_DURATION - current_time, 0)

            # Se o tempo acabar, exibe "YOU WIN" e permite inserir nome
            if self.time_remaining <= 0:
                self.window.fill((0, 0, 0))
                win_text = self.font.render("YOU WIN!", True, (0, 255, 0))
                self.window.blit(win_text, (WIN_WIDTH // 2 - 80, WIN_HEIGHT // 2 - 60))
                #sub_text = self.font.render("Enter your name (5 characters):", True, (255, 255, 255))
                #self.window.blit(sub_text, (WIN_WIDTH // 2 - 150, WIN_HEIGHT // 2))
                pygame.display.flip()
                pygame.time.delay(1500)

                # Captura entrada do nome do jogador
                player_name = self.get_player_name()
                print(f"Salvando score: {player_name} - {self.score}")  # Debug para verificar chamada
                self.save_score(player_name, self.score)  # Salva score no banco
                print("Score salvo no banco!")  # Confirmação da execução
                return  # Volta ao menu inicial após salvar

            # Se o jogador perdeu todas as vidas, exibe "YOU LOSE" e aguarda input
            if self.player.health <= 0:
                game_over_text = self.font.render("YOU LOSE - Press any key to return", True, (255, 0, 0))
                self.window.blit(game_over_text, (WIN_WIDTH // 2 - 150, WIN_HEIGHT // 2 - 20))
                pygame.display.flip()
                pygame.time.delay(1500)

                # Espera input do jogador antes de voltar ao menu
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            waiting = False
                            return

            # Verifica colisões
            for enemy_shot in self.all_sprites:
                if isinstance(enemy_shot, EnemyShot) and enemy_shot.rect.colliderect(self.player.rect):
                    self.player.take_damage()
                    enemy_shot.kill()

            for enemy in self.all_sprites:
                if isinstance(enemy, Enemy) and enemy.rect.colliderect(self.player.rect):
                    self.player.take_damage()
                    enemy.kill()

            for player_shot in self.all_sprites:
                for enemy in self.all_sprites:
                    if isinstance(player_shot, PlayerShot) and isinstance(enemy, Enemy) and player_shot.rect.colliderect(enemy.rect):
                        enemy.take_damage()
                        player_shot.kill()
                        self.score += 10  # Aumenta Score ao eliminar inimigo

            # Atualiza e desenha todos os sprites na tela
            # Atualiza e desenha todos os sprites na tela
            self.all_sprites.update()

            # Remove inimigos que saem da parte de baixo da tela
            for enemy in self.all_sprites:
                if isinstance(enemy, Enemy) and enemy.rect.top > WIN_HEIGHT:
                    enemy.kill()

            self.all_sprites.draw(self.window)

            # Exibe Score e tempo na tela
            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.window.blit(score_text, (10, 10))

            time_text = self.font.render(f"Time: {self.time_remaining}s", True, (255, 255, 255))
            self.window.blit(time_text, (10, 40))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def get_player_name(self):
        """ Captura o nome do jogador (máximo 5 caracteres) """
        input_name = ""
        while len(input_name) < 5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Fecha o jogo corretamente se clicar no X

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(input_name) == 5:
                        return input_name  # Retorna nome ao pressionar ENTER
                    elif event.key == pygame.K_BACKSPACE:
                        input_name = input_name[:-1]
                    elif len(input_name) < 5:
                        input_name += event.unicode.upper()

            self.window.fill((0, 0, 0))
            name_text = self.font.render(f"Your Name (5 characters): {input_name}", True, (255, 255, 255))
            self.window.blit(name_text, (WIN_WIDTH // 2 - 150, WIN_HEIGHT // 2))
            pygame.display.flip()

        return input_name


    def save_score(self, player_name, score):
        """ Salva o nome e pontuação do jogador no banco de dados """
        conn = sqlite3.connect("./data/game_scores.db")
        cursor = conn.cursor()

        # Cria tabela se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                score INTEGER,
                date TEXT
            )
        """)
        # Insere novo registro
        current_date = datetime.datetime.now().strftime("%d/%m")
        cursor.execute("INSERT INTO scores (name, score, date) VALUES (?, ?, ?)",
                       (player_name, score, current_date))

        conn.commit()
        conn.close()