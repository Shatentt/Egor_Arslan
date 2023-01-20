from app._settings import *


class Button:
    def __init__(self, x, y, bg_color1, bg_color2):
        self.x, self.y = x, y
        self.color_current = bg_color1
        self.color_1 = bg_color1
        self.color_2 = bg_color2
        self.rect = pygame.Rect(x - 25, y - 25, 50, 50)  # емного заколхозил

    def hover(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.color_current = self.color_2
                else:
                    self.color_current = self.color_1

    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    return True
        return False


class ButtonTriag(Button):
    def __init__(self, x, y, bg_color1, bg_color2):
        super().__init__(x, y, bg_color1, bg_color2)

    def show_left(self, screen):
        pygame.draw.rect(screen, self.color_current, self.rect)
        image = pygame.image.load('data/btn_left.png')
        image = pygame.transform.scale(image, (50, 50))
        screen.blit(image, self.rect)

    def show_right(self, screen):
        pygame.draw.rect(screen, self.color_current, self.rect)
        image = pygame.image.load('data/btn_right.png')
        image = pygame.transform.scale(image, (50, 50))
        screen.blit(image, self.rect)


class ButtonRect(Button):
    def __init__(self, x, y, w, h, text, size, bg_color1, bg_color2, text_color, border_radius):
        super().__init__(x, y, bg_color1, bg_color2)
        self.rect = pygame.Rect(x - w / 2, y - h / 2, w, h)
        font = pygame.font.SysFont(pygame.font.get_fonts()[0], size)
        self.text = font.render(text, False, text_color)
        self.border_radius = border_radius

    def show(self, screen):
        pygame.draw.rect(screen, self.color_current, self.rect, border_radius=self.border_radius)
        w, h = self.text.get_size()
        screen.blit(self.text, (self.x - w / 2, self.y - h / 2))
