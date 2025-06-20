import pygame
import sys
from code.Level import Level
from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Megamania Inspired Game")
        self.clock = pygame.time.Clock()

    def run(self):
        print("Entrou na tela de Score!")  # debug
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
        menu = Menu(self.window)
        opcao = menu.run()
        return MENU_OPTION.index(opcao) if opcao in MENU_OPTION else 2  # fallback: exit

    def start_game(self):
        level = Level(self.window)
        level.run()

    def show_score(self):
        # Exibir ranking de pontuação
        score = Score(self.window)       #  Instancia a tela de score
        score.run()                      #  Executa a exibição
        pass
