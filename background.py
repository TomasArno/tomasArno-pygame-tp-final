import pygame
from constantes import *
from auxiliar import Auxiliar


class Background:
    def __init__(self, x, y, width, height, path):
        self.image = pygame.image.load(Auxiliar.set_background_level(path)).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
