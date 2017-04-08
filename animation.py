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
        ball.dropStraight()
        # canvas.bind_all('<KeyPress-Left>', ball.dropLeft)
        # canvas.bind_all('<Double-KeyPress-Left>', ball.dropLeft)
        # canvas.bind_all('<KeyPress-Right>', ball.dropRight)
        # canvas.bind_all('<Double-KeyPress-Right>', ball.dropRight)
        canvas.bind_all('<KeyPress-Left>', ball.moveLeft)
        canvas.bind_all('<KeyPress-Right>', ball.moveRight)

        time.sleep(0.01)

    inter.mainloop()
