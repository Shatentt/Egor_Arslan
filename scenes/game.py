from random import randrange

import pygame
from app.settings import COLOR_RED, WIDTH, HEIGHT, CELL_SIZE
from objects.food import Food
from objects.snake import Snake
from scenes._base import Scene


class SceneGame(Scene):
    def __init__(self):
        super().__init__()
        self.snake = Snake(COLOR_RED)
        self.food = Food([randrange(1, WIDTH / CELL_SIZE) * CELL_SIZE, randrange(1, HEIGHT / CELL_SIZE) * CELL_SIZE], COLOR_RED)
        self.score = 0
    def processing(self,
                   app):  # функция processing обрабатывает события, для стартового окна к примеру, после нажатия Enter, будет сменяться текущая сцена на сцену игры
        events = pygame.event.get()
        flag_pressed = False # булевое значение, которое определяет, нажимал ли пользователь кнопки управления змейкой
        # нужен чтобы не было багов
        self.screen.fill('#999999')
        self.snake.draw_snake(self.screen)
        self.food.draw(self.screen)
        if self.snake.check_lose(WIDTH, HEIGHT):
            self.terminate()
        for event in events:
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.snake.change_dir("DOWN")
                flag_pressed = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.snake.change_dir("UP")
                flag_pressed = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.snake.change_dir("RIGHT")
                flag_pressed = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.snake.change_dir("LEFT")
                flag_pressed = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                print(self.snake.snake_cells)
        if not flag_pressed:
            self.score, self.food.food_pos = self.snake.move(self.score, self.food.food_pos, WIDTH, HEIGHT)

    def show(self, app, screen):  # функция отображения начального окна
        self.screen = screen
        screen.fill('#999999')
        self.main(app,
                  self)  # вызов функции main из родительского класса Scene, аналогично, по идее, можно будет ее вызывать в остальных классах сцен
