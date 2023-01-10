import os
import sys
import pygame

pygame.font.init()
pygame.mixer.init()
button_sound = None

ARIAL = pygame.font.SysFont('arial', 30)


class Button:
    def __init__(self, width, height, inactive_col, active_col):
        self.width = width
        self.height = height
        self.inactive_col = inactive_col
        self.active_col = active_col

    def draw(self, x, y, message, screen, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, (23, 204, 58), (x, y, self.width, self.height))
                if click[0]:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300)
                    if action is not None:
                        action()
        else:
            pygame.draw.rect(screen, (13, 162, 58), (x, y, self.width, self.height))


class Scene:
    def __init__(self, screen):
        self.current_scene = None
        self.screen = screen

    def print_text(self, text, text_coord, interval=10, size=30):
        font = pygame.font.Font(None, size)
        for line in text:
            string_rendered = font.render(line, True, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += interval
            intro_rect.top = text_coord
            intro_rect.x = interval
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image


class Menu(Scene):  #
    def __init__(self, screen):
        super().__init__(screen)
        self._option_surfaces = []
        self._callback = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(ARIAL.render(option, True, (255, 255, 255)))
        self._callback.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callback[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)



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

    def finish_game_won(self):
        while True:
            mouse = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.terminate()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.width / 2 <= mouse[0] <= self.width / 2 + 140 \
                            and self.height / 2 <= mouse[1] <= self.height / 2 + 40:
                        self.restart = True
                        pygame.quit()
            for ev in pygame.event.get():
                if ev.type != pygame.QUIT:
                    self.screen.fill(pygame.Color('green'))
                    smallfont = pygame.font.SysFont('Corbel', 35)
                    text_1 = smallfont.render('restart', True, (255, 255, 255))
                    text_2 = smallfont.render('you won', True, (255, 255, 255))
                    pygame.draw.rect(self.screen, (170, 170, 170), [self.width / 2, self.height / 2, 140, 40])
                    self.screen.blit(text_1, (self.width / 2 + 50, self.height / 2))
                    self.screen.blit(text_2, (self.width / 2 + 50, self.height / 2 - 100))
                    pygame.display.flip()
                    self.clock.tick(self.fps)

    def finish_game_lost(self):
        while True:
            mouse = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.terminate()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.width / 2 <= mouse[0] <= self.width / 2 + 140 \
                            and self.height / 2 <= mouse[1] <= self.height / 2 + 40:
                        self.restart = True
                        pygame.quit()
            for ev in pygame.event.get():
                if ev.type != pygame.QUIT:
                    self.screen.fill(pygame.Color('red'))
                    smallfont = pygame.font.SysFont('Corbel', 35)
                    text_1 = smallfont.render('restart', True, (255, 255, 255))
                    text_2 = smallfont.render('you have lost, Game Over', True, (255, 255, 255))
                    pygame.draw.rect(self.screen, (170, 170, 170), [self.width / 2, self.height / 2, 140, 40])
                    self.screen.blit(text_1, (self.width / 2 + 50, self.height / 2))
                    self.screen.blit(text_2, (50, self.height / 2 - 100))
                    pygame.display.flip()
                    self.clock.tick(self.fps)


if __name__ == '__main__':
    app = App()
    app.start()
    # app.start_screen()
    # app.run_game()
