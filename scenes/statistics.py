from app import _settings
from ._base import Scene
from app._settings import *
import pygame
from objects.button import ButtonTriag
from objects.button import ButtonRect
import os


class SceneStatistics(Scene):  #
    def __init__(self):
        super().__init__()
        self.button_back = ButtonRect(200, 740, 200, 100, "BACK", 30, '#D1A7A0', '#965044', '#282B28', 20)
        self.button_clear = ButtonRect(500, 740, 200, 100, "CLEAR STATISTICS", 25, '#D1A7A0', '#965044', '#282B28', 20)

    def show(self, app):
        self.main(app, self)

    def read_data(self):
        try:
            with open(file="data/statistics.txt", mode="r") as f:
                text = f.read()
                return text
        except:
            with open(file="data/statistics.txt", mode="w") as f:
                return ""

    def find_best_results(self, data):
        # функция, которая ищет лучший результат для каждого режима
        best_results = []
        for i in range(len(data) - 1):
            str_list = data[i].split(", ")
            gamemodes = [best_results[i][5] for i in range(len(best_results))]
            if str_list[5] not in gamemodes:
                best_results.append(str_list)
            for i in range(len(best_results)):
                if str_list[5] == best_results[i][5]:
                    if int(str_list[0]) > int(best_results[i][0]):
                        best_results[i] = str_list
        for i in range(len(best_results)):
            best_results[i] = ", ".join(best_results[i])
        return best_results

    def processing(self, app):
        events = pygame.event.get()
        txt = self.read_data()
        data = txt.split("\n")
        text1 = ['STATISTICS']
        text2 = ['3 последние игры:',
                 'Лучшие результаты(по режимам игры):']
        text3 = data[-2:-5:-1]
        text4 = ['Статистика показана в формате', '"score, time, board size, food amount, speed, game mode, result"']
        text5 = self.find_best_results(data)
        fon = pygame.transform.scale(self.load_image('fon.jpg'), (WIDTH, HEIGHT))
        app.screen.blit(fon, (0, 0))
        self.print_text(app, text1, 50, 20, size=80)
        self.print_text(app, text2, 160, 20, size=50, interval=200)
        self.print_text(app, text3, 210, 20, size=50, interval=30)
        self.print_text(app, text4, 102, 20, size=35, interval=5)
        self.print_text(app, text5, 440, 20, size=40, interval=10)
        self.button_back.hover(events)
        self.button_clear.hover(events)

        self.button_back.show(app.screen)
        self.button_clear.show(app.screen)

        for event in events:
            if self.button_back.is_clicked(events):
                app.scenes = [True, False, False, False, False, False]
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                app.scenes = [True, False, False, False, False, False]
            if self.button_clear.is_clicked(events):
                try:
                    os.remove("data/statistics.txt")
                except:
                    pass
