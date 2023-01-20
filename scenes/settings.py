from ._base import Scene
from app._settings import *
import pygame
from objects.button import ButtonTriag
from objects.button import ButtonRect


class Settings(Scene):  #
    def __init__(self):
        super().__init__()
        self.btn_board_plus = ButtonTriag(400, 175, '#729246', '#D2E0BF')
        self.button_left2 = ButtonTriag(400, 300, '#729246', '#D2E0BF')
        self.button_left3 = ButtonTriag(400, 425, '#729246', '#D2E0BF')
        self.btn_board_minus = ButtonTriag(550, 175, '#729246', '#D2E0BF')
        self.button_right2 = ButtonTriag(550, 300, '#729246', '#D2E0BF')
        self.button_right3 = ButtonTriag(550, 425, '#729246', '#D2E0BF')
        self.button_back = ButtonRect(200, 740, 200, 100, "BACK", 30, '#D1A7A0', '#965044', '#282B28', 20)

    def show(self, app):
        text1 = ['SETTINGS']
        text2 = ['Size of the board',
                 'Something',
                 'Something']
        fon = pygame.transform.scale(self.load_image('fon.jpg'), (WIDTH, HEIGHT))
        app.screen.blit(fon, (0, 0))
        self.print_text(app, text2, 160, 20, size=50, interval=100)
        self.print_text(app, text1, 50, 20, size=80)
        self.main(app, self)

    def processing(self, app):
        events = pygame.event.get()
        self.btn_board_plus.hover(events)
        self.button_left2.hover(events)
        self.button_left3.hover(events)
        self.btn_board_minus.hover(events)
        self.button_right2.hover(events)
        self.button_right3.hover(events)
        self.button_back.hover(events)
        self.btn_board_minus.show_right(app.screen)
        self.button_right2.show_right(app.screen)
        self.button_right3.show_right(app.screen)
        self.btn_board_plus.show_left(app.screen)
        self.button_left2.show_left(app.screen)
        self.button_left3.show_left(app.screen)
        self.button_back.show(app.screen)
        for event in events:
            if self.button_back.is_clicked(events):
                app.scenes = [True, False, False, False]
            if self.btn_board_plus.is_clicked(events):
                pass
            if self.btn_board_minus.is_clicked(events):
                pass
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                app.scenes = [True, False, False, False]
