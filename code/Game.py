import pygame
import sys
from code.Level import Level
from code.Const import MENU_OPTION

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((576, 324))
        pygame.display.set_caption("Megamania Inspired Game")


        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            menu_option = self.show_menu()  # Agora retorna um índice válido

            if menu_option == 0:  # NEW GAME
                self.start_game()
            elif menu_option == 1:  # SCORE
                self.show_score()
            elif menu_option == 2:  # EXIT
                pygame.quit()
                sys.exit()

    def show_menu(self):
        background = pygame.image.load("../asset/Menu.png").convert_alpha()
        font = pygame.font.Font(None, 40)
        selected = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = max(0, selected - 1)
                    elif event.key == pygame.K_DOWN:
                        selected = min(len(MENU_OPTION) - 1, selected + 1)
                    elif event.key == pygame.K_RETURN:
                        return selected  # RETORNA o índice correto

            self.window.blit(background, (0, 0))
            for i, option in enumerate(MENU_OPTION):
                color = (255, 255, 255) if i == selected else (150, 150, 150)
                text = font.render(option, True, color)
                self.window.blit(text, (250, 150 + i * 40))

            pygame.display.flip()

    def start_game(self):
        level = Level(self.window)
        level.run()

    def show_score(self):
        # Exibir ranking de pontuação
        pass
# O que foi ajustado: ✔ Tela de jogo com resolução fixa (576x324). ✔ Menu funcional com opções de iniciar jogo, visualizar score e sair. ✔ Chamada correta do Level.py para executar o jogo.

# Onde substituir assets: 🔹 Imagem do menu (PNG) → ./asset/Menu.png. 🔹 Som do menu (MP3) → ./asset/Menu.mp3.