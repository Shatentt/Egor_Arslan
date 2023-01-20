from random import randrange

import pygame

from app import _settings


class Snake:
    def __init__(self, snake_color):
        if _settings.CELL_SIZE == 30:
            self.snake_cells = [[120, 120], [0, 0], [0, 0], [0, 0], [0, 0]]
        else:
            self.snake_cells = [[100, 100], [0, 0], [0, 0], [0, 0], [0, 0]]
        for i in range(1, len(self.snake_cells)):
            self.snake_cells[i][0] = self.snake_cells[i - 1][0] - _settings.CELL_SIZE
            self.snake_cells[i][1] = self.snake_cells[0][1]
        self.snake_color = snake_color
        self.direction = "RIGHT"

    def change_dir(self, dir):
        # Изменяем направление движения змеи, если оно не противоположно текущему
        if any((dir == "RIGHT" and not self.direction == "LEFT",
                dir == "LEFT" and not self.direction == "RIGHT",
                dir == "UP" and not self.direction == "DOWN",
                dir == "DOWN" and not self.direction == "UP")):
            self.direction = dir

    def change_pos(self):
        # Изменение положения змейки каждый фрейм
        tmp = list(self.snake_cells)
        for i in range(len(self.snake_cells) - 1, 0, -1):
            self.snake_cells[i][0] = self.snake_cells[i - 1][0]
            self.snake_cells[i][1] = self.snake_cells[i - 1][1]
        if self.direction == "RIGHT":
            self.snake_cells[0][0] += _settings.CELL_SIZE
        elif self.direction == "LEFT":
            self.snake_cells[0][0] -= _settings.CELL_SIZE
        elif self.direction == "UP":
            self.snake_cells[0][1] -= _settings.CELL_SIZE
        elif self.direction == "DOWN":
            self.snake_cells[0][1] += _settings.CELL_SIZE

    def move(self, score, foods_pos, screen_width, screen_height):
        # функция движения змейки
        for i in range(len(foods_pos)):
            if self.snake_cells[0][0] == foods_pos[i].food_pos[0] and self.snake_cells[0][1] == foods_pos[i].food_pos[1]:
                if _settings.CELL_SIZE == 10:
                    foods_pos[i].food_pos = [randrange(1, screen_width / _settings.CELL_SIZE) * _settings.CELL_SIZE,
                                    randrange(6, screen_height / _settings.CELL_SIZE) * _settings.CELL_SIZE]
                else:
                    foods_pos[i].food_pos = [randrange(1, screen_width / _settings.CELL_SIZE) * _settings.CELL_SIZE, randrange(4, screen_height / _settings.CELL_SIZE) * _settings.CELL_SIZE]
                score += 1
                self.add_snake_cell()
        self.change_pos()
        return score, foods_pos

    def add_snake_cell(self):
        if self.snake_cells[-1][0] > self.snake_cells[-2][0]:
            self.snake_cells.append([self.snake_cells[-1][0] + _settings.CELL_SIZE, self.snake_cells[-1][1]])
        elif self.snake_cells[-1][0] < self.snake_cells[-2][0]:
            self.snake_cells.append([self.snake_cells[-1][0] - _settings.CELL_SIZE, self.snake_cells[-1][1]])
        elif self.snake_cells[-1][1] > self.snake_cells[-2][1]:
            self.snake_cells.append([self.snake_cells[-1][0], self.snake_cells[-1][1] + _settings.CELL_SIZE])
        elif self.snake_cells[-1][1] > self.snake_cells[-2][1]:
            self.snake_cells.append([self.snake_cells[-1][0], self.snake_cells[-1][1] - _settings.CELL_SIZE])

    def draw_snake(self, screen):
        # Отображаем змею
        for pos in self.snake_cells:
            pygame.draw.rect(screen, self.snake_color, pygame.Rect(pos[0], pos[1], _settings.CELL_SIZE, _settings.CELL_SIZE))

    def check_lose(self, screen_width, screen_height):
        if _settings.gamemode != 2:
            # Проверка на проигрыш
            if _settings.CELL_SIZE == 10:
                if any((self.snake_cells[0][0] > screen_width - _settings.CELL_SIZE or self.snake_cells[0][0] < 0,
                        self.snake_cells[0][1] > screen_height - _settings.CELL_SIZE or self.snake_cells[0][1] < _settings.CELL_SIZE * 5)):
                    return True
                for pos in self.snake_cells[1:]:
                    if pos[0] == self.snake_cells[0][0] and pos[1] == self.snake_cells[0][1]:
                        return True
                return False
            else:
                if any((self.snake_cells[0][0] > screen_width - _settings.CELL_SIZE or self.snake_cells[0][0] < 0,
                        self.snake_cells[0][1] > screen_height - _settings.CELL_SIZE or self.snake_cells[0][1] < _settings.CELL_SIZE * 3)):
                    return True
                for pos in self.snake_cells[1:]:
                    if pos[0] == self.snake_cells[0][0] and pos[1] == self.snake_cells[0][1]:
                        return True
                return False
        return False
