import tkinter as tk
from obj import *
import time
import random


class Games:
    inter = tk.Tk()
    inter.title('Rapid Roll')
    inter.resizable(0, 0)
    canvas = tk.Canvas(inter, width=300, height=500)
    canvas.pack()

    def __init__(self):
        self.score = 0
        self.life = 6

        Games.canvas.create_rectangle(10, 50, 290, 480)
        for i in range(10, 290, 10):
            Games.canvas.create_polygon(i, 50, i + 5, 55, i + 10, 50)
            Games.canvas.create_polygon(i, 480, i + 5, 475, i + 10, 480)

        life = Lifes(self.canvas)
        life.move(10, 25)
        Games.canvas.create_text(50, 28, text='x %i' % self.life, font=('Times', 18))
        Games.canvas.create_text(250, 28, text='%07i' % self.score, font=('Times', 18))

        self.listPad = []
        self.listFen = []

        for y in range(100, 500, 50):
            num = random.randint(1, 4)
            x = random.randint(10, 240)
            if num == 1:
                self.listPad.append(Fences(Games.canvas, x, y).id)
            else:
                self.listFen.append(Paddles(Games.canvas, x, y).id)


if __name__ == '__main__':
    rapid = Games()
    rapid.inter.mainloop()
