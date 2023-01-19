import pygame
import os
import sys

pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 900
CELL_SIZE = 20
FPS = 30
ARIAL = pygame.font.SysFont('arial', 30)

COLOR_WHITE = 255, 255, 255
COLOR_RED = pygame.Color('#CD533B')
COLOR_BLACK = 0, 0, 0
COLOR_BLUE = pygame.Color('#5c59ff')