# Practical Worksheet 5: Using functions
# Thomas Boxall, up2108121


from turtle import distance
from graphics import *
import math
import random


# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2

def circumferenceOfCircle(radius):
    circ = math.pi * radius * 2
    return circ

def circleInfo():
    uRadius = eval(input("Enter the radius of a circle: "))
    area = areaOfCircle(uRadius)
    circ = circumferenceOfCircle(uRadius)
    print("The area is {0:0.3f} and the circumference is {1:0.3f}".format(area, circ))

# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def drawBrownEyeInCentre():
    window = GraphWin()
    # Add your code here
    centre = Point(window.getWidth()/2, window.getHeight()/2)
    radius = [60, 30, 15]
    colour = ["white", "brown", "black"]
    for x in range(0, len(radius)):
        drawCircle(window, centre, radius[x], colour[x])
    window.getKey()

def drawBlockOfStars(width, height):
    for x in range(0, height):
        print("*"*width)

def drawLetterE():
    toDraw = [[8,2],[2,2],[5,2],[2,2],[8,2]]
    for x in range(0,len(toDraw)):
        drawBlockOfStars(toDraw[x][0], toDraw[x][1])


# For exercise 5
def drawBrownEye(win, centre, radius):
    """Draws a single brown eye at specified centre with specified radius"""
    #pass
    # Remove pass and add your code here
    
    colour = ["white", "brown", "black"]
    for x in range(0, len(colour)):
        drawCircle(win, centre, radius, colour[x])
        radius = radius / 2

def drawPairOfBrownEyes():
    x = 400
    y = 200
    win = GraphWin("I'm watching you", x, y)
    radius = 50
    centreLeft = x/2 - radius
    centreRight = x/2 + radius
    drawBrownEye(win, Point(centreLeft, y/2), radius)
    drawBrownEye(win, Point(centreRight, y/2), radius)
    input()

def distanceBetweenPoints(p1, p2):
    return math.sqrt(((p2.getX()-p1.getX())**2) + (p2.getY()-p1.getY())**2)

def drawBlocks(sp1, st1, sp2, st2, h):
    for x in range(0,h):
        print(" "*sp1 + "*"*st1 + " "*sp2 + "*"*st2)

def drawLetterA():
    toDraw = [[1,8,1,0,2], [0,2,6,2,2], [0,10,0,0,2], [0,2,6,2,3]]
    for x in toDraw:
        drawBlocks(x[0], x[1], x[2], x[3], x[4])

def drawFourPairsOfBrownEyes():
    win = GraphWin("Beady eyes", 600,600)
    for x in range(0,4):
        p1 = win.getMouse()
        p2 = win.getMouse()
        rad = distanceBetweenPoints(p1,p2)
        centreLeft = p1.getX() - rad
        centreRight = p1.getX() + rad
        drawBrownEye(win, Point(centreLeft, p1.getY()), rad)
        drawBrownEye(win, Point(centreRight, p1.getY()), rad)
    win.getMouse()

def displayTextWithSpaces(ttd, size, loc, win):
    text = Text(loc, ttd)
    text.draw(win)
    text.setSize(size)

def constructVisionChart():
    sizes = [30,25,20,15,10,5]
    x = 600
    y = 700
    dispX = x/2
    dispY = 100
    win = GraphWin("Can you see me?", x, y)
    for current in sizes:
        uString = input("Enter a string: ")
        uString = uString.upper()
        strToDisplay = ""
        for currentLetter in uString:
            strToDisplay += currentLetter + " "
        displayTextWithSpaces(strToDisplay, current, Point(dispX, dispY), win)
        dispY += 100
    win.getMouse()

def drawStickFigureFamily():
    win = GraphWin("Stick figure", 700, 500)
    #drawStickFigure(Point(100,100), 5, win)
    sticksToDraw = [[200, 300, 5], [250, 300, 4], [300, 300, 3], [325, 300, 2], [360, 300, 1]]
    for currentStick in sticksToDraw:
        drawStickFigure(Point(currentStick[0], currentStick[1]), currentStick[2], win)
    win.getMouse()

def drawStickFigure(centrePoint, mod, win):
    centX = centrePoint.getX()
    centY = centrePoint.getY()
    neck = Point(centX, (centY-5*mod))
    waist = Point(centX, (centY+10*mod))
    body = Line(neck, waist)
    body.draw(win)
    headRad = 2*mod
    head = Circle(Point(centX, neck.getY()-headRad), headRad)
    head.draw(win)
    arms = Line(Point((centX-3.5*mod), centY), Point((centX + 3.5*mod), centY))
    arms.draw(win)
    lleg = Line(waist, Point(waist.getX()-3*mod, waist.getY()+5*mod))
    lleg.draw(win)
    rleg = Line(waist, Point(waist.getX()+3*mod, waist.getY()+5*mod))
    rleg.draw(win)
    

#print(circumferenceOfCircle(23))
#circleInfo()
#drawBrownEyeInCentre()
#drawBlockOfStars(5,3)
#drawLetterE()
#drawPairOfBrownEyes()
#print(distanceBetweenPoints(Point(1,2), Point(4,6)))
#drawLetterA()
#drawFourPairsOfBrownEyes()
#constructVisionChart()
drawStickFigureFamily()