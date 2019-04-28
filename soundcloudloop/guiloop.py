from tkinter import *
from threading import Thread
from scloop import SCLOOP
class Gui:
    def __init__(self, master):
        self.track_name = Label(text="INSERT THE TRACK LINK: ")
        self.track_name_field = Entry(width=100)
        self.track_name_button = Button(text="START!")
        self.lay_out()
        self.binding()
    def lay_out(self):
        self.track_name.grid(row=0, column=0)
        self.track_name_field.grid(row=0, column=1)
        self.track_name_button.grid(row=1, columnspan=2)
    def binding(self):
        self.track_name_button.bind("<Button-1>", self.start_track)
    def start_track(self, master):
        Thread(target=self.start_track_2, args="").start()
    def start_track_2(self):
        S = SCLOOP(str(self.track_name_field.get()))
        S.loopsong()
if __name__ == '__main__':
    window = Tk()
    G = Gui(window)
    window.mainloop()