import os
import sys
import pygame


class App:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Mario')
        self.fps = 50

    def terminate(self):
        pygame.quit()
        sys.exit()

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
    app.run_game()