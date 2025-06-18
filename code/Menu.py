import sqlite3

import pygame
from code.Const import MENU_OPTION, WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 40)
        self.selected = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = max(0, self.selected - 1)
                    elif event.key == pygame.K_DOWN:
                        self.selected = min(len(MENU_OPTION) - 1, self.selected + 1)
                    elif event.key == pygame.K_RETURN:
                        if MENU_OPTION[self.selected] == "SCORE":  # Se o jogador escolheu SCORE
                            print("✅ Exibindo tela de scores...")  # Debug para verificar chamada
                            self.show_scores()  # Exibe a tela de ranking
                        else:
                            return MENU_OPTION[self.selected]  # Continua normalmente

                        #return MENU_OPTION[self.selected]

            self.window.fill((0, 0, 0))
            for i, option in enumerate(MENU_OPTION):
                color = (255, 255, 255) if i == self.selected else (150, 150, 150)
                text = self.font.render(option, True, color)
                self.window.blit(text, (250, 150 + i * 40))

            pygame.display.flip()
        return None

    def show_scores(self):
        """ Exibe os scores salvos no banco de dados """
        conn = sqlite3.connect("game_scores.db")
        cursor = conn.cursor()

        cursor.execute("SELECT name, score, date FROM scores ORDER BY score DESC LIMIT 10")
        scores = cursor.fetchall()

        self.window.fill((0, 0, 0))

        title_text = self.font.render("Top Scores:", True, (255, 255, 255))
        self.window.blit(title_text, (WIN_WIDTH // 2 - 50, 50))

        y_offset = 100
        for name, score, date in scores:
            score_text = self.font.render(f"{name}: {score} pts - {date}", True, (255, 255, 255))
            self.window.blit(score_text, (WIN_WIDTH // 2 - 100, y_offset))
            y_offset += 30

        pygame.display.flip()

        # Espera input para voltar ao menu
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False  # Sai da tela de scores e volta ao menu

# O que esse módulo faz: ✔ Cria o menu do jogo com opções de Novo Jogo, Score e Sair. ✔ Permite a navegação com as setas UP/DOWN e seleção com ENTER. ✔ Exibe as opções de forma clara e interativa na tela inicial.

# Onde substituir assets: 🔹 Imagem do menu (PNG) → ./asset/Menu.png. 🔹 Som do menu (MP3) → ./asset/Menu.mp3.
