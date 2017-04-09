import tkinter as tk
from obj import *

if __name__ == '__main__':
    inter = tk.Tk()
    inter.title('Rapid Roll')
    inter.resizable(0, 0)
    canvas = tk.Canvas(inter, width=300, height=500)
    canvas.pack()

    fen = Fences(canvas, 150, 50)
    pos = canvas.coords(fen.id)
    print(pos)

    inter.mainloop()
