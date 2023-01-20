from random import randrange

import pygame

from app import _settings
from app._settings import COLOR_RED, WIDTH, HEIGHT, COLOR_YELLOW, COLOR_GREY, COLOR_BLUE, COLOR_GREEN, \
    game_goes
from objects.food import Food
from objects.snake import Snake
from scenes._base import Scene


class SceneGame(Scene):
    def __init__(self):
        super().__init__()
        self.snake = Snake(_settings.SNAKE_COLOR)
        self.foods = []
        for i in range(_settings.amount_of_food):
            if _settings.CELL_SIZE == 10:
                self.foods.append(Food([randrange(1, WIDTH / _settings.CELL_SIZE) * _settings.CELL_SIZE, randrange(4, HEIGHT / _settings.CELL_SIZE) * _settings.CELL_SIZE], COLOR_RED))
            else:
                self.foods.append(Food([randrange(1, WIDTH / _settings.CELL_SIZE) * _settings.CELL_SIZE, randrange(6, HEIGHT / _settings.CELL_SIZE) * _settings.CELL_SIZE], COLOR_RED))
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
    def processing(self,
                   app):  # функция processing обрабатывает события, для стартового окна к примеру, после нажатия Enter, будет сменяться текущая сцена на сцену игры
        events = pygame.event.get()
        app.screen.fill(_settings.FIELD_COLOR)
        if _settings.CELL_SIZE == 10:
            pygame.draw.rect(app.screen, COLOR_GREY, pygame.Rect(0, 0, WIDTH, _settings.CELL_SIZE * 5))
        else:
            pygame.draw.rect(app.screen, COLOR_GREY, pygame.Rect(0, 0, WIDTH, _settings.CELL_SIZE * 3))
        if _settings.speed == 0:
            tick = self.clock.tick(20)
        if _settings.speed == 1:
            tick = self.clock.tick(40)
        else:
            tick = self.clock.tick()
        if _settings.game_goes:
            self.ticks += tick
        seconds = int(self.ticks / 1000 % 60)
        minutes = int(self.ticks / 60000 % 24)
        time_text = [f"Time {minutes:02d}:{seconds:02d}"]
        self.print_text(app, time_text, 20, 220, 50)
        _settings.game_goes = True
        self.snake.draw_snake(app.screen)
        for i in self.foods:
            i.draw(app.screen)
        score_text = [f"Score {self.score}"]
        self.print_text(app, score_text, 20, 10, 50)
        if self.snake.check_lose(WIDTH, HEIGHT):
            self.terminate()
        for event in events:
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.image.save(app.screen, "data/screenshot.png")
                _settings.game_goes = False
                app.scenes = [False, False, False, True]
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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                print(self.snake.snake_cells)
        self.score, self.foods = self.snake.move(self.score, self.foods, WIDTH, HEIGHT)

    def show(self, app):  # функция отображения начального окна
        self.main(app,
                  self)  # вызов функции main из родительского класса Scene, аналогично, по идее, можно будет ее вызывать в остальных классах сцен
