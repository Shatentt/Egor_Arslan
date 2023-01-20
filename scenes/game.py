from random import randrange

import pygame

from app import _settings
from app._settings import COLOR_RED, WIDTH, HEIGHT, CELL_SIZE, COLOR_YELLOW, COLOR_GREY, COLOR_BLUE, COLOR_GREEN, \
    game_goes
from objects.food import Food
from objects.snake import Snake
from scenes._base import Scene


class SceneGame(Scene):
    def __init__(self):
        super().__init__()
        self.snake = Snake(COLOR_BLUE)
        self.food = Food([randrange(1, WIDTH / CELL_SIZE) * CELL_SIZE, randrange(4, HEIGHT / CELL_SIZE) * CELL_SIZE], COLOR_RED)
        self.score = 0
        self.clock = pygame.time.Clock()
        self.ticks = 0
        _settings.game_goes = True
        self.clock.tick()
    def processing(self,
                   app):  # функция processing обрабатывает события, для стартового окна к примеру, после нажатия Enter, будет сменяться текущая сцена на сцену игры
        events = pygame.event.get()
        app.screen.fill(COLOR_GREEN)
        pygame.draw.rect(app.screen, COLOR_GREY, pygame.Rect(0, 0, WIDTH, CELL_SIZE * 3))
        tick = self.clock.tick()
        if _settings.game_goes:
            self.ticks += tick
        seconds = int(self.ticks / 1000 % 60)
        minutes = int(self.ticks / 60000 % 24)
        time_text = [f"Time {minutes:02d}:{seconds:02d}"]
        self.print_text(app, time_text, 20, 220, 50)
        _settings.game_goes = True
        self.snake.draw_snake(app.screen)
        self.food.draw(app.screen)
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
        self.score, self.food.food_pos = self.snake.move(self.score, self.food.food_pos, WIDTH, HEIGHT)

    def show(self, app):  # функция отображения начального окна
        self.main(app,
                  self)  # вызов функции main из родительского класса Scene, аналогично, по идее, можно будет ее вызывать в остальных классах сцен
