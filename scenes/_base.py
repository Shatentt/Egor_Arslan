from app.settings import *

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