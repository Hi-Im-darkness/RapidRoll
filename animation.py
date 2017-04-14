import tkinter as tk
from obj import *
import time


if __name__ == '__main__':
    inter = tk.Tk()
    inter.title('Rapid Roll')
    inter.resizable(0, 0)
    canvas = tk.Canvas(inter, width=300, height=500)
    canvas.pack()

    ball = Balls(canvas, 140, 80)

    while True:
        canvas.update()
        ball.drop()
        ball.move()
        canvas.bind_all('<KeyPress-Left>', ball.keyPressLeft)
        canvas.bind_all('<KeyPress-Right>', ball.keyPressRight)
        canvas.bind_all('<KeyRelease>', ball.keyRelease)
        time.sleep(0.01)
    # canvas.bind_all('<KeyRelease-Left>', ball.moveLeft)
    # canvas.bind_all('<KeyRelease-Right>', ball.moveRight)
    # canvas.bind_all('<Double-KeyRelease-Left>', ball.moveLeft)
    # canvas.bind_all('<Double-KeyRelease-Right>', ball.moveRight)

    inter.mainloop()
