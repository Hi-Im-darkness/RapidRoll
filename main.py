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
        self.score = 0  # score of you
        self.scoreId = None  # id of score object
        self.life = 2  # life of you
        self.lifeId = None  # id of life object
        self.heart = None  # id of heart object

        Games.canvas.create_rectangle(10, 50, 291, 455)  # creat frame
        for i in range(10, 290, 10):  # creat fence in top and bot of frame
            Games.canvas.create_polygon(i, 50, i + 5, 55, i + 10, 50)
            Games.canvas.create_polygon(i, 455, i + 5, 450, i + 10, 455)

        Lifes(self.canvas, 10, 25)

        self.updateScore()
        self.updateLife()

        self.listPad = []
        self.listFen = []

        for y in range(100, 500, 50):
            self.addRandomPF(y)

        self.ball = None
        self.addBall()

    def drawPF(self):
        ''' make fence and paddle move up '''

        for o in self.listFen + self.listPad:
            o.moveUp()
            if o.hitTop() is True:  # when padd or fen hit top, delete it
                Games.canvas.delete(o.id)
                if o in self.listPad:
                    self.listPad.remove(o)
                else:
                    self.listFen.remove(o)
                self.addRandomPF()  # add new padd or fen at bottom of canvas
            Games.canvas.update()

    def play(self):
        '''make the game running'''

        self.drawPF()

        # make ball move left and right
        self.ball.move()  # make ball move left or right or static
        if self.ball.hitLeftSide():  # ball hit left side
            Games.canvas.unbind_all('<KeyPress-Left>')  # dont bind KeyPressLeft
            self.ball.x = 0  # static ball
        elif self.ball.hitRightSide():
            Games.canvas.unbind_all('<KeyPress-Right>')
            self.ball.x = 0
        else:
            Games.canvas.bind_all('<KeyPress-Left>', self.ball.keyPressLeft)
            Games.canvas.bind_all('<KeyPress-Right>', self.ball.keyPressRight)
            Games.canvas.bind_all('<KeyRelease>', self.ball.keyRelease)

        # check whether ball hit paddle
        if self.ball.hitPaddle(self.listPad) is False:
            self.score += 1
            self.ball.drop()
        else:
            self.ball.moveUp()
        self.updateScore()

        # check whether you die
        if self.isDie():
            time.sleep(0.5)
            self.addBall()
            self.life -= 1
            self.updateLife()

        # add heart in game when score equal 800*x
        if self.score % 800 == 0 and self.score != 0:
            self.addLife()

        if self.heart is not None:
            self.heart.moveUp()
            if self.heart.hitTop():  # heart hit top
                Games.canvas.delete(self.heart.id)
                self.heart = None

        if self.heart is not None:
            if self.ball.hitHeart(self.heart.id):  # you get 1 heart
                if self.life != 6:
                    self.life += 1
                    self.updateLife()
                Games.canvas.delete(self.heart.id)
                self.heart = None

    def isDie(self):
        '''check whether you die (lost a life)'''
        if self.ball.hitTopBot():
            return True
        if self.ball.hitFence(self.listFen):
            return True
        return False

    def stop(self):
        '''check whether game stop'''
        if self.life < 0:
            return True
        return False

    def addLife(self):
        ''' add a life in last paddle'''
        if self.heart is not None:
            Games.canvas.delete(self.heart.id)

        padPos = Games.canvas.coords(self.listPad[-1].id)
        self.heart = Lifes(Games.canvas, padPos[0] + 18, padPos[3] - 15)

    def addRandomPF(self, y=452):
        '''add fence and paddle'''
        num = random.randint(1, 7)
        x = random.choice(range(10, 240, 2))
        if num <= 2:
            self.listFen.append(Fences(Games.canvas, x, y))
        else:
            self.listPad.append(Paddles(Games.canvas, x, y))

    def addBall(self):
        '''add a ball in last paddle'''
        if self.ball is not None:
            Games.canvas.delete(self.ball.id)

        padPos = Games.canvas.coords(self.listPad[-1].id)
        self.ball = Balls(Games.canvas, padPos[0] + 18, padPos[3] - 8)

    def updateScore(self):
        '''update score'''
        if self.scoreId is not None:
            Games.canvas.delete(self.scoreId)
        self.scoreId = Games.canvas.create_text(250, 28, text='%07i' % self.score, font=('Times', 18))

    def updateLife(self):
        '''update life'''
        if self.lifeId is not None:
            Games.canvas.delete(self.lifeId)
        self.lifeId = Games.canvas.create_text(50, 28, text='x %i' % self.life, font=('Times', 18))


def main():
    game = Games()

    while True:
        game.play()
        if game.stop():
            return
        time.sleep(0.004)

    game.inter.mainloop()


if __name__ == '__main__':
    main()
