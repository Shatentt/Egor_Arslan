from app.settings import *


class Scene:
    def __init__(self):
        pass

    def print_text(self, app, text, text_coord, interval=10,
                   size=30):  # app - объект класса приложения, функция отображает текст на экране
        font = pygame.font.Font(None, size)
        for line in text:
            string_rendered = font.render(line, True, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = text_coord
            intro_rect.x = interval
            text_coord += intro_rect.height
            app.screen.blit(string_rendered, intro_rect)

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

    def terminate(self):
        pygame.quit()
        sys.exit()

    def update(self, events):
        pass

    def main(self, app, obj):  # obj - объект класса сцены которую мы собираемся отображать
        """"Используется obj, тк у каждого класса сцены будут своя обработка событий
               Все это происходит в функции processing, которую нужно создавать в каждом классе сцены"""
        running = True
        pref = app.current_scene
        while running:  # цикл отображения сцены класса obj
            obj.processing(app)
            if pref != app.scenes.index(True):
                app.switch_scene(app.scenes.index(True))  # смена сцены
                running = False
            pref = app.current_scene
            pygame.display.flip()
            app.clock.tick(app.fps)
