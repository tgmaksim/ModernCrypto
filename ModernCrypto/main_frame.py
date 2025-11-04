from tkinter import Frame, Misc


class MainFrame(Frame):
    BG_COLOR = "#e9edf5"

    def __init__(self, master: Misc):
        Frame.__init__(self, master, bg=self.BG_COLOR)
