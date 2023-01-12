from scenes._base import Scene
from scenes.menu import Menu
from scenes.start import Start_Scene
from app_full.settings import *


class App:
    def __init__(self):
        pygame.init()
        self.scenes = [True, False, False,
                       False]  # начальное окно, игра, меню паузы, меню (какая сцена сейчас отображается)
        self.width, self.height = WIDTH, HEIGHT
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Mario')
        self.fps = FPS
        self.current_scene = self.scenes.index(True)  # текущий индекс сцены

        self.start_scene = Start_Scene()  # объект сцены начального экрана

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
            print(self.current_scene)
            if self.current_scene == 0:  # в случае если индекс сцены - 1, то запускаем функцию с циклом отображения сцены начального экрана
                self.start_scene.show(self)
                print('Метод запуска сцены начального экрана запущен')

                # elif self.current_scene == 3:
                #     self.menu.draw(self.screen, 100, 100, 75)

    def run_game(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
            # update

            # render
            self.screen.fill(pygame.Color('blue'))
            pygame.display.flip()
            self.clock.tick(self.fps)
