import tkinter as tk
from obj import *
import time
import random

if __name__ == '__main__':
    inter = tk.Tk()
    inter.title('Rapid Roll')
    inter.resizable(0, 0)
    canvas = tk.Canvas(inter, width=300, height=500)
    canvas.pack()

    point = 0
    life = 6

    canvas.create_rectangle(10, 50, 290, 480)
    for i in range(10, 290, 10):
        canvas.create_polygon(i, 50, i + 5, 55, i + 10, 50)
        canvas.create_polygon(i, 480, i + 5, 475, i + 10, 480)

    life = Lifes(canvas)
    life.move(10, 25)
    canvas.create_text(55, 25, text='x 6', font=('Courier', 15))
    canvas.create_text(250, 25, text='0000000', font=('Courier', 15))

    padd = Paddles(canvas, 200, 150)
    ball = Balls(canvas, 218, 142)
    inter.mainloop()
