# house.py - a simple program to draw a house


from graphics import *


def main():
    doorColour, lightsOn, size, houseNumb = getInputs()
    drawHouse(doorColour, lightsOn, size, houseNumb)
    


def getInputs():
    doorColour = input("Enter door colour: ")
    lightsYN = input("Are the lights on (y/n): ")
    lightsOn = lightsYN[0] == "y"
    size = int(input("Enter window size: "))
    houseNumb = int(input("Enter house number: "))
    return doorColour, lightsOn, size, houseNumb


def drawHouse(doorColour, lightsOn, size, houseNumb):
    win = GraphWin("House", size, size)
    win.setCoords(0,200,200,0)

    roof = Polygon(Point(2, 60), Point(42, 2),
                   Point(158, 2), Point(198,60))
    roof.setFill("pink")
    roof.draw(win)

    # draw wall and door
    drawRectangle(win, Point(2, 60), Point(198, 198), "brown")
    drawRectangle(win, Point(30, 110), Point(80, 198), doorColour)
    number = Text(Point(55, 130), str(houseNumb))
    number.draw(win)


    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawRectangle(win, Point(110, 110), Point(170, 170), windowColour)


def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)


main()
