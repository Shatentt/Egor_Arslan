import pygame

from app import _settings
from app._settings import COLOR_RED


class Food:
    def __init__(self, start_pos, color):
        self.food_pos = start_pos
        self.food_color = _settings.FOOD_COLOR

    def draw(self, screen):
        pygame.draw.rect(screen, self.food_color, pygame.Rect(self.food_pos[0], self.food_pos[1], _settings.CELL_SIZE, _settings.CELL_SIZE))