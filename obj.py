import time


class Balls:
    def __init__(self, canvas, x=0, y=15, color='red'):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, x, y - 15)

    def dropStraight(self):
        self.canvas.move(self.id, 0, 1.5)

    def dropRight(self, event):
        for i in range(20):
            self.canvas.update()
            self.canvas.move(self.id, 2, 1)
            time.sleep(0.01)
        # self.canvas.move(self.id, 4, 1.5)

    def dropR(self, event):
        self.canvas.move(self.id, 4, 1.5)

    def dropLeft(self, event):
        for i in range(20):
            self.canvas.update()
            self.canvas.move(self.id, -2, 1)
            time.sleep(0.01)
        # self.canvas.move(self.id, -4, 1.5)

    def dropL(self, event):
        self.canvas.move(self.id, -4, 1.5)

    def moveLeft(self, event):
        self.canvas.move(self.id, -4, 0)

    def moveRight(self, event):
        self.canvas.move(self.id, 4, 0)


class Paddles:
    def __init__(self, canvas, x=0, y=8, color='blue'):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 50, 8, fill=color)
        self.canvas.move(self.id, x, y - 8)

    def moveUp(self):
        self.canvas.move(self.id, 0, -1)
        self.canvas.update()

    def hitTop(self):
        pos = self.canvas.coords(self.id)
        if pos[1] <= 50:
            return True
        return False


class Fences:
    def __init__(self, canvas, x=0, y=8, color='black'):
        self.canvas = canvas
        tmp = [0, 8, 5, 0, 10, 8, 15, 0, 20, 8, 25, 0, 30, 8]
        tmp.extend([35, 0, 40, 8, 45, 0, 50, 8])
        self.id = canvas.create_polygon(tmp, fill=color)
        self.canvas.move(self.id, x, y - 8)

    def moveUp(self):
        self.canvas.move(self.id, 0, -1)
        self.canvas.update()

    def hitTop(self):
        pos = self.canvas.coords(self.id)
        if pos[3] <= 50:
            return True
        return False


class Lifes:
    def __init__(self, canvas, color='green'):
        self.canvas = canvas
        self.id = canvas.create_polygon(8, 0, 16, 8, 8, 16, 0, 8, fill='green')

    def move(self, x, y):
        self.canvas.move(self.id, x, y - 8)
        self.canvas.update()
