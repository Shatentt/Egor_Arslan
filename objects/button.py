from app_full.settings import *


button_sound = None
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