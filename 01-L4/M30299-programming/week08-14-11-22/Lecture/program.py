import utils
from graphics import *
from utils import *
import random

sqaures = []

def twoByTwo(xIn,yIn,c,d,col,win):
    for x in range (xIn,yIn,100):
        for y in range(c,d,100):
            tl = Point(x,y)
            br = Point(tl.x + 100, tl.y + 100)
            rectangle(win, tl, br, col)
            pause(win)

def twoByTwoArray(xIn,yIn,c,d,col):
    for x in range (xIn,yIn,100):
        for y in range(c,d,100):
            tl = Point(x,y)
            br = Point(tl.x + 100, tl.y + 100)
            rect = Rectangle(tl, br)
            rect.setFill(col)
            sqaures.append(rect)


def main():

    win = GraphWin("Test", 400, 400)
    win.getMouse()
    twoByTwo(0, 200, 0, 200, "blue", win)
    twoByTwo(200, 400, 0, 200, "red", win)
    twoByTwo(0,200, 200, 400, "orange", win)
    twoByTwo(200, 400, 200, 400, "purple", win)

    pause(win)

def randomImproved():
    win = GraphWin("Test", 400, 400)
    win.getMouse()
    twoByTwoArray(0, 200, 0, 200, "blue")
    twoByTwoArray(200, 400, 0, 200, "red")
    twoByTwoArray(0,200, 200, 400, "orange")
    twoByTwoArray(200, 400, 200, 400, "purple")
    
    while (len(sqaures) >0):
        rand = random.randint(0,len(sqaures) - 1)
        sqaures[rand].draw(win)
        sqaures.remove(sqaures[rand])
        pause(win)




# EXEC (ENTRY POINT)
#main()
randomImproved()
