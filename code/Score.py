import pygame
import sys
import os
from code.DBProxy import DBProxy
from utils import resource_path


class Score:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 24)

        # Caminho seguro e compatível com diferentes sistemas operacionais
        bg_path = resource_path("asset/ScoreBg.png")
        try:
            self.background = pygame.image.load(bg_path).convert()
        except FileNotFoundError:
            print(f"Imagem de fundo não encontrada em {bg_path}")
            self.background = None

        self.db = DBProxy("game_scores")

    def run(self):
        scores = self.db.retrieve_top10()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    running = False  # Volta ao menu

            if self.background:
                self.window.blit(self.background, (0, 0))
            else:
                self.window.fill((0, 0, 0))

            # Título centralizado
            title = self.font.render("TOP 10 SCORES", True, (255, 255, 255))
            title_rect = title.get_rect(center=(self.window.get_width() // 2, 40))
            self.window.blit(title, title_rect)

            # Lista de scores centralizada
            start_y = 80
            spacing = 26

            for i, (id, name, score, date) in enumerate(scores):
                text = self.font.render(f"{name}: {score} pts ({date})", True, (200, 200, 200))
                text_rect = text.get_rect(center=(self.window.get_width() // 2, start_y + i * spacing))
                self.window.blit(text, text_rect)

            pygame.display.flip()
