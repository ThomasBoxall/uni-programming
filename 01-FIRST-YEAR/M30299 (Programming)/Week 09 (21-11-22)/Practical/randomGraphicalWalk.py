from graphics import *
import math
import random

def getInputs():
    distance = int(input("Enter the max distance of a walk: "))
    numberWalks = int(input("Enter the number of walks to simulate: "))
    return distance, numberWalks

def windowConfig(distance):
    winSize = distance * 2 + 100
    win = GraphWin("Walk Map", winSize, winSize)
    c = Circle(Point(winSize/2, winSize/2), distance)
    c.draw(win)
    c.setOutline("black")
    c.setWidth(3)
    return win

def distanceBetweenPoints(point1, point2):
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

def walkLine(win, start, end):
    ln = Line(start, end)
    # ln.setFill("grey")
    # ln.setOutline("")
    # ln.setWidth("1")
    ln.draw(win)

def goForWalk(win, distance, numberWalks):
    centreCircle = Point(win.getWidth()/2, win.getHeight()/2)
    counter = Text(Point(win.getWidth()/4,10), "0/"+str(numberWalks))
    counter.draw(win)
    for walkCount in range(0, numberWalks):   
        currentPos = centreCircle
        prevPos = centreCircle
        counter.setText(str(walkCount+1)+"/"+str(numberWalks))
        # print("loopy") 
        while distanceBetweenPoints(centreCircle, currentPos) < distance:
            #prevPos = currentPos
            direction = random.randint(1,100)
            if direction < 25:
                # walk north
                currentPos = Point(currentPos.getX(), currentPos.getY()+5)
            elif direction < 50:
                #walk east
                # currentPos.x = currentPos.getX() + 5
                currentPos = Point(currentPos.getX()+5, currentPos.getY())
            elif direction <75:
                #walk south
                # currentPos.y = currentPos.getY() - 5
                currentPos = Point(currentPos.getX(), currentPos.getY()-5)
            else:
                #walk west
                # currentPos.x = currentPos.getX() - 5
                currentPos = Point(currentPos.getX()-5, currentPos.getY())
            walkLine(win, prevPos, currentPos)
            prevPos = currentPos



def main():
    distance, numberWalks = getInputs()
    win = windowConfig(distance)
    goForWalk(win, distance, numberWalks)
    win.getMouse()

main()