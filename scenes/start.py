from ._base import Scene
from app.settings import *


class Start_Scene(Scene):
    def __init__(self, screen):
        super().__init__(screen)

    def show(self):
        intro_text = ["Змейка", "",
                      "Правила игры",
                      "Вы играете за змейку",
                      "Вам нужно есть яблоки",
                      "Но будьте аккуратнее: Не врезайтесь в стенки и в себя",
                      "Удачи!"]
        # (pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])
        fon = pygame.transform.scale(self.load_image('fon.jpg'), (800, 600))
        self.screen.blit(fon, (0, 0))
        self.print_text(intro_text, 50, 10, 30)