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
game_goes = True
amount_of_food = 1
speed = 1

COLOR_WHITE = 255, 255, 255
COLOR_RED = pygame.Color('#CD533B')
COLOR_ORANGE = pygame.Color("#ffa500")
COLOR_PURPLE = pygame.Color("#800080")
FOOD_COLOR = COLOR_RED
COLOR_BLACK = 0, 0, 0
COLOR_BLUE = pygame.Color('#5c59ff')
COLOR_YELLOW = pygame.Color('#ffff00')
COLOR_GREEN = pygame.Color('#aad751')
COLOR_GREY = pygame.Color('#999999')