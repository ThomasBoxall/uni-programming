# ITEM 3 COURSEWORK
from graphics import *

# HELPER FUNCTIONS
def centrePoint(tlPoint, radius):
    """Returns centre point of circle based on top left coordinate and radius of circle"""
    x = tlPoint.getX() + radius
    y = tlPoint.getY() + radius
    centre = Point(x, y)
    return centre

def text(win, tlPoint, text, colour):
    """Draws text object on screen and returns text object"""
    p = centrePoint(tlPoint,5)
    t = Text(p, text)
    t.setOutline(colour)
    t.draw(win)
    return t

def circle(win, centre, radius, colour):
    """Draws circle on screen and returns circle object"""
    c = Circle(centre, radius)
    c.setFill(colour)
    c.draw(win)
    c.setOutline(colour)
    return c

def rectangle(win, tlPoint, brPoint, colour):
    """Draws rectangle on screen and returns rectangle object"""
    r = Rectangle(tlPoint, brPoint)
    r.setFill(colour)
    r.draw(win)
    r.setOutline(colour)
    return r


def line(win, point1, point2, colour):
    """Draws line on screen and returns line object"""
    l = Line(point1, point2)
    l.setOutline(colour)
    l.draw(win)
    return l

def brPoint(tlPoint, width, height):
    """Calculates a bottom right Point based on the Top Left point, width and height. Returns bottom right point object"""
    x = tlPoint.getX() + width
    y = tlPoint.getY() + height
    brPoint = Point(x, y)
    return brPoint

def circlefromTL(win, tlPoint, radius, colour):
    """Draws a circle based on the top left coordinates"""
    centre = centrePoint(tlPoint, radius)
    circle(win, centre, radius, colour)

# DRAW SINGLE PATCH FUNCTIONS
def circlePatch(win, colours, tl):
    patchSize = 100
    increment = 20
    altFlag = True
    for y in range(int(tl.getY()), int(tl.getY())+patchSize, increment):
        for x in range(int(tl.getX()), int(tl.getX())+patchSize, increment):
            currentTopLeft = Point(x, y)
            innerIncrement = 10
            innerPatchSize = 20
            radius = 5
            if altFlag:
                rectangle(win, currentTopLeft, brPoint(currentTopLeft, increment, increment), colours[0])
            else:
                rectangle(win, currentTopLeft, brPoint(currentTopLeft, increment, increment), colours[1])
            for i in range(int(currentTopLeft.getY()), int(currentTopLeft.getY()+innerPatchSize), innerIncrement):
                for j in range(int(currentTopLeft.getX()), int(currentTopLeft.getX()+innerPatchSize), innerIncrement):
                    innerCurrentTopLeft = Point(j, i)
                    if altFlag:
                        circlefromTL(win, innerCurrentTopLeft, radius, colours[1])
                    else:
                        circlefromTL(win, innerCurrentTopLeft, radius, colours[0])                        
            altFlag = not altFlag

def linePatch(win, colours, tl):
    patchSize = 100
    increment = 10
    for y in range(int(tl.getY()), int(tl.getY())+patchSize, increment):
        drawOne = True
        for x in range(int(tl.getY()), int(tl.getY())+patchSize, increment):
            # startOne = Point(x, tl.getY())
            # startTwo = Point(tl.getX(), y)
            # endOne = Point(x+increment, y)
            # endTwo = Point(x, y+ increment)
            startOne = Point(x, tl.getY())
            startTwo = Point(tl.getX(), y)
            endOne = Point(tl.getX()+patchSize, y+increment)
            endTwo = Point(x, y+ increment)
            line(win, startOne, endOne, colours[0])
            #line(win, startTwo, endTwo, colours[0])
            win.getMouse()

def drawLinePatchDifferent(win, colours, tl):
    patchSize = 100
    increment = 10
    for i in range(1,11,1):
        startOne = Point(int(tl.getX())*i, tl.getY())
        endOne = Point(tl.getX()+patchSize, tl.getY()*i+increment)
        line(win, startOne, endOne, colours[0])
        startTwo = Point(tl.getX(), int(tl.getY())*i)
        endTwo = Point(tl.getX()*i+increment, tl.getY()+patchSize)
        line(win, startTwo, endTwo, colours[0])
        win.getMouse()

def drawLinePatchworkEvenMoreDifferent(win, colours, tl):
    patchSize = 100
    increment = 10
    for i in range(0, 10, 1):
        startOne = Point(i*increment + tl.getX(), tl.getY())
        endOne = Point(tl.getX()+patchSize, i*increment + tl.getY() + increment)
        line(win, startOne, endOne, colours[0])

        startTwo = Point(tl.getX(), tl.getY()+(i*increment))
        endTwo = Point(i*increment + tl.getX() + increment, tl.getY()+patchSize)
        line(win, startTwo, endTwo, colours[0])


def main():
    win = GraphWin("", 400, 400)
    colours = ["red", "white"]
    #drawLinePatchworkEvenMoreDifferent(win, colours, Point(10,10))
    for i in range(0,4,1):
        drawLinePatchworkEvenMoreDifferent(win, colours, win.getMouse())
    win.getMouse()


main()