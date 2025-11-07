from ui import Text, Button
from tkinter import Frame, Misc, Label


class AESFrame(Frame):
    BG_COLOR = "#e9edf5"
    FONT = "Inter 10 bold"

    def __init__(self, master: Misc):
        Frame.__init__(self, master, bg=self.BG_COLOR)

        self.label_text = Label(self, text="Введите текст или выберите файл", bg=self.BG_COLOR, font=self.FONT)
        self.label_text.place(x=20, y=20)

        self.text = Text(self, "Введите текст")
        self.text.place(x=23, y=50, relwidth=0.8, height=80)

        self.button_input_file = Button(self, "Выбрать файл")
        self.button_input_file.place(x=20, y=150)
