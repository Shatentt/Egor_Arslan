import pygame


class Snake_Animated(pygame.sprite.Sprite):
    """
    Класс Анимации змеи на финишной сцене

    Атрибуты
    -------------------------------
    all_sprites - группа спрайтов
    frames - спрайты-изображения в виде массивов пикселей
    cur_frame - индекс текущего спрайт-изображения
    image - текущее спрайт-изображение
    rect - прямоугольное поле, на котором будет лежать спрайт

    Методы
    -------------------------------
    cut_sheet - разрезает картинку со спрайтами на отдельные спрайт-изображения
    update - обновление спрайт-изображения
    """
    def __init__(self, sheet, columns, rows, x, y):
        self.all_sprites = pygame.sprite.Group()
        super().__init__(self.all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        """
        функция разрезания картинки со спрайтами на отдельные спрайты
        :param sheet: картинка со спрайтами
        :param columns: количество колонок
        :param rows: количество строк
        """
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        """
        Меняет текущий спрайт на следующий
        """
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]