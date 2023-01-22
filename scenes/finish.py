from ._base import *
from objects.button import ButtonRect
from objects.snake_animated import Snake_Animated

class Finish(Scene):
    def __init__(self):
        super().__init__()
        self.btn_finish = ButtonRect(200, 800, 200, 100, "TO MENU", 30, '#D2E0BF', '#65656C', '#282B28', 20)
        self.btn_replay = ButtonRect(420, 800, 200, 100, "PLAY AGAIN", 30, '#D2E0BF', '#65656C', '#282B28', 20)
        self.snake = Snake_Animated(self.load_image('sprites.png'), 12, 2, 700, 700)

    def show(self, app):
        app.fps = 10
        self.background = pygame.transform.scale(self.load_image('finish_scene.jpg'), (WIDTH, HEIGHT))
        self.main(app, self)

    def processing(self, app):
        app.screen.blit(self.background, (0, 0))
        self.snake.all_sprites.update()
        self.snake.all_sprites.draw(app.screen)
        events = pygame.event.get()
        self.btn_finish.hover(events)
        self.btn_replay.hover(events)
        self.btn_finish.show(app.screen)
        self.btn_replay.show(app.screen)
        self.print_text(app, [f'SCORE:  {app.game_scene.score}'], 50, 50)
        self.print_text(app, [f'TIME:  {app.game_scene.minutes} minutes {app.game_scene.seconds} seconds'], 50, 200)
        for event in events:
            if event.type == pygame.QUIT:
                self.terminate()
            if self.btn_finish.is_clicked(events):
                app.scenes = [True, False, False, False, False, False]
                app.fps = FPS
            if self.btn_replay.is_clicked(events):
                app.scenes = [False, True, False, False, False, False]
                app.reset_game()
                app.fps = FPS
