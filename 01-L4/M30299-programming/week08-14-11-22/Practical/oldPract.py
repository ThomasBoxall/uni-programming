from graphics import *
import math

def calculateGrade(score):
    if (score >= 16 and score <= 20):
        return("A")
    elif (score >= 12 and score <= 15):
        return("B")
    elif (score >= 8 and score <= 11):
        return("C")
    elif (score >= 0 and score <= 7):
        return("F")
    else:
        return("X")

def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawBrownEye(win, centre, radius):
    """Draws a single brown eye at specified centre with specified radius"""    
    colour = ["white", "brown", "black"]
    for x in range(0, len(colour)):
        drawCircle(win, centre, radius, colour[x])
        radius = radius / 2

def distanceBetweenPoints(p1, p2):
    return math.sqrt(((p2.getX()-p1.getX())**2) + (p2.getY()-p1.getY())**2)



def drawColEye(win, centre, radius, col):
    """Draws a single brown eye at specified centre with specified radius with specified centre colour"""    
    colour = ["white", "", "black"]
    colour[1] = col
    for x in range(0, len(colour)):
        drawCircle(win, centre, radius, colour[x])
        radius = radius / 2