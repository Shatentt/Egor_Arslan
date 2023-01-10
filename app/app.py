from scenes._base import Scene
from scenes.menu import Menu
from scenes.start import Start_Scene
from app.settings import *


class App:
    def __init__(self):
        pygame.init()
        self.scenes = [True, False, False, False]  # начальное окно, игра, меню паузы, меню
        self.width, self.height = 800, 600
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Mario')
        self.fps = 50
        self.current_scene = self.scenes.index(True)

        self.scene = Scene(self.screen)

        self.start_scene = Start_Scene(self.screen)

        self.menu = Menu(self.screen)  #
        self.menu.append_option('Hello', lambda: print('Hello'))  #
        self.menu.append_option('Quit', pygame.quit)  #

    def terminate(self):
        pygame.quit()
        sys.exit()

    def switch_scene(self, scene):  #
        self.current_scene = scene

    def start(self):
        while True:
            pref = 3
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
            running = True
            print(self.current_scene)
            if self.current_scene == 0:
                self.start_scene.show()
            elif self.current_scene == 3:
                self.menu.draw(self.screen, 100, 100, 75)
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.terminate()
                # for scene in range(len(self.scenes)):
                if pref != self.current_scene:
                    self.switch_scene(self.scenes.index(True))
                    running = False
                pref = self.current_scene


                    # elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  #
                    #     self.menu.draw(self.screen, 100, 100, 75)
                    # elif event.type == pygame.KEYDOWN or \
                    #         event.type == pygame.MOUSEBUTTONDOWN:
                    #     return  # начинаем игру

            pygame.display.flip()
            self.clock.tick(self.fps)

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