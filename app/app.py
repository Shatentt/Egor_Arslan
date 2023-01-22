from scenes.pause import Pause
from scenes.game import SceneGame
from scenes.settings import Settings
from scenes.start import Start_Scene
from app._settings import *
from scenes.statistics import SceneStatistics
from scenes.finish import Finish


class App:
    """
    Класс приложения

    Атрибуты
    ------------------
    scenes - список булева-переменных, показывает, какая из сцен отображается на данный момент в окне
    [Начальное окно, Игра, Настройки, Меню паузы, Статистика]

    width, height - переменные ширины и высоты окна в пикселях
    clock - объект класса pygame.time.Clock отвечающий за время в приложении
    screen - главное окно приложения
    fps - кадры в секунду
    current_scene - индекс текущей сцены
    class_scenes - словарь с объектами сцен соответствующих своим индексам
    start_scene, settings, game_scene, menu_pause, stats_scene, finish - переменные с объектами сцен

    Методы
    ---------------------
    terminate - завершить работу программы
    switch_scene - смена сцены
    reset_game - обновление окна игры(змейка встает в исходное положение, все данные предыдущей игры сбрасываются)
    start - функция старта основного цикла, который запускает сцены
    """
    def __init__(self):
        pygame.init()
        self.scenes = [True, False, False,  #
                       False, False, False]  # начальное окно, игра, Настройки, меню паузы, статистика
        self.width, self.height = WIDTH, HEIGHT
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake')
        self.fps = FPS
        self.current_scene = self.scenes.index(True)  # текущий индекс сцены
        self.class_scenes = {
            5: Finish(),
            4: SceneStatistics(),
            3: Pause(),
            2: Settings(),
            1: SceneGame(),
            0: Start_Scene()
        }
        self.start_scene = Start_Scene()  # объект сцены начального экрана
        self.settings = Settings()
        self.game_scene = SceneGame()
        self.menu_pause = Pause()
        self.stats_scene = SceneStatistics()
        self.finish = Finish()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def switch_scene(self, scene):
        """Обновляем текущий индекс сцены в self.scenes на scene"""
        self.current_scene = scene

    def reset_game(self):
        """Обновление данных предыдущей игры"""
        self.game_scene = SceneGame()

    def start(self):  # функция старта основного цикла програмы(где за один проход цикла меняется одна сцена)
        """
        Запуск основного цикла программы
        За один проход меняется одна сцена
        В зависимости от сцены отображается соотвествующая сцена
        :return:
        """
        while True:
            self.class_scenes[self.current_scene].update(pygame.event.get())
            if self.current_scene == 0:
                # в случае если индекс сцены - 0, то запускаем функцию с циклом отображения сцены начального экрана
                self.start_scene.show(self)
            if self.current_scene == 1:
                self.game_scene.show(self)
            if self.current_scene == 2:
                self.settings.show(self)
            if self.current_scene == 3:
                self.menu_pause.show(self)
            if self.current_scene == 4:
                self.stats_scene.show(self)
            if self.current_scene == 5:
                self.finish.show(self)
