from graphics import *
from random import *

def getInputs():
    numberHouses = int(input("Number Houses: "))
    height = int(input("Height: "))
    doorCol = input("Door colour: ")
    lightOnProb = float(input("Light on probablity (float < 1): "))
    return numberHouses, height, doorCol, lightOnProb

def drawHouse(win, topLeft, height, doorCol, lightCol, houseNumb):
    roofCol = "grey"
    houseCol = "grey"
    x = topLeft.getX()
    y = topLeft.getY()
    roof = Polygon(Point(x+100, y), Point(x, y+(height/3)), Point(x+100, y+(height/3)))
    roof.draw(win)
    roof.setFill(roofCol)
    house = Rectangle(Point(x, y+(height/3)), Point(x+100, y+height))
    house.draw(win)
    house.setFill(houseCol)
    door = Rectangle(Point(x+45, y+(height/4)*3), Point(x+55, y+height))
    door.setFill(doorCol)
    door.draw(win)
    window = Rectangle(Point(x+60, y+(height/2)), Point(x+90, y+(height/3)*2))
    window.setFill(lightCol)
    window.draw(win)
    number = Text(Point(x+50, y+(height/4)*3.5), houseNumb)

def drawStreet(numberHouses, height, door, lightProb):
    win = GraphWin("Street", numberHouses * 100, height + 10)
    for i in range (0,numberHouses):
        topLeftPoint = Point(i*100, 10)
        lightColour = getLightState(lightProb)
        drawHouse(win, topLeftPoint, height, door, lightColour, i+1)
    win.getMouse()


def getLightState(lightProb):
    if random() < lightProb:
        return "yellow"
    else:
        return "grey"

def main():
    numberHouses, height, doorCol, lightOnProb = getInputs()
    drawStreet(numberHouses, height, doorCol, lightOnProb)

main()