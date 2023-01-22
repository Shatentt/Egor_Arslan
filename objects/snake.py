from random import randrange

import pygame

from app import _settings
from objects.cell import Cell

"""
    class Snake -  Класс змейки
        def __init__(self, snake_color)
            Конструктор класса змейки, принимает в себя цвет змейки, который зависит от настроек игрока
            Создание массива позиций каждой клектки, по которому будут рисоваться квадраты
        def change_dir(self, dir) - Изменяем направление движения змеи, если оно не противоположно текущему
        def change_pos(self) - Изменение положения змейки каждый фрейм
        def move -  функция движения змейки. Работает и возвращает значения по-разному, в зависимости от режима игры
        def reverse(self):  # функция для режима игры reverse
            При съедании еды хвост змейки становится головой, а голова хвостом. Эта функция реализовывает такой поворот
        def add_snake_cell(self) - Добавление новой клетки змейке
        def draw_snake(self, screen, koef=0) - Отображаем змею
        def check_lose(self, screen_width, screen_height, walls=None, koef=0)
            Проверка каждый фрейм на проигрыш (удар об себя, об стенку, об границу карты)
"""

class Snake: # Класс змейки
    def __init__(self, snake_color):
        # Конструктор класса змейки, принимает в себя цвет змейки, который зависит от настроек игрока
        # Создание массива позиций каждой клектки, по которому будут рисоваться квадраты
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

    def move(self, score, foods_pos, screen_width, screen_height, walls_pos=None, keys_pos=None, future_food_pos=None):
        # Функция движения змейки. Работает и возвращает значения по-разному, в зависимости от режима игры
        size = 4 if _settings.CELL_SIZE == 10 else 7
        to_del = [] # список, нужный для удаляния еды в режиме lock
        for i in range(len(foods_pos)):
            if self.snake_cells[0][0] == foods_pos[i].pos[0] and self.snake_cells[0][1] == foods_pos[i].pos[1]:
                # Если голова змейки находится на одной позиции с едой, то позиция еды изменяется, score прибавляется
                # в режиме игры lock спавнятся стена и ключ, еда удаляется
                # в режиме игры seer еда отправляется на позицию будущего яблока, будущее яблоко меняет позицию
                if _settings.gamemode != 5 and _settings.gamemode != 6:
                    foods_pos[i].pos = [randrange(1, screen_width / _settings.CELL_SIZE) * _settings.CELL_SIZE,
                                    randrange(size, screen_height / _settings.CELL_SIZE) * _settings.CELL_SIZE]
                elif _settings.gamemode == 5:
                    keys_pos.append(Cell([randrange(1, _settings.WIDTH / _settings.CELL_SIZE) * _settings.CELL_SIZE,
                                           randrange(4, _settings.HEIGHT / _settings.CELL_SIZE) * _settings.CELL_SIZE],
                                          _settings.COLOR_SILVER))
                    walls_pos.append(Cell([randrange(1, _settings.WIDTH / _settings.CELL_SIZE) * _settings.CELL_SIZE,
                                           randrange(4, _settings.HEIGHT / _settings.CELL_SIZE) * _settings.CELL_SIZE],
                                          _settings.COLOR_YELLOW))
                    to_del.append(i)
                else:
                    foods_pos[i].pos = future_food_pos[0].pos
                    future_food_pos.pop(0)
                    future_food_pos.append(
                        Cell([randrange(1, _settings.WIDTH / _settings.CELL_SIZE) * _settings.CELL_SIZE,
                              randrange(4, _settings.HEIGHT / _settings.CELL_SIZE) * _settings.CELL_SIZE],
                             _settings.FUTURE_FOOD_COLOR))
                score += 1
                # Добавление стенки каждые 2 очка при режиме игры walls
                if _settings.gamemode == 1:
                    if score % 2 == 0:
                        walls_pos.append(Cell(
                            [randrange(1, _settings.WIDTH / _settings.CELL_SIZE) * _settings.CELL_SIZE,
                             randrange(4, _settings.HEIGHT / _settings.CELL_SIZE) * _settings.CELL_SIZE],
                            _settings.COLOR_YELLOW))
                if _settings.gamemode != 3:
                    self.add_snake_cell()
                else:
                    # В режиме игры hole добавляются 2 клетки. Одна видимая, другая нет
                    self.add_snake_cell()
                    self.add_snake_cell()
                # В режиме reverse при съедании яблока "переворачиваем змейку"
                if _settings.gamemode == 4:
                    self.reverse()
        cnt_of_deleted = 0
        for i in range(len(to_del)):
            foods_pos.pop(to_del[i] - cnt_of_deleted)
            cnt_of_deleted += 1
        list_of_deleted = []  # список, помогающий удалить элементы списка keys_pos
        # При взятии ключа змейкой в режиме lock добавляем еду на место стенки, стенку и ключ удаляем
        for i in range(len(keys_pos)):
            if self.snake_cells[0][0] == keys_pos[i].pos[0] and self.snake_cells[0][1] == keys_pos[i].pos[1]:
                list_of_deleted.append(i)
                foods_pos.append(Cell(walls_pos[0].pos, _settings.FOOD_COLOR))
                walls_pos.pop(0)
        cnt_of_deleted = 0
        for i in list_of_deleted:
            keys_pos.pop(i - cnt_of_deleted)
            cnt_of_deleted += 1
        self.change_pos()
        if _settings.gamemode == 1:
            return score, foods_pos, walls_pos
        elif _settings.gamemode == 5:
            return score, foods_pos, walls_pos, keys_pos
        elif _settings.gamemode == 6:
            return score, foods_pos, future_food_pos
        else:
            return score, foods_pos

    def reverse(self):  # функция для режима игры reverse
        # При съедании еды хвост змейки становится головой, а голова хвостом. Эта функция реализовывает такой поворот
        if self.snake_cells[-1][0] > self.snake_cells[-2][0]:
            self.direction = "RIGHT"
        elif self.snake_cells[-1][0] < self.snake_cells[-2][0]:
            self.direction = "LEFT"
        elif self.snake_cells[-1][1] > self.snake_cells[-2][1]:
            self.direction = "DOWN"
        elif self.snake_cells[-1][1] < self.snake_cells[-2][1]:
            self.direction = "UP"
        print(self.direction)
        self.snake_cells = list(reversed(self.snake_cells))

    def add_snake_cell(self):
        # Добавление новой клетки змейке
        if self.snake_cells[-1][0] > self.snake_cells[-2][0]:
            self.snake_cells.append([self.snake_cells[-1][0] + _settings.CELL_SIZE, self.snake_cells[-1][1]])
        elif self.snake_cells[-1][0] < self.snake_cells[-2][0]:
            self.snake_cells.append([self.snake_cells[-1][0] - _settings.CELL_SIZE, self.snake_cells[-1][1]])
        elif self.snake_cells[-1][1] > self.snake_cells[-2][1]:
            self.snake_cells.append([self.snake_cells[-1][0], self.snake_cells[-1][1] + _settings.CELL_SIZE])
        elif self.snake_cells[-1][1] < self.snake_cells[-2][1]:
            self.snake_cells.append([self.snake_cells[-1][0], self.snake_cells[-1][1] - _settings.CELL_SIZE])

    def draw_snake(self, screen, koef=0):
        # Отображаем змею
        if _settings.gamemode != 3:
            for pos in self.snake_cells:
                pygame.draw.rect(screen, self.snake_color,
                                 pygame.Rect(pos[0], pos[1], _settings.CELL_SIZE, _settings.CELL_SIZE))
        else:
            pygame.draw.rect(screen, self.snake_color,
                             pygame.Rect(self.snake_cells[0][0], self.snake_cells[0][1], _settings.CELL_SIZE,
                                         _settings.CELL_SIZE))
            start = 1 + koef % 2
            for i in range(start, len(self.snake_cells), 2):
                pygame.draw.rect(screen, self.snake_color,
                                 pygame.Rect(self.snake_cells[i][0], self.snake_cells[i][1], _settings.CELL_SIZE,
                                             _settings.CELL_SIZE))

    def check_lose(self, screen_width, screen_height, walls=None, koef=0):
        # Проверка каждый фрейм на проигрыш (удар об себя, об стенку, об границу карты)
        for wall in walls:
            if wall.pos[0] == self.snake_cells[0][0] and wall.pos[1] == self.snake_cells[0][1]:
                return True
        if _settings.gamemode != 2:
            top_size = _settings.CELL_SIZE * 5 if _settings.CELL_SIZE == 10 else _settings.CELL_SIZE * 3
            if any((self.snake_cells[0][0] > screen_width - _settings.CELL_SIZE or self.snake_cells[0][0] < 0,
                    self.snake_cells[0][1] > screen_height - _settings.CELL_SIZE or self.snake_cells[0][1] < top_size)):
                return True
            for i in range(1, len(self.snake_cells)):
                if self.snake_cells[i][0] == self.snake_cells[0][0] and self.snake_cells[i][1] == self.snake_cells[0][1]:
                    if _settings.gamemode == 3 and koef % 2 == i % 2:
                        return False
                    return True
            return False
        else:
            return False
