import pygame
from code.DBProxy import DBProxy
from code.Const import SCORE_POS

class Score:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 30)
        self.db = DBProxy("game_score")

    def run(self):
        scores = self.db.retrieve_top10()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                    running = False

            self.window.fill((0, 0, 0))
            title = self.font.render("TOP 10 SCORES", True, (255, 255, 255))
            self.window.blit(title, SCORE_POS["Title"])

            for i, (id, name, score, date) in enumerate(scores):
                text = self.font.render(f"{name}: {score} pts ({date})", True, (200, 200, 200))
                self.window.blit(text, SCORE_POS[i])

            pygame.display.flip()
# O que esse módulo faz: ✔ Recupera e exibe o ranking dos 10 melhores jogadores. ✔ Mostra nome, pontuação e data de cada score salvo no banco de dados. ✔ Permite sair pressionando ENTER ou fechando a janela.

# Onde substituir assets: 🔹 Imagem da tela de score (PNG) → ./asset/Score.png.