from random import randrange

import pygame

from app import _settings
from app._settings import COLOR_RED, WIDTH, HEIGHT, COLOR_YELLOW, COLOR_GREY, COLOR_BLUE, COLOR_GREEN, \
    game_goes
from objects.cell import Cell
from objects.snake import Snake
from scenes._base import Scene


class SceneGame(Scene):
    def __init__(self):
        super().__init__()
        self.snake = Snake(_settings.SNAKE_COLOR)
        self.foods = []
        self.walls = []
        self.keys = []
        self.future_food = []
        self.koef = 0 # коэффицент, нужный для отображения змейки в режиме hole
        if _settings.gamemode != 5:
            for i in range(_settings.amount_of_food):
                lim = 4 if _settings.CELL_SIZE == 10 else 7
                self.foods.append(Cell([randrange(1, WIDTH / _settings.CELL_SIZE) * _settings.CELL_SIZE,
                                        randrange(lim, HEIGHT / _settings.CELL_SIZE) * _settings.CELL_SIZE],
                                       _settings.FOOD_COLOR))
                if _settings.gamemode == 6:
                    self.future_food.append(Cell([randrange(1, WIDTH / _settings.CELL_SIZE) * _settings.CELL_SIZE,
                                                  randrange(lim, HEIGHT / _settings.CELL_SIZE) * _settings.CELL_SIZE],
                                                 _settings.FUTURE_FOOD_COLOR))
        else:
            for i in range(_settings.amount_of_food):
                self.walls.append(Cell([randrange(1, _settings.WIDTH / _settings.CELL_SIZE) * _settings.CELL_SIZE,
                                        randrange(4, _settings.HEIGHT / _settings.CELL_SIZE) * _settings.CELL_SIZE],
                                       _settings.COLOR_YELLOW))
                self.keys.append(Cell([randrange(1, _settings.WIDTH / _settings.CELL_SIZE) * _settings.CELL_SIZE,
                                        randrange(4, _settings.HEIGHT / _settings.CELL_SIZE) * _settings.CELL_SIZE],
                                       _settings.COLOR_SILVER))

        self.score = 0
        self.clock = pygame.time.Clock()
        self.ticks = 0
        _settings.game_goes = True
        if _settings.speed == 0:
            self.clock.tick(20)
        if _settings.speed == 1:
            self.clock.tick(40)
        else:
            self.clock.tick()

    def data_save(self, res="lose"):
        prev_text = ""
        with open(file="data/statistics.txt", mode="r") as f:
            prev_text = f.read()
        with open(file="data/statistics.txt", mode="w") as f:
            time = self.seconds + self.minutes * 60
            field_size = "small" if _settings.CELL_SIZE == 30 else "medium" if _settings.CELL_SIZE == 20 else "big"
            speed = "slow" if _settings.speed == 0 else "medium" if _settings.speed == 1 else "fast"
            modes = ["default", "walls", "immortal", "hole", "reverse", "lock", "seer"]
            gamemode = modes[_settings.gamemode]
            text = f"{prev_text}{self.score}, {time}, {field_size}, {_settings.amount_of_food}, {speed}, {gamemode}, " \
                   f"{res}\n"
            f.write(text)

    def processing(self,
                   app):
        # функция processing обрабатывает события, для стартового окна к примеру
        # после нажатия Enter, будет сменяться текущая сцена на сцену игры
        events = pygame.event.get()
        app.screen.fill(_settings.FIELD_COLOR)
        if _settings.CELL_SIZE == 10:
            pygame.draw.rect(app.screen, COLOR_GREY, pygame.Rect(0, 0, WIDTH, _settings.CELL_SIZE * 5))
        else:
            pygame.draw.rect(app.screen, COLOR_GREY, pygame.Rect(0, 0, WIDTH, _settings.CELL_SIZE * 3))
        if _settings.speed == 0:
            tick = self.clock.tick(20)
        elif _settings.speed == 1:
            tick = self.clock.tick(40)
        else:
            tick = self.clock.tick()
        if _settings.game_goes:
            self.ticks += tick
        self.seconds = int(self.ticks / 1000 % 60)
        self.minutes = int(self.ticks / 60000 % 24)
        time_text = [f"Time {self.minutes:02d}:{self.seconds:02d}"]
        self.print_text(app, time_text, 20, 220, 50)
        _settings.game_goes = True
        self.snake.draw_snake(app.screen, self.koef)
        for i in self.walls:
            i.draw(app.screen)
        for i in self.foods:
            i.draw(app.screen)
        for i in self.keys:
            i.draw(app.screen)
        for i in self.future_food:
            i.draw(app.screen)
        score_text = [f"Score {self.score}"]
        self.print_text(app, score_text, 20, 10, 50)
        if _settings.gamemode == 1:
            if self.snake.check_lose(WIDTH, HEIGHT, self.walls):
                self.data_save()
                app.scenes = [False, False, False, False, False, True]
        else:
            if self.snake.check_lose(WIDTH, HEIGHT, self.walls, self.koef):
                self.data_save()
                app.scenes = [False, False, False, False, False, True]
        for event in events:
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.image.save(app.screen, "data/screenshot.png")
                _settings.game_goes = False
                app.scenes = [False, False, False, True, False, False]
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.snake.change_dir("DOWN")
                break
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.snake.change_dir("UP")
                break
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.snake.change_dir("RIGHT")
                break
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.snake.change_dir("LEFT")
                break
        if _settings.gamemode == 1:
            self.score, self.foods, self.walls = self.snake.move(self.score, self.foods, WIDTH, HEIGHT, self.walls,
                                                                 self.keys, self.future_food)
        elif _settings.gamemode == 5:
            self.score, self.foods, self.walls, self.keys = self.snake.move(self.score, self.foods, WIDTH, HEIGHT,
                                                                            self.walls, self.keys, self.future_food)
        elif _settings.gamemode == 6:
            self.score, self.foods, self.future_food = self.snake.move(self.score, self.foods, WIDTH, HEIGHT,
                                                                            self.walls, self.keys, self.future_food)
        else:
            self.score, self.foods = self.snake.move(self.score, self.foods, WIDTH, HEIGHT, self.walls, self.keys,
                                                     self.future_food)
        self.koef += 1

    def show(self, app):  # функция отображения начального окна
        self.main(app,
                  self)  # вызов функции main из родительского класса Scene, аналогично, по идее, можно будет ее вызывать в остальных классах сцен
