# create window of 800x800. user clicks in tl, draw purple circle. user clicks in tr, draw red circle. user clicks in bl, draw black circle. user clicks in br, draw black outline circle. 
from graphics import *

def drawCircle(win, col, out, cent, rad):
    c = Circle(cent, rad)
    c.draw(win)
    c.setFill(col)
    c.setOutline(out)

def stepOne():
    win = GraphWin("Circle Fun!", 800, 800)
    radius = 10
    for i in range(0,10):
        mousePos = win.getMouse()
        mousePosX = mousePos.getX()
        mousePosY = mousePos.getY()
        if (mousePosX <= 400 and mousePosY <= 400):
            drawCircle(win, "purple", "purple", mousePos, radius)
        elif (mousePosX >400 and mousePosY <=400):
            drawCircle(win, "red", "red", mousePos, radius)
        elif (mousePosX <= 400 and mousePosY > 400):
            drawCircle(win, "black", "black", mousePos, radius)
        elif (mousePosX > 400 and mousePosY>400):
            drawCircle(win, "", "black", mousePos, radius)
    win.getMouse()

def stepTwo():
    win = GraphWin("Further Circle Fun", 800, 800)
    radius = 50
    for y in range(350, 550, 100):
        for x in range(250,650, 100):
            win.getMouse()
            if (x <= 400 and y <= 400):
                circlePos = Point(x,y)
                drawCircle(win, "purple", "purple", circlePos, radius)
            elif (x >400 and y <=400):
                circlePos = Point(x,y)
                drawCircle(win, "red", "red", circlePos, radius)
            elif (x <= 400 and y > 400):
                circlePos = Point(x,y)
                drawCircle(win, "black", "black", circlePos, radius)
            elif (x > 400 and y>400):
                circlePos = Point(x,y)
                drawCircle(win, "", "black", circlePos, radius)
    win.getMouse()


stepOne()
#stepTwo()