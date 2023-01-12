from ._base import Scene
from app_full.settings import *


class Start_Scene(Scene):  # класс стартововй сцены
    def processing(self,
                   app):  # функция processing обрабатывает события, для стартового окна к примеру, после нажатия Enter, будет сменяться текущая сцена на сцену игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.terminate()
                # app.scenes[0] = False
                # app.scenes[3] = True

    def show(self, app):  # функция отображения начального окна
        intro_text = ["Змейка", "",
                      "Правила игры",
                      "Вы играете за змейку",
                      "Вам нужно есть яблоки",
                      "Но будьте аккуратнее: Не врезайтесь в стенки и в себя",
                      "Удачи!"]
        fon = pygame.transform.scale(self.load_image('fon.jpg'), (800, 600))
        app.screen.blit(fon, (0, 0))
        self.print_text(app, intro_text, 50, 10, 30)
        self.main(app,
                  self)  # вызов функции main из родительского класса Scene, аналогично, по идее, можно будет ее вызывать в остальных классах сцен
