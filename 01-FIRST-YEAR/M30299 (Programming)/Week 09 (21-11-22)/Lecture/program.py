from graphics import *
from patches import *
import math


def main():
    screenSize = 500
    win = GraphWin("Test", screenSize, screenSize)
    colours = ["blue", "green", "orange", "white"]
    alternateFlag = True

    #STEP 1
    tlPoint = Point(0,0)
    patch1(win, colours, tlPoint)
    #patch2(win, colours, tlPoint)

    #STEP 2
    # for i in range(4):
    #     tlPoint = win.getMouse()
    #     patch1(win, colours, tlPoint)
    #     tlPoint = win.getMouse()
    #     patch2(win, colours, tlPoint)

    #STEP 3
    # for y in range(0, screenSize, 100):
    #     for x in range(0, screenSize, 100):
    #         tlPoint = Point(x, y)
    #         if alternateFlag:  #if y  == 0 or x == 0   #or x == 400 or y == 400:
    #             patch2(win,colours,tlPoint)
    #         else:
    #             patch1(win,colours,tlPoint)
    #         alternateFlag = not alternateFlag
    win.getMouse()

main()