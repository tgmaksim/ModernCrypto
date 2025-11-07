from tkinter import Frame, Misc
from aes import AESFrame


class MainFrame(Frame):
    def __init__(self, master: Misc):
        Frame.__init__(self, master)
        self.frames: list[Frame] = []
        self.frames.append(AESFrame(self))
        self.frames[0].place(relwidth=1, relheight=1)
