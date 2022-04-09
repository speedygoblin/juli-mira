from ast import While
from lib2to3.pytree import WildcardPattern
import pygame, sys

class Prueba_2:
    def __init__(self):
        pygame.init
        self.ventana = pygame.display.set_mode((500,700))
        pygame.display.set_caption('prueba2')

    def correr_juego(self):
        While True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()

if __name__ == "__main__":
    a = Prueba_2()
    a.correr_juego()