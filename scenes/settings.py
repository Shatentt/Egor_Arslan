from app import _settings
from ._base import Scene
from app._settings import *
import pygame
from objects.button import ButtonTriag
from objects.button import ButtonRect


class Settings(Scene):  #
    def __init__(self):
        super().__init__()
        y = 175
        inter = 80
        self.board_size = ["small", "medium", "big"]
        self.cur_size = 1
        self.color_food = ["apple", "orange", "grape"]
        self.cur_food = 0
        self.btn_board_plus = ButtonTriag(400, y, '#729246', '#D2E0BF')
        self.btn_board_minus = ButtonTriag(550, y, '#729246', '#D2E0BF')
        y += inter
        self.btn_food_amount_minus = ButtonTriag(400, y, '#729246', '#D2E0BF')
        self.btn_food_amount_plus = ButtonTriag(550, y, '#729246', '#D2E0BF')
        y += inter
        self.btn_food_color_minus = ButtonTriag(400, y, '#729246', '#D2E0BF')
        self.btn_food_color_plus = ButtonTriag(550, y, '#729246', '#D2E0BF')
        y += inter
        self.button_left4 = ButtonTriag(400, y, '#729246', '#D2E0BF')
        self.button_right4 = ButtonTriag(550, y, '#729246', '#D2E0BF')
        y += inter
        self.button_left5 = ButtonTriag(400, y, '#729246', '#D2E0BF')
        self.button_right5 = ButtonTriag(550, y, '#729246', '#D2E0BF')
        y += inter
        self.button_left6 = ButtonTriag(400, y, '#729246', '#D2E0BF')
        self.button_right6 = ButtonTriag(550, y, '#729246', '#D2E0BF')
        y += inter
        self.button_left7 = ButtonTriag(400, y, '#729246', '#D2E0BF')
        self.button_right7 = ButtonTriag(550, y, '#729246', '#D2E0BF')
        self.button_back = ButtonRect(200, 740, 200, 100, "BACK", 30, '#D1A7A0', '#965044', '#282B28', 20)

    def show(self, app):
        self.main(app, self)

    def change_cur_size(self, a):
        self.cur_size += a
        if self.cur_size == 3:
            self.cur_size = 0
        if self.cur_size == -1:
            self.cur_size = 2
        if self.cur_size == 0:
            _settings.CELL_SIZE = 30
        if self.cur_size == 1:
            _settings.CELL_SIZE = 20
        if self.cur_size == 2:
            _settings.CELL_SIZE = 10

    def change_food_amount(self, a):
        _settings.amount_of_food += a
        if _settings.amount_of_food > 5:
            _settings.amount_of_food = 1
        if _settings.amount_of_food < 1:
            _settings.amount_of_food = 5

    def change_food_color(self, a):
        self.cur_food += a
        if self.cur_food == 3:
            self.cur_food = 0
        if self.cur_food == -1:
            self.cur_food = 2
        if self.cur_food == 0:
            _settings.FOOD_COLOR = _settings.COLOR_RED
        if self.cur_food == 1:
            _settings.FOOD_COLOR = _settings.COLOR_ORANGE
        if self.cur_food == 2:
            _settings.FOOD_COLOR = _settings.COLOR_PURPLE

    def processing(self, app):
        events = pygame.event.get()
        text1 = ['SETTINGS']
        text2 = ['Size of the board',
                 'Amount of food',
                 'Food',
                 'Speed',
                 'Snake Color',
                 'Field Color',
                 'Game Mode']
        fon = pygame.transform.scale(self.load_image('fon.jpg'), (WIDTH, HEIGHT))
        app.screen.blit(fon, (0, 0))
        self.print_text(app, text2, 160, 20, size=50, interval=45)
        self.print_text(app, text1, 50, 20, size=80)
        self.print_text(app, [self.board_size[self.cur_size]], 165, 435, 50)
        self.print_text(app, [str(_settings.amount_of_food)], 245, 467, 50)
        self.print_text(app, [self.color_food[self.cur_food]], 325, 450, 50)

        self.btn_board_plus.hover(events)
        self.btn_board_minus.hover(events)
        self.btn_food_amount_minus.hover(events)
        self.btn_food_amount_plus.hover(events)
        self.btn_food_color_minus.hover(events)
        self.btn_food_color_plus.hover(events)
        self.button_left4.hover(events)
        self.button_right4.hover(events)
        self.button_left5.hover(events)
        self.button_right5.hover(events)
        self.button_left6.hover(events)
        self.button_right6.hover(events)
        self.button_left7.hover(events)
        self.button_right7.hover(events)
        self.button_back.hover(events)

        self.btn_board_plus.show_left(app.screen)
        self.btn_board_minus.show_right(app.screen)
        self.btn_food_amount_minus.show_left(app.screen)
        self.btn_food_amount_plus.show_right(app.screen)
        self.btn_food_color_minus.show_left(app.screen)
        self.btn_food_color_plus.show_right(app.screen)
        self.button_left4.show_left(app.screen)
        self.button_right4.show_right(app.screen)
        self.button_left5.show_left(app.screen)
        self.button_right5.show_right(app.screen)
        self.button_left6.show_left(app.screen)
        self.button_right6.show_right(app.screen)
        self.button_left7.show_left(app.screen)
        self.button_right7.show_right(app.screen)
        self.button_back.show(app.screen)

        for event in events:
            if self.button_back.is_clicked(events):
                app.scenes = [True, False, False, False]
            if self.btn_board_minus.is_clicked(events):
                self.change_cur_size(1)
                break
            if self.btn_board_plus.is_clicked(events):
                self.change_cur_size(-1)
                break
            if self.btn_food_amount_plus.is_clicked(events):
                self.change_food_amount(2)
                break
            if self.btn_food_amount_minus.is_clicked(events):
                self.change_food_amount(-2)
                break
            if self.btn_food_color_plus.is_clicked(events):
                self.change_food_color(1)
                break
            if self.btn_food_color_minus.is_clicked(events):
                self.change_food_color(-1)
                break
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print(_settings.CELL_SIZE)
                app.scenes = [True, False, False, False]
