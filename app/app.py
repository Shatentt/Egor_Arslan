import pygame

from scenes._base import Scene
from scenes.game import SceneGame
from scenes.menu import Menu
from scenes.start import Start_Scene
from app.settings import *


class App:
    def __init__(self):
        pygame.init()
        self.scenes = [True, False, False,
                       False]  # начальное окно, игра, меню паузы, меню (какая сцена сейчас отображается)
        self.width, self.height = WIDTH, HEIGHT
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake')
        self.fps = FPS
        self.current_scene = self.scenes.index(True)  # текущий индекс сцены
        self.class_scenes = {
            2: Menu(),
            1: SceneGame(),
            0: Start_Scene()
        }
        self.start_scene = Start_Scene() # объект сцены начального экрана
        self.menu_scene = Menu()
        self.game_scene = SceneGame()

        # self.menu = Menu(self.screen)  #
        # self.menu.append_option('Hello', lambda: print('Hello'))  #
        # self.menu.append_option('Quit', pygame.quit)  #

    def terminate(self):
        pygame.quit()
        sys.exit()

    def switch_scene(self, scene):  #
        self.current_scene = scene

    def start(self):  # функция старта основного цикла програмы(где за один проход цикла меняется одна сцена)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
            self.class_scenes[self.current_scene].update(pygame.event.get())
            if self.current_scene == 0:  # в случае если индекс сцены - 1, то запускаем функцию с циклом отображения сцены начального экрана
                self.start_scene.show(self, self.screen)
                print('Метод запуска сцены начального экрана запущен')
            if self.current_scene == 1:
                self.game_scene.show(self, self.screen)

                # elif self.current_scene == 3:
                #     self.menu.draw(self.screen, 100, 100, 75)

    def run_game(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
            # update
            self.class_scenes[self.current_scene].update(pygame.event.get())
            # render
            self.screen.fill(pygame.Color('blue'))
            pygame.display.flip()
            self.clock.tick(self.fps)
