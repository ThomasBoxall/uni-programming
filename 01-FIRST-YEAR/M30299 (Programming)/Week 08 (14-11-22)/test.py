from graphics import *

def circle(win, centre, rad, fill, outline):
    c = Circle(centre, rad)
    c.setFill(fill)
    c.setOutline(outline)
    c.draw(win)

def drawCircles():
    win = GraphWin("Circles", 600, 600)
    for i in range(0,15,1):
        mousePos = win.getMouse()
        x = mousePos.getX()
        y = mousePos.getY()
        if x < 300 and  y <300:
            circle(win, mousePos, 30, "", "blue")
        elif x >300 and y < 300:
            circle(win, mousePos, 30, "blue", "black")
        elif x < 300 and y> 300:
            circle(win, mousePos, 30, "", "pink")
        elif x > 300 and y > 300:
            circle(win, mousePos, 30, "pink", "black")

    win.getMouse()

def drawCircles2():
    win = GraphWin("Circles 2", 600, 600)
    for j in range(450, 630, 60):
        for i in range (30, 630, 60):
            mousePos = win.getMouse()
            x = mousePos.getX()
            y = mousePos.getY()
            centre = Point(i, j)
            if x < 300 and  y <300:
                circle(win, centre, 30, "", "blue")
            elif x >300 and y < 300:
                circle(win, centre, 30, "blue", "black")
            elif x < 300 and y> 300:
                circle(win, centre, 30, "", "pink")
            elif x > 300 and y > 300:
                circle(win, centre, 30, "pink", "black")

    win.getMouse()
drawCircles()
#drawCircles2()
