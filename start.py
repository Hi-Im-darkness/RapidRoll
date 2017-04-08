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
    canvas.create_text(50, 28, text='x 6', font=('Times', 15))
    canvas.create_text(250, 25, text='0000000', font=('Courier', 15))

    padd = Paddles(canvas, 150, 150)
    ball = Balls(canvas, 168, 142)
    listId = [padd.id]

    for y in range(200, 500, 50):
        num = random.randint(1, 4)
        x = random.randint(10, 240)
        if num == 1:
            fen = Fences(canvas, x, y)
            listId.append(fen.id)
        else:
            pad = Paddles(canvas, x, y)
            listId.append(pad.id)

    while True:
        canvas.update()
        # ball.dropStraight()
        canvas.bind_all('<KeyPress-Left>', ball.dropLeft)
        # canvas.bind_all('<Double-KeyPress-Left>', ball.dropLeft)
        canvas.bind_all('<KeyPress-Right>', ball.dropRight)
        # canvas.bind_all('<Double-KeyPress-Right>', ball.dropRight)
        # canvas.bind_all('<KeyPress-Left>', ball.moveLeft)
        # canvas.bind_all('<KeyPress-Right>', ball.moveRight)

        time.sleep(0.01)
    inter.mainloop()
