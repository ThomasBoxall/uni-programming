from graphics import *

import random

# FUNCTIONS


def myCircle(win,centre,radius,colour):
    c = Circle(centre,radius)
    c.setFill(colour)
    c.draw(win)


def myRect(win, tlPoint, brPoint, colour):
    r = Rectangle(tlPoint,brPoint)
    r.setFill(colour)
    r.draw(win)

def myLine(win, tlPoint, brPoint, colour):
    l = Line(tlPoint, brPoint)
    l.setFill(colour)
    l.draw(win)

def myText(win, point, text):
    t = Text(point, text)
    t.draw(win)

def myPolygon(win, listOfPoints, colour):
    p = Polygon(listOfPoints)
    p.setFill(colour)
    p.draw(win)

def print10():
    print("-" * 10)

def getCol():
    cols = ["red", "orange", "blue", "green", "pink", "purple"]
    return cols[random.randint(0,len(cols)-1)]

def getPoint():
    return Point(random.randint(0, x), random.randint(0, y))


def menu():
    print10()
    print("-- MENU --")
    print10()
    print("Select an option")
    print("0 - close")
    print("1 - circle")
    print("2 - rect")
    print("3 - Line")
    print("4 - Text")
    print("5 - Polygon")
    print10()
    return int(input("please select an option: "))


# ENTRY POINT
def main():
    while True:
        selection = menu()
        if selection == 0:
            win.close()
            break
        elif selection == 1:
            # draw circle
            rad = random.randint(1, 300)
            myCircle(win, getPoint(), rad, getCol())
        elif selection == 2:
            # rectangle
            myRect(win, getPoint(), getPoint(), getCol())
            pass
        elif selection == 3:
            # line
            myLine(win, getPoint(), getPoint(), getCol())
        elif selection == 4:
            # text
            txt = input("enter text: ")
            myText(win, getPoint(), txt)
        elif selection == 5:
            pointList = []
            for i in range (0, random.randint(0,20)):
                pointList.append(getPoint())
            myPolygon(win, pointList, getCol())
        elif selection == 11:
            for i in range(0,10):
                myCircle(win, Point(i*50, 300), 50, "green")
        else:
            pass

# EXEC (ENTRY POINT)
x = 800
y = 800
win = GraphWin("Window", x, y)
main()

input()

