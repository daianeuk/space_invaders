import sys
import pygame
from configuracoes import Settings
from nave import Ship
#função do jogo
def run_game():
    #criação da primeira tela do jogo
    pygame.init()
    configuracoesDoJogo = Settings() #criando um objeto a partir da classe Settings
    screen = pygame.display.set_mode((configuracoesDoJogo.screen_width,
    configuracoesDoJogo.screen_height))
    pygame.display.set_caption('Invasao Alienigena')
    ship = Ship(screen)
    # loop inicial do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ship.blitme()
        pygame.display.flip()
run_game()



