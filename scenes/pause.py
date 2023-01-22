from app import _settings
from ._base import *
from objects.button import ButtonRect


class Pause(Scene):
    def __init__(self):
        super().__init__()
        self.btn_finish = ButtonRect(310, 520, 200, 100, "to Menu", 30, '#D2E0BF', '#729246', '#282B28', 20)

    def show(self, app):
        text1 = ['PAUSE']
        under_fon = pygame.transform.scale(self.load_image('screenshot.png'), (WIDTH, HEIGHT))
        fon2 = pygame.transform.scale(self.load_image('fon.jpg'), (600, 450))
        app.screen.blit(under_fon, (0, 0))
        app.screen.blit(fon2, (180, 150))
        self.print_text(app, text1, 190, 210, size=80)
        self.main(app, self)

    def processing(self, app):
        events = pygame.event.get()
        self.btn_finish.hover(events)
        self.btn_finish.show(app.screen)
        for event in events:
            if event.type == pygame.QUIT:
                self.terminate()
            if self.btn_finish.is_clicked(events):
                app.scenes = [True, False, False, False, False]
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                app.scenes = [False, True, False, False, False]
