from random import randrange

import pygame

from app.settings import CELL_SIZE


class Snake:
    def __init__(self, snake_color):
        self.snake_cells = [[100, 40], [0, 0], [0, 0], [0, 0], [0, 0]]
        for i in range(1, len(self.snake_cells)):
            self.snake_cells[i][0] = self.snake_cells[i - 1][0] - CELL_SIZE
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
            self.snake_cells[0][0] += CELL_SIZE
        elif self.direction == "LEFT":
            self.snake_cells[0][0] -= CELL_SIZE
        elif self.direction == "UP":
            self.snake_cells[0][1] -= CELL_SIZE
        elif self.direction == "DOWN":
            self.snake_cells[0][1] += CELL_SIZE

    def move(self, score, food_pos, screen_width, screen_height):
        # функция движения змейки
        if self.snake_cells[0][0] == food_pos[0] and self.snake_cells[0][1] == food_pos[1]:
            food_pos = [randrange(1, screen_width / CELL_SIZE) * CELL_SIZE, randrange(1, screen_height / CELL_SIZE) * CELL_SIZE]
            score += 1
            self.add_snake_cell()
        self.change_pos()
        return score, food_pos

    def add_snake_cell(self):
        if self.snake_cells[-1][0] > self.snake_cells[-2][0]:
            self.snake_cells.append([self.snake_cells[-1][0] + CELL_SIZE, self.snake_cells[-1][1]])
        elif self.snake_cells[-1][0] < self.snake_cells[-2][0]:
            self.snake_cells.append([self.snake_cells[-1][0] - CELL_SIZE, self.snake_cells[-1][1]])
        elif self.snake_cells[-1][1] > self.snake_cells[-2][1]:
            self.snake_cells.append([self.snake_cells[-1][0], self.snake_cells[-1][1] + CELL_SIZE])
        elif self.snake_cells[-1][1] > self.snake_cells[-2][1]:
            self.snake_cells.append([self.snake_cells[-1][0], self.snake_cells[-1][1] - CELL_SIZE])

    def draw_snake(self, screen):
        # Отображаем змею
        for pos in self.snake_cells:
            pygame.draw.rect(screen, self.snake_color, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

    def check_lose(self, screen_width, screen_height):
        # Проверка на проигрыш
        if any((self.snake_cells[0][0] > screen_width - 10 or self.snake_cells[0][0] < 0,
                self.snake_cells[0][1] > screen_height - 10 or self.snake_cells[0][1] < 0)):
            return True
        for pos in self.snake_cells[1:]:
            if pos[0] == self.snake_cells[0][0] and pos[1] == self.snake_cells[0][1]:
                return True
        return False
