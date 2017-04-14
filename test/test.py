from tkinter import *

x = 10
y = 10
a = 100
b = 100
direction = None


def drop():
    window.move(rect, 0, 1)


def move():
    global x_vel
    global y_vel
    global direction
    if direction is not None:
        canvas1.move(rect, x_vel, y_vel)
    window.after(33, move)


def on_keypress(event):
    global direction
    global x_vel
    global y_vel
    direction, x_vel, y_vel = dir_vel[event.keysym]


def on_keyrelease(event):
    global direction
    direction = None


dir_vel = {
    "Left": ("left", -5, 0),
    "Right": ('right', 5, 0),
    "Down": ('down', 0, 5),
    "Up": ('up', 0, -5)}


window = Tk()
window.geometry("400x200")

move()

# canvas and drawing
canvas1 = Canvas(window, height=200, width=400)
canvas1.grid(row=0, column=0, sticky=W)
coord = [x, y, a, b]
rect = canvas1.create_rectangle(*coord, outline="#fb0", fill="#fb0")

while True:
    # drop()
    # capturing keyboard inputs and assigning to function
    window.bind_all('<KeyPress>', on_keypress)
    window.bind_all('<KeyRelease>', on_keyrelease)
window.mainloop()
