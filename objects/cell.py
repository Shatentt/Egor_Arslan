import pygame

from app import _settings
from app._settings import COLOR_RED

"""
    class Cell - Это класс, который является одной клеткой. Используется, для того чтобы создать еду/стену/ключ
        def __init__(self, start_pos, color) - Конструктор класса Cell
        def draw(self, screen) - Отображение клетки
"""

class Cell:
    # Это класс, который является одной клеткой. Используется, для того чтобы создать еду/стену/ключ
    def __init__(self, start_pos, color):
        # Конструктор класса Cell
        self.pos = start_pos
        self.color = color

    def draw(self, screen):
        # Отображение клетки
        pygame.draw.rect(screen, self.color, pygame.Rect(self.pos[0], self.pos[1], _settings.CELL_SIZE, _settings.CELL_SIZE))