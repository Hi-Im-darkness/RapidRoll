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
        self.scoreId = None
        self.life = 2
        self.lifeId = None

        Games.canvas.create_rectangle(10, 50, 290, 455)
        for i in range(10, 290, 10):
            Games.canvas.create_polygon(i, 50, i + 5, 55, i + 10, 50)

        life = Lifes(self.canvas)
        life.move(10, 25)

        self.updateScore()
        self.updateLife()

        self.listPad = []
        self.listFen = []

        for y in range(100, 500, 50):
            self.makeRandomPF(y)

    def updateScore(self):
        if self.scoreId is not None:
            Games.canvas.delete(self.scoreId)
        self.scoreId = Games.canvas.create_text(250, 28, text='%07i' % self.score, font=('Times', 18))

    def updateLife(self):
        if self.lifeId is not None:
            Games.canvas.delete(self.lifeId)
        self.lifeId = Games.canvas.create_text(50, 28, text='x %i' % self.life, font=('Times', 18))

    def refresh(self):
        for o in self.listFen + self.listPad:
            o.moveUp()
            if o.hitTop() is True:
                Games.canvas.delete(o.id)
                if o in self.listPad:
                    self.listPad.remove(o)
                else:
                    self.listFen.remove(o)
                self.makeRandomPF()

    def makeRandomPF(self, y=452):
        num = random.randint(1, 7)
        x = random.randint(10, 240)
        if num <= 2:
            self.listPad.append(Fences(Games.canvas, x, y))
        else:
            self.listFen.append(Paddles(Games.canvas, x, y))


if __name__ == '__main__':
    rapid = Games()

    while len(rapid.listPad + rapid.listFen) != 0:
        rapid.refresh()
        time.sleep(0.01)

    rapid.inter.mainloop()
