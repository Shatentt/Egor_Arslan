import pygame

import app._settings
from scenes._base import Scene
from scenes.pause import Pause
from scenes.game import SceneGame
from scenes.settings import Settings
from scenes.start import Start_Scene
from app._settings import *
from scenes.statistics import SceneStatistics


class App:
    def __init__(self):
        pygame.init()
        self.scenes = [True, False, False,  # какая сцена сейчас отображается
                       False, False]  # начальное окно, игра, Настройки, меню паузы, статистика
        self.width, self.height = WIDTH, HEIGHT
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake')
        self.fps = FPS
        self.current_scene = self.scenes.index(True)  # текущий индекс сцены
        self.class_scenes = {
            4: SceneStatistics(),
            3: Pause(),
            2: Settings(),
            1: SceneGame(),
            0: Start_Scene()
        }
        self.start_scene = Start_Scene()  # объект сцены начального экрана
        self.settings = Settings()
        self.game_scene = SceneGame()
        self.menu_pause = Pause()
        self.stats_scene = SceneStatistics()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def switch_scene(self, scene):  #
        self.current_scene = scene

    def reset_game(self):
        self.game_scene = SceneGame()

    def start(self):  # функция старта основного цикла програмы(где за один проход цикла меняется одна сцена)
        while True:
            self.class_scenes[self.current_scene].update(pygame.event.get())
            if self.current_scene == 0:  # в случае если индекс сцены - 1, то запускаем функцию с циклом отображения сцены начального экрана
                self.start_scene.show(self)
                print('Метод запуска сцены начального экрана запущен')
            if self.current_scene == 1:
                self.game_scene.show(self)
            if self.current_scene == 2:
                self.settings.show(self)
            if self.current_scene == 3:
                self.menu_pause.show(self)
            if self.current_scene == 4:
                self.stats_scene.show(self)