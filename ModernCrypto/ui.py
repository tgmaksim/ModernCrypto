from tkinter.font import Font
from tkinter import Text as _Text, Misc, Canvas


class Text(_Text):
    FONT = "Inter 10"
    PLACEHOLDER_COLOR = "gray"

    def __init__(self, master: Misc, placeholder: str):
        _Text.__init__(self, master, font=self.FONT, relief="flat", highlightthickness=1,
                       highlightbackground="#cccccc", highlightcolor="#0078d7")
        self.placeholder = placeholder
        self.default_color = self.cget("fg")
        self._add_placeholder()

        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _add_placeholder(self, _=None):
        if not self.get(1.0, "end").strip():
            self.insert(1.0, self.placeholder)
            self.config(fg=self.PLACEHOLDER_COLOR)

    def _clear_placeholder(self, _=None):
        if self.get(1.0, "end").strip() == self.placeholder:
            self.delete(1.0, "end")
            self.config(fg=self.default_color)


class Button(Canvas):
    ENTERED_COLOR = "#e1e7f5"
    BACKGROUND_COLOR = "#f0f4fa"
    FOREGROUND_COLOR = "#2d4e90"
    BORDER_COLOR = "#a5b6da"
    FONT = "Inter 10"

    def __init__(self, master: Misc, text: str):
        width, height = self.metrics_text(text)
        Canvas.__init__(self, master, width=width, height=height, bg=self.BACKGROUND_COLOR, highlightthickness=1)

        self._highlighting = self.create_rounded_rectangle(0, 0, width, height, 10, fill=self.BACKGROUND_COLOR)
        self.tag_lower(self._highlighting)

        # self.bind("<Enter>", self.enter)
        # self.bind("<Leave>", self.leave)
        # self.bind("<Button-1>", command)

        self.create_text(0, 0, text=text, font=self.FONT, anchor="nw", fill=self.FOREGROUND_COLOR)

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

    @classmethod
    def metrics_text(cls, text: str) -> tuple[int, int]:
        """
        Считает длину и высоту текста основным шрифтом
        :return: длина и высота
        """

        font = Font(font=cls.FONT)
        return font.measure(text), font.metrics("linespace")
