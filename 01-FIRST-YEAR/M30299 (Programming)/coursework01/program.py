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
def drawCirclePatch(win, colour, tl):
    """Draws single square then calls drawFourSmallCircles() to draw alternating colour circles in that rectangle"""
    patchSize = 100
    increment = 20
    altFlag = True
    for y in range(int(tl.getY()), int(tl.getY())+patchSize, increment):
        for x in range(int(tl.getX()), int(tl.getX())+patchSize, increment):
            currentTopLeft = Point(x, y)
            if altFlag:
                rectangle(win, currentTopLeft, brPoint(currentTopLeft, increment, increment), colour)
            else:
                rectangle(win, currentTopLeft, brPoint(currentTopLeft, increment, increment), "white")

            drawFourSmallCircles(win, colour, currentTopLeft, altFlag)
            altFlag = not altFlag

def drawFourSmallCircles(win, colour, tl, altFlag):
    """Draws four little circles in a 20x20 space, based from TopLeft (tl) point of specified colour"""
    # all circles have radius 5
    for y in range(int(tl.getY()), int(tl.getY()+20), 10):
        for x in range(int(tl.getX()), int(tl.getX()+20), 10):
            currentTopLeft = Point(x, y)
            if altFlag:
                circlefromTL(win, currentTopLeft, 5, "white")
            else:
                circlefromTL(win, currentTopLeft, 5, colour)


def drawLinePatch(win, colour, tl):
    """Draw a single 'line' patch with TopLeft point tl"""
    # we add 100 as this moves to the other side of the patch
    # we add 10 as this is the gap between the lines
    for offset in range(0, 100,10):
        # define start and end points for line separately to make call to line() method simpler
        startOne = Point(offset + tl.getX(), tl.getY())
        endOne = Point(tl.getX()+100, offset + tl.getY() + 10)
        line(win, startOne, endOne, colour)

        startTwo = Point(tl.getX(), tl.getY()+offset)
        endTwo = Point(offset + tl.getX() + 10, tl.getY()+100)
        line(win, startTwo, endTwo, colour)

def drawPlainPatch(win, colour, tl):
    """Draw a plain patch of colours[0]"""
    rectangle(win, tl, brPoint(tl, 100, 100), colour)


def populateWindow(win, colours, dimension):
    for y in range(0,dimension,100):
        for x in range(0,dimension,100):
            topLeft = Point(x,y)
            if x >= 100 and y >= 100 and x<dimension-100 and y<dimension-100:
                #we actually need to draw a patch now
                if x == y or x+y == dimension - 100:
                    drawLinePatch(win, getColours(colours, topLeft, dimension), topLeft)
                else:
                    drawCirclePatch(win, getColours(colours, topLeft, dimension), topLeft)
            else:
                drawPlainPatch(win, getColours(colours, topLeft, dimension), topLeft)

def getColours(colours, tl, dimension):
    x = tl.getX()
    y = tl.getY()
    if x == y or x+y == dimension - 100:
        return colours[0]
    elif x>y and y+x < dimension:
        return colours[1]
    elif x>y and x+y >= dimension:
        return colours[2]
    elif x<y and x+y >= dimension:
        return colours[1]
    else:
        return colours[2]


def main():
    dimension = 500
    win = GraphWin("", dimension, dimension)
    colours = ["blue", "orange", "red"]
    #drawLinePatchworkEvenMoreDifferent(win, colours, Point(10,10))
    populateWindow(win, colours, dimension)
    win.getMouse()


main()

# IMPROVEMENTS FROM SPEAKING TO MANI
# use literals in the code rather than a var where there is no chance of changing
# refactor little circles out of the main function for circlePatch
# better iteration of for loops
# better var names