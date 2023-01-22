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
gamemode = 0

COLOR_WHITE = 255, 255, 255
COLOR_RED = pygame.Color('#CD533B')
COLOR_ORANGE = pygame.Color("#ffa500")
COLOR_PURPLE = pygame.Color("#800080")
FOOD_COLOR = COLOR_RED
COLOR_DIM_RED = pygame.Color("#a85252")
COLOR_DIM_ORANGE = pygame.Color("#d9a98b")
COLOR_DIM_PURPLE = pygame.Color("#84597e")
FUTURE_FOOD_COLOR = COLOR_DIM_RED
COLOR_BLACK = 0, 0, 0
COLOR_SILVER = pygame.Color("#b5b8b1")
COLOR_BLUE = pygame.Color('#5c59ff')
SNAKE_COLOR = COLOR_BLUE
COLOR_YELLOW = pygame.Color('#ffff00')
COLOR_GREEN = pygame.Color('#aad751')
FIELD_COLOR = COLOR_GREEN
COLOR_PINK = pygame.Color("#ff9baa")
COLOR_CYAN = pygame.Color("#30d5c8")
COLOR_GREY = pygame.Color('#999999')