import pygame

from app import _settings
from app._settings import COLOR_RED


class Wall:
    def __init__(self, start_pos, color):
        self.wall_pos = start_pos
        self.wall_color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.wall_color, pygame.Rect(self.wall_pos[0], self.wall_pos[1], _settings.CELL_SIZE, _settings.CELL_SIZE))