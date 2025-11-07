import os
import sys

from menu import Menu
from tkinter import Tk, Event
from main_frame import MainFrame
from constants import WIDTH, HEIGHT


class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Современные криптографические алгоритмы")
        center_x = (self.winfo_screenwidth() - WIDTH) // 2
        center_y = (self.winfo_screenheight() - HEIGHT) // 2
        self.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, center_x, center_y))
        self.minsize(WIDTH, HEIGHT)
        self.iconbitmap(resource_path("icon.ico"))
        self.bind("<Configure>", self.window_configure)  # Обработка изменений размеров и положения окна

        # Меню со списком доступных алгоритмов
        self.menu = Menu(self)
        self.menu.place(width=WIDTH // 4, relheight=1)

        # Основная (рабочая) область программы
        self.main_frame = MainFrame(self)
        self.main_frame.place(x=WIDTH // 4, relheight=1, width=0.75 * WIDTH)

    def window_configure(self, _: Event):
        # Изменение абсолютной ширины основной области
        self.main_frame.place(x=WIDTH // 4, relheight=1, width=self.winfo_width() - WIDTH // 4)


def resource_path(relative_path: str) -> str:
    """
    Получает путь к файлу для работы из исполняемого exe и при тестировании
    :param relative_path: относительный путь файла в проекте
    :return: правильный путь
    """

    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
