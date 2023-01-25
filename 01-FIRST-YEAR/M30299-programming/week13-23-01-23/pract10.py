from graphics import *
import time


class MyPoint():
    """
    A class to represent a point in on the graphics window.
    A point has an `x` and `y` coordinate and can be moved
    or drawn on the graphics window.    
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        """
        Returns the value of the instance variable `x`.
        """
        return self.x

    def getY(self):
        """
        Returns the value of the instance variable `y`.
        """
        return self.y

    def move(self, dx, dy):
        """
        Moves the point by `dx` units in the x direction
        and `dy` units in the y direction.
        """
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        output = "MyPoint({0}, {1})".format(self.x, self.y)
        return output

    def draw(self, win):
        """
        Draws the point on a given graphics window `win`.
        """
        point = Point(self.x, self.y)
        point.draw(win)


class Square():
    """
    A class to represent a square on the graphics window.
    A square has a top left point, a side length.
    Also a fill colour which is black by default.
    A square can be moved, drawn and filled with a colour.
    """

    def __init__(self, topLeftPoint, sideLength):
        self.fillColour = "black"
        self.outlineColour = "black"
        self.p1 = topLeftPoint
        self.side = sideLength
        p2x = self.p1.getX() + sideLength
        p2y = self.p1.getY() + sideLength
        self.p2 = MyPoint(p2x, p2y)

    def getSide(self):
        """
        Returns the value of the instance variable `side`.
        """
        return self.side

    def getP1(self):
        """
        Returns the value of the top left point (instance variable `p1`)
        """
        return self.p1

    def getP2(self):
        """
        Returns the value of the bottom right point (instance variable `p2`)
        """
        return self.p2

    def move(self, dx, dy):
        """
        Moves the square by `dx` units in the x direction
        and `dy` units in the y direction.
        """
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        output = "Square({0}, {1})".format(self.p1, self.side)
        return output

    def setFill(self, colour):
        """
        Sets the fill colour of the square to `colour`.
        """
        self.fillColour = colour
    
    def setOutline(self, colour):
        """
        Sets the outline colour of the square to 'colour'
        """
        self.outlineColour = colour

    def draw(self, win):
        """
        Draws the square on a given graphics window `win`.
        It also fills the square with the fill colour.
        """
        p1 = Point(self.p1.getX(), self.p1.getY())
        p2 = Point(self.p2.getX(), self.p2.getY())
        square = Rectangle(p1, p2)
        square.setFill(self.fillColour)
        square.setOutline(self.outlineColour)
        square.draw(win)
    
    def getCenter(self):
        """
        Returns the centre point of the square
        """
        cx = self.p1.getX() + (self.side/2)
        cy = self.p1.getY() + (self.side/2)
        return MyPoint(cx, cy)

class MyCircle():
    def __init__(self, cp, r):
        self.centre = cp
        self.radius = r
        self.outlineColour = "black"
        self.fillColour = "black"
    
    def draw(self, win):
        c = Circle(self.centre, self.radius)
        c.setOutline(self.outlineColour)
        c.setFill(self.fillColour)
        c.draw(win)
    
    def getCenter(self):
        return self.centre
    
    def getRadius(self):
        return self.radius
    
    def move(self, dx, dy):
        self.centre.move(dx, dy)
    
class StickFigure():
    def __init__(self, cHead):
        self.cx = cHead.getX()
        self.cy = cHead.getY()
        self.centreHead = cHead
        self.head = Circle(self.centreHead, 20)
        self.body = Line(Point(self.cx, self.cy+20), Point(self.cx, self.cy+60))
        self.arms = Line(Point(self.cx - 30, self.cy+30), Point(self.cx+30, self.cy+30))
        self.leftLeg = Line(Point(self.cx, self.cy+60), Point(self.cx-20, self.cy+110))
        self.rightLeg = Line(Point(self.cx, self.cy + 60), Point(self.cx + 20, self.cy+110))
        self.colour = "black"
        self.setColour(self.colour)
    
    def draw(self, win):
        self.head.draw(win)
        self.body.draw(win)
        self.arms.draw(win)
        self.rightLeg.draw(win)
        self.leftLeg.draw(win)
    
    def setColour(self, colour):
        self.head.setFill(colour)
        self.head.setOutline(colour)
        self.body.setFill(colour)
        self.arms.setFill(colour)
        self.rightLeg.setFill(colour)
        self.leftLeg.setFill(colour)

class DigitalClock():
    def __init__(self, tl, currTime, size):
        self.size = size
        self.topLeft = tl
        x = self.topLeft.getX()
        y = self.topLeft.getY()
        self.time = currTime
        self.background = Rectangle(self.topLeft, Point(x+100*self.size, y+50*self.size))
        self.background.setFill("orange")
        self.background.setOutline("orange")
        self.inner = Rectangle(Point(x+10*self.size, y+10*self.size), Point(x+90*self.size, y+40*self.size))
        self.inner.setFill("white")
        self.inner.setOutline("white")
        self.timeText = Text(Point(x+50*self.size, y+25*self.size), self.time.strftime("%H:%M:%S"))
        txtSize = 36 if 12*self.size>36 else 12*self.size
        self.timeText.setSize(txtSize)
        self.timeText.setFace("courier")
        self.timeText.setStyle("bold")
    
    def draw(self, win):
        self.background.draw(win)
        self.inner.draw(win)
        self.timeText.draw(win)
    
    def update(self, currTime):
        self.time = currTime
        self.timeText.setText(self.time.strftime("%H:%M:%S"))
        

def testSquare():
    """
    Tests the `Square` class we have created.
    """
    win = GraphWin()
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)
    print(square.getSide())  # 50
    print(square.getP1())  # MyPoint(100, 50)
    print(square.getP2())  # MyPoint(150, 100)
    # Moves the square by 10 units in the x and 20 units in the y direction.
    square.move(10, 20)
    print(square.getP1())  # MyPoint(110, 70)
    print(square.getP2())  # MyPoint(160, 120)
    print(square)  # Square(MyPoint(100, 50), 50)
    square.setFill("red")
    square.draw(win)
    print(square.getCenter())
    win.mainloop()


def testPoint():
    """
    Tests the `Point` class from the graphics module.
    """
    win = GraphWin()
    point = Point(100, 50)
    print(point.getX())  # 100.0
    print(point.getY())  # 50.0
    # Moves the point by 10 units in the x and 20 units in the y direction.
    point.move(10, 20)
    print(point.getX())  # 110.0
    print(point.getY())  # 70.0
    print(point)  # Point(100.0, 50.0)
    point.draw(win)
    print(type(point))
    win.mainloop()


def testMyPoint():
    """
    Tests the `MyPoint` class we have created.
    """
    win = GraphWin()
    myPoint = MyPoint(100, 50)
    print(myPoint.getX())  # 100
    print(myPoint.getY())  # 50
    # Moves the point by 10 units in the x and 20 units in the y direction.
    myPoint.move(10, 20)
    print(myPoint.getX())  # 110
    print(myPoint.getY())  # 70
    print(myPoint)  # MyPoint(110, 70)
    myPoint.draw(win)
    win.mainloop()

def testOutline():
    win = GraphWin()
    mySquare = Square(Point(10,10), 5)
    mySquare.draw(win)
    win.getMouse()

def testMutateOutline():
    win = GraphWin()
    mySquare = Square(Point(10,10), 50)
    mySquare.draw(win)
    win.getMouse()
    mySquare.setOutline("orange")
    win.getMouse()

def testCircle():
    win = GraphWin()
    circle = MyCircle(MyPoint(100, 50), 50)
    print(circle.getCenter()) # MyPoint(100, 50)
    print(circle.getRadius()) # 50
    circle.move(10, 20)
    print(circle.getCenter()) # MyPoint(110, 70)
    print(circle) # MyCircle(MyPoint(100, 50), 50)
    circle.draw(win) # Optional!
    win.getMouse()

def stickFigureTest():
    win = GraphWin()
    sf = StickFigure(Point(50, 50))
    sf.draw(win)
    sf.setColour("red")
    win.getMouse()

def testClock():
    clock = DigitalClock(Point(50,50), time, 5)
    win = GraphWin("Big Clock", 600, 400)
    clock.draw(win)
    while True:
        time.sleep(1)
        clock.update(time)

#testOutline()
#testMutateOutline()
# testSquare()
# testCircle()
# stickFigureTest()
testClock()