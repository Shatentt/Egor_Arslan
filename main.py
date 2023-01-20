from app import _settings
from app._settings import CELL_SIZE
from app.app import App

def main():
    app = App()
    app.start()  # функция старта основного цикла всей игры
    # app_full.run_game()


if __name__ == '__main__':
    main()
