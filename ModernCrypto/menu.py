from constants import WIDTH
from typing import Callable, Any, Literal
from tkinter import Frame, Misc, Label, Event, Canvas


class Menu(Frame):
    BG_COLOR = "#f8f9fb"
    FONT = "Inter 12"

    def __init__(self, master: Misc):
        Frame.__init__(self, master, bg=self.BG_COLOR)
        self.label_algorithms = Label(self, text="Алгоритмы", bg=self.BG_COLOR, font=self.FONT)
        self.label_algorithms.place(x=10, y=25)

        self.aes_button = MenuButton(self, "AES", self.select_menu, select=True)
        self.selected_menu_button = self.aes_button
        self.aes_button.place(y=55)

        self.rsa_button = MenuButton(self, "RSA", self.select_menu)
        self.rsa_button.place(y=100)

        self.sha_button = MenuButton(self, "SHA-2", self.select_menu)
        self.sha_button.place(y=145)

        self.sign_button = MenuButton(self, "Цифровая подпись", self.select_menu)
        self.sign_button.place(y=190)

    def select_menu(self, event: Event):
        """
        Функция-обработчик события выбора пункта меню
        :param event: системный объект события
        """

        self.selected_menu_button.selected = False
        event.widget.selected = True
        self.selected_menu_button = event.widget


class MenuButton(Canvas):
    SELECTED_COLOR = "#d0daf4"  # Цвет выбранного пункта меню
    ENTERED_COLOR = "#e1e7f5"  # Цвет наведенного курсором пункта меню
    FONT = "Inter 12"

    def __init__(self, master: Misc, text: str, command: Callable[[Event], Any], select: bool = False):
        Canvas.__init__(self, master, width=WIDTH // 4, height=45, bg=master.cget("bg"), highlightthickness=0)

        # selected - пункт меню выбран, entered - на пункт меню наведен курсор
        self._selected = self._entered = select

        self._highlighting = None  # polygon, показывающий состояние пункта меню
        if self._selected:
            self.highlight("selected")

        self.bind("<Enter>", self.enter)
        self.bind("<Leave>", self.leave)
        self.bind("<Button-1>", command)

        self.create_text(20, 20, text=text, font=self.FONT, anchor="w")

    def enter(self, event: Event):
        """
        Функция-обработчик события наведения курсора на пункт меню: окрашивание в тусклый голубой цвет
        :param event: системный объект события
        """

        event.widget.config(cursor="hand2")
        self._entered = True
        if not self._selected:
            self.highlight("entered")  # Выделение пункта меню, если он не выбран

    def leave(self, _: Event):
        """
        Функция-обработчик события выведение курсора из области пункта меню: возвращение цвета
        :param _: системный объект события
        """

        self._entered = False
        if not self._selected:
            self.highlight("normal")  # Удаление выделения пункта меню

    def highlight(self, mode: Literal["selected", "entered", "normal"]):
        """
        Изменение выделения у пункта меню (выбранный, с наведенным курсором, обычный)
        :param mode: режим выделения
        """

        if mode == "normal":  # Удаление выделения
            self.delete(self._highlighting)
            self._highlighting = None

        else:  # Выбор нужного цвета выделения и создание закругленного прямоугольника
            fill = self.SELECTED_COLOR if mode == "selected" else self.ENTERED_COLOR
            self._highlighting = self.create_rounded_rectangle(10, 0, WIDTH // 4 - 10, 40, 10, fill=fill)

            self.tag_lower(self._highlighting)  # Опускание на задний план

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        """
        Создание закругленного прямоугольника с помощью Canvas.create_polygon
        :param x1: координата x левого верхнего угла
        :param y1: координата y левого верхнего угла
        :param x2: координата x нижнего правого угла
        :param y2: координата y нижнего правого угла
        :param radius: радиус закругления углов прямоугольника
        :param kwargs: другие параметры для create_polygon
        :return: CanvasId созданного polygon
        """

        radius = min(radius, (x2 - x1) / 2, (y2 - y1) / 2)  # Радиус не более половины наименьшей стороны
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    @property
    def selected(self) -> bool:
        """Состояние данного пункта меню"""

        return self._selected

    @selected.setter
    def selected(self, selected: bool):
        """Изменение состояния данного пункта меню"""

        if self._selected == selected:
            return

        self._selected = selected
        self.highlight("normal")  # Удаление выделения
        if self._selected:
            self.highlight("selected")
