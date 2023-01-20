import pygame
from app._settings import COLOR_RED, CELL_SIZE


class Food:
    def __init__(self, start_pos, color):
        self.food_pos = start_pos
        self.food_color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.food_color, pygame.Rect(self.food_pos[0], self.food_pos[1], CELL_SIZE, CELL_SIZE))