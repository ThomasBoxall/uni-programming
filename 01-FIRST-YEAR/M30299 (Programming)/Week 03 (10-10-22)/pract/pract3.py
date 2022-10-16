# Practical Worksheet P3: Graphical Programming
# your name, your number

from graphics import *
import math


def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    leftLeg = Line(Point(100,120), Point(80,140))
    leftLeg.draw(win)
    rightLeg = Line(Point(100,120), Point(120,140))
    rightLeg.draw(win)
    leftArm = Line(Point(100,100), Point(80,100))
    leftArm.draw(win)
    rightArm = Line(Point(100,100), Point(120,100))
    rightArm.draw(win)

    input()


def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100,100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")

# wk03,ex02 userinputs radius of circle to terminal, the output a circle with that radius to gui
def drawCircle():
    radius = int(input("Please enter the radius here: "))
    size = (radius * 2) + 30
    win = GraphWin("Circle", size, size)
    centre = Point(win.getHeight()/2, win.getWidth()/2)
    circle = Circle(centre, radius)
    circle.draw(win)

    input()

# wk03, ex03 draw archery target (3x concentric circle, each diff colour.)
def drawArcheryTarget():
    win = GraphWin("Archery Target", 400,400)
    centre = Point(win.getHeight()/2, win.getWidth()/2)
    circle1 = Circle(centre, 150)
    circle1.draw(win)
    circle1.setFill("blue")
    circle2 = Circle(centre, 100)
    circle2.draw(win)
    circle2.setFill("red")
    circle3 = Circle(centre, 50)
    circle3.draw(win)
    circle3.setFill("yellow")
    input()
  
# wk03, ex04 use input height and width of rectangle. draw in gui (200x200,assume user enters values less than this), draw rectangle with user values in centre of screen.
def drawRectangle():
    width = int(input("Enter width:"))
    height = int(input("Enter height: "))
    win = GraphWin("Rectangle Box", 200, 200)
    topLeft = Point((100-width/2), (100-height/2))
    bottomRight = Point((100+width/2), (100+height/2))
    rectangle = Rectangle(topLeft, bottomRight)
    rectangle.draw(win)
    input()

# wk03, ex05 user clicks in gui somewhere. draw a blue circle with radius 50 wherever they click
def blueCircle():
    win = GraphWin("Click for Circle", 200,200)
    mousePos = win.getMouse()
    circle = Circle(mousePos, 50)
    circle.draw(win)
    circle.setFill("blue")
    input()


# wk03, ex06 pt1 user clicks two points, draw line between them
def drawLine():
    win = GraphWin("Line box", 400, 400)
    lineStart = win.getMouse()
    lineEnd = win.getMouse()
    line = Line(lineStart, lineEnd)
    line.draw(win)
    input()

# wk03, ex06 pt2 user can draw 10 lines by clicking their start and end point
def tenLines():
    win = GraphWin("Ten line box", 500, 500)
    for x in range(0,10):
        lineStart = win.getMouse()
        lineEnd = win.getMouse()
        line = Line(lineStart, lineEnd)
        line.draw(win)
    input()

# wk03, ex07 user enters string into input box then click on screen to place it. repeat 10 times.
def tenStrings():
    win = GraphWin("String box", 600,600)
    inputBox = Entry(Point(100,100),20)
    inputBox.draw(win)
    for x in range(0,10):
        mousePos = win.getMouse()
        message = Text(mousePos, inputBox.getText())
        # TO BE CONTINUED HERE
        messageOnDisplay = Text(mousePos, message)
        messageOnDisplay.setText(inputBox.getText())
        messageOnDisplay.draw(win)

# wk03, ex08 user clicks top left bottom right corner of rectangle after entering colour of rect into text box
def tenColouredRectangles():
    win = GraphWin("Rectangle Box", 1000,1000)
    inputBox = Entry(Point(100,100),20)
    inputBox.draw(win)
    for x in range (0,10):
        mouse1 = win.getMouse()
        mouse2 = win.getMouse()
        rect = Rectangle(mouse1, mouse2)
        rect.draw(win)
        rect.setFill(inputBox.getText())

# wk03, wx09 user clicks five times to draw stick man
def fiveClickStickFigure():
    win = GraphWin("Five Click Stick Figure",600,600)
    point1 = win.getMouse()
    point2 = win.getMouse()
    faceRad = math.sqrt(((point2.getX() - point1.getX())**2) + ((point2.getY() - point1.getY())**2))
    face = Circle(point1, faceRad)
    face.draw(win)
    point3 = win.getMouse()
    body = Line(Point(point1.getX(),point1.getY() + faceRad), point3)
    body.draw(win)
    point4 = win.getMouse()
    armSpan = (point1.getX() - point4.getX()) * 2
    arms = Line(point4, Point(armSpan + point4.getX(), point4.getY()))
    arms.draw(win)
    point5 = win.getMouse()
    legL = Line(point3, point5)
    legL.draw(win)
    rightFoot = Point((((point3.getX() - point5.getX()) * 2) + point5.getX()), point5.getY())
    legR = Line(point3, rightFoot)
    legR.draw(win)

# wk03 ex10 plots histogram based on values the user enters
def plotRainfall():
    win = GraphWin("Rain over time", 600, 600)
    inputBox = Entry(Point(100, 25), 20)
    inputBox.draw(win)
    startX = 300
    startY = 500
    for x in range(0,7):
        mouse = win.getMouse()
        value = float(inputBox.getText())
        bottomLeft = Point(startX, startY)
        topRight = Point(startX + 10, startY-value)
        rect = Rectangle(bottomLeft, topRight)
        rect.draw(win)
        rect.setFill("pink")
        caption = Text(Point(startX + 4, startY + 10), x+1)
        caption.draw(win)
        startX = startX + 12
    input()



    



#################### MAIN PROGRAMME BELOW ################
#drawStickFigure()
#drawCircle()
#drawArcheryTarget()
#drawRectangle()
#blueCircle()
#drawLine()
#tenLines()
#tenStrings()
#tenColouredRectangles()
#fiveClickStickFigure()
plotRainfall()