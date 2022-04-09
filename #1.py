import pygame, sys
from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((500,700))
pygame.display.set_caption('prueba1')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
