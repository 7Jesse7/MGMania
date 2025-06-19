import sqlite3
import os
import sys

import pygame
import pygame.mixer
from code.Const import MENU_OPTION, WIN_WIDTH
from code.Background import Background
from code.Score import Score


class Menu:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 40)
        self.selected = 0
        self.background = Background("Background", (0, 0))

    def run(self):
        running = True

        pygame.mixer.init()
        pygame.mixer.music.load('asset/Menu.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)  # toca indefinidamente

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = max(0, self.selected - 1)
                    elif event.key == pygame.K_DOWN:
                        self.selected = min(len(MENU_OPTION) - 1, self.selected + 1)
                    elif event.key == pygame.K_RETURN:
                        if MENU_OPTION[self.selected] == "SCORE":
                            print("Exibindo tela de scores...")
                            score = Score(self.window)
                            score.run()
                        else:
                            return MENU_OPTION[self.selected]

            self.window.blit(self.background.image, self.background.rect)

            text_height = self.font.get_height()
            total_height = len(MENU_OPTION) * text_height
            start_y = (self.window.get_height() - total_height) // 2

            for i, option in enumerate(MENU_OPTION):
                color = (255, 255, 255) if i == self.selected else (150, 150, 150)
                text = self.font.render(option, True, color)
                text_rect = text.get_rect(center=(self.window.get_width() // 2, start_y + i * text_height))
                self.window.blit(text, text_rect)

            pygame.display.flip()
        return None
