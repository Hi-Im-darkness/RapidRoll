class Balls:
    ''' Represent a ball which made by tkinter graphic

    Atrributes: canvas - tkinter canvas
                x, y - coord appear
                color - ball color
    '''

    def __init__(self, canvas, x=0, y=15, color='red'):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.x = 0
        self.canvas.move(self.id, x, y - 15)

    def drop(self):
        ''' ball drop'''
        self.canvas.move(self.id, 0, 1)
        self.canvas.update()

    def moveUp(self):
        ''' ball move up'''
        self.canvas.move(self.id, 0, -1)
        self.canvas.update()

    def move(self):
        ''' ball move left or right or static'''
        self.canvas.move(self.id, self.x, 0)

    def keyPressLeft(self, event):
        ''' when the KeyPress-Left, make ball move left'''
        self.x = -2

    def keyPressRight(self, event):
        ''' when the KeyPress-Right, make ball move right'''
        self.x = 2

    def keyRelease(self, event):
        ''' when the key release, make ball static'''
        self.x = 0

    def hitTopBot(self):
        ''' ball hit top or bot (isDie())'''
        ballPos = self.canvas.coords(self.id)
        if ballPos[1] <= 50 or ballPos[3] >= 455:
            return True
        return False

    def hitLeftSide(self):
        ''' ball hit left side'''
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 10:
            return True
        return False

    def hitRightSide(self):
        ''' ball hit right side'''
        ballPos = self.canvas.coords(self.id)
        if ballPos[2] >= 291:
            return True
        return False

    def hitPaddle(self, listPad):
        ''' ball hit paddle'''
        ballPos = self.canvas.coords(self.id)
        for pad in listPad:
            padPos = self.canvas.coords(pad.id)
            if ballPos[3] >= padPos[1] and ballPos[3] <= padPos[1] + 2:
                if ballPos[2] > padPos[0] and ballPos[0] < padPos[2]:
                    return True
        return False

    def hitFence(self, listFen):
        ''' ball hit fence'''
        ballPos = self.canvas.coords(self.id)
        for fen in listFen:
            fenPos = self.canvas.coords(fen.id)
            if ballPos[3] <= fenPos[1] and ballPos[3] >= fenPos[3]:
                if ballPos[2] > fenPos[0] and ballPos[0] < fenPos[20]:
                    return True
        return False

    def hitHeart(self, heartId):
        ''' ball hit heart'''
        ballPos = self.canvas.coords(self.id)
        heartPos = self.canvas.coords(heartId)
        if ballPos[2] >= heartPos[6] and ballPos[2] <= heartPos[2]:
            if ballPos[3] >= heartPos[1] and ballPos[3] <= heartPos[5]:
                return True

        if ballPos[0] >= heartPos[0] and ballPos[0] <= heartPos[2]:
            if ballPos[3] >= heartPos[1] and ballPos[3] <= heartPos[5]:
                return True

        return False


class Paddles:
    ''' Represent a paddle is made by tkinter graphic

    Atrributes: canvas - tkinter canvas
                x, y - coord appear
                color - ball color
    '''

    def __init__(self, canvas, x=0, y=8, color='blue'):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 50, 8, fill=color)
        self.canvas.move(self.id, x, y - 8)

    def moveUp(self):
        ''' paddle move up'''
        self.canvas.move(self.id, 0, -1)
        self.canvas.update()

    def hitTop(self):
        ''' paddle hit top'''
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
    def __init__(self, canvas, x=0, y=8, color='green'):
        self.canvas = canvas
        self.id = canvas.create_polygon(8, 0, 16, 8, 8, 16, 0, 8, fill='green')
        self.canvas.move(self.id, x, y - 8)

    def moveUp(self):
        self.canvas.move(self.id, 0, -1)
        self.canvas.update()

    def hitTop(self):
        pos = self.canvas.coords(self.id)
        if pos[1] <= 50:
            return True
        return False
