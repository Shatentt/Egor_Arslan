from objects.button import ButtonRect
from ._base import Scene
from app._settings import *


class Start_Scene(Scene):  # класс стартововй сцены
    def __init__(self):
        super().__init__()
        self.button_play = ButtonRect(120, 350, 200, 100, "PLAY", 30, '#D2E0BF', '#729246', '#282B28', 20)
        self.button_stats = ButtonRect(120, 475, 200, 100, "STATISTICS", 30, '#D2E0BF', '#729246', '#282B28', 20)
        self.button_settings = ButtonRect(120, 600, 200, 100, "SETTINGS", 30, '#D2E0BF', '#729246', '#282B28', 20)
        self.button_exit = ButtonRect(120, 725, 200, 100, "EXIT", 30, '#D1A7A0', '#965044', '#282B28', 20)

    def processing(self,
                   app):  # функция processing обрабатывает события, для стартового окна к примеру, после нажатия Enter, будет сменяться текущая сцена на сцену игры
        events = pygame.event.get()
        self.button_play.hover(events)
        self.button_stats.hover(events)
        self.button_exit.hover(events)
        self.button_settings.hover(events)
        self.button_play.show(app.screen)
        self.button_stats.show(app.screen)
        self.button_settings.show(app.screen)
        self.button_exit.show(app.screen)
        if self.button_play.is_clicked(events):
            app.scenes = [False, True, False, False, False]
            app.reset_game()
        if self.button_settings.is_clicked(events):
            app.scenes = [False, False, True, False, False]
        if self.button_exit.is_clicked(events):
            self.terminate()
        if self.button_stats.is_clicked(events):
            app.scenes = [False, False, False, False, True]
        for event in events:
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.terminate()

    def show(self, app):  # функция отображения начального окна
        intro_text = ["Змейка", "",
                      "Правила игры",
                      "Вы играете за змейку",
                      "Вам нужно есть яблоки",
                      "Но будьте аккуратнее: Не врезайтесь в стенки и в себя",
                      "Удачи!"]
        fon = pygame.transform.scale(self.load_image('fon.jpg'), (WIDTH, HEIGHT))
        app.screen.blit(fon, (0, 0))
        self.print_text(app, intro_text, 50, 20, 10, 30)
        self.button_play.show(app.screen)
        self.button_stats.show(app.screen)
        self.button_exit.show(app.screen)
        self.main(app,
                  self)  # вызов функции main из родительского класса Scene, аналогично, по идее, можно будет ее вызывать в остальных классах сцен
