from app._settings import *


class Scene:
    """
    Родительский класс сцены(от него наследуется каждая сцена)

    Атрибуты
    -----------------------------

    Методы
    -----------------------------
    print_text - функция написания текста на поверности
    load_image - загрузка изображения и представления в виде массива пикселей
    terminate - завершение работы программы
    main - функция цикла отображения сцены
    """
    def __init__(self):
        pass

    def print_text(self, app, text, text_coord, text_coordx, interval=10, size=30):
        """
        Отображение текста на основной поверхности приложения
        :param app: объект класса приложения
        :param text: список, которые нужно отобразить друг под другом
        :param text_coord: координаты по Оу
        :param text_coordx: координаты по Ох
        :param interval: интервал в пикселях между строками пикселей
        :param size: размер текста
        """
        font = pygame.font.Font(None, size)
        for line in text:
            string_rendered = font.render(line, True, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            if text[0] != line:
                text_coord += interval
            intro_rect.top = text_coord
            intro_rect.x = text_coordx
            text_coord += intro_rect.height
            app.screen.blit(string_rendered, intro_rect)

    def load_image(self, name, colorkey=None):
        """
        Загрузка изображения
        :param name: имя файла
        """
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
        """
        Завершение работы программы
        """
        pygame.quit()
        sys.exit()

    def update(self, events):
        pass

    def main(self, app, obj):  # obj - объект класса сцены которую мы собираемся отображать
        """
        основной цикл отображение одной сцены типа obj
        :param app: объект приложения
        :param obj: объект сцены которая сейчас отображается(чтобы использовать фун-ю processing именно действующей сцены)
        """
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
