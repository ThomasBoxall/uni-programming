# ITEM 3 COURSEWORK
from graphics import *

# HELPER FUNCTIONS
def centrePoint(tlPoint, radius):
    """Returns centre point of circle based on top left coordinate and radius of circle"""
    x = tlPoint.getX() + radius
    y = tlPoint.getY() + radius
    centre = Point(x, y)
    return centre


def drawCircle(win, centre, radius, colour):
    """Draws circle on screen and returns circle object"""
    c = Circle(centre, radius)
    c.setFill(colour)
    c.draw(win)
    c.setOutline(colour)
    return c

def drawRectangle(win, tlPoint, brPoint, colour):
    """Draws rectangle on screen and returns rectangle object"""
    r = Rectangle(tlPoint, brPoint)
    r.setFill(colour)
    r.draw(win)
    r.setOutline(colour)
    return r


def drawLine(win, point1, point2, colour):
    """Draws line on screen and returns line object"""
    l = Line(point1, point2)
    l.setOutline(colour)
    l.draw(win)
    return l

def getBrPoint(tlPoint, width, height):
    """Calculates a bottom right Point based on the Top Left point, width and height. Returns bottom right point object"""
    x = tlPoint.getX() + width
    y = tlPoint.getY() + height
    brPoint = Point(x, y)
    return brPoint

def drawCirclefromTL(win, tlPoint, radius, colour):
    """Draws a circle based on the top left coordinates"""
    centre = centrePoint(tlPoint, radius)
    drawCircle(win, centre, radius, colour)

# DRAW SINGLE PATCH FUNCTIONS
def drawCirclePatch(win, colour, tl):
    """Draws single square then calls drawFourSmallCircles() to draw alternating colour circles in that rectangle"""
    patchSize = 100
    increment = 20
    altFlag = True # this is used to alternate colours as we have to alternate between user defined colour and white
    for y in range(int(tl.getY()), int(tl.getY())+patchSize, increment):
        for x in range(int(tl.getX()), int(tl.getX())+patchSize, increment):
            currentTopLeft = Point(x, y)
            if altFlag:
                drawRectangle(win, currentTopLeft, getBrPoint(currentTopLeft, increment, increment), colour)
            else:
                drawRectangle(win, currentTopLeft, getBrPoint(currentTopLeft, increment, increment), "white")

            drawFourSmallCircles(win, colour, currentTopLeft, altFlag)
            altFlag = not altFlag

def drawFourSmallCircles(win, colour, tl, altFlag):
    """Draws four little circles in a 20x20 space, based from TopLeft (tl) point of specified colour or white if altFlag=True"""
    # all circles have radius 5
    for y in range(int(tl.getY()), int(tl.getY()+20), 10):
        for x in range(int(tl.getX()), int(tl.getX()+20), 10):
            currentTopLeft = Point(x, y)
            if altFlag:
                drawCirclefromTL(win, currentTopLeft, 5, "white")
            else:
                drawCirclefromTL(win, currentTopLeft, 5, colour)


def drawLinePatch(win, colour, tl):
    """Draw a single 'line' patch with TopLeft point tl"""
    # we add 100 as this moves to the other side of the patch
    # we add 10 as this is the gap between the lines
    for offset in range(0, 100,10):
        # define start and end points for line one
        startOne = Point(offset + tl.getX(), tl.getY())
        endOne = Point(tl.getX()+100, offset + tl.getY() + 10)
        drawLine(win, startOne, endOne, colour)
        # define start and end points of line two
        startTwo = Point(tl.getX(), tl.getY()+offset)
        endTwo = Point(offset + tl.getX() + 10, tl.getY()+100)
        drawLine(win, startTwo, endTwo, colour)

def drawPlainPatch(win, colour, tl):
    """Draw a plain patch of specified colour"""
    drawRectangle(win, tl, getBrPoint(tl, 100, 100), colour)


def populateWindow(win, colours, dimension):
    for y in range(0,dimension,100):
        for x in range(0,dimension,100):
            topLeft = Point(x,y)
            if x >= 100 and y >= 100 and x<dimension-100 and y<dimension-100:
                #we actually need to draw a patch now
                if x == y or x+y == dimension - 100:
                    drawLinePatch(win, getColour(colours, topLeft, dimension), topLeft)
                else:
                    drawCirclePatch(win, getColour(colours, topLeft, dimension), topLeft)
            else:
                drawPlainPatch(win, getColour(colours, topLeft, dimension), topLeft)

def getColour(colours, tl, dimension):
    x = tl.getX()
    y = tl.getY()
    if x == y or x+y == dimension - 100:
        # both diagonals
        return colours[0]
    elif x>y and y+x < dimension:
        return colours[1]
    elif x<y and x+y >= dimension:
        return colours[1]
    else:
        return colours[2]

def getUserInput():
    acceptableColours = ["red", "green", "blue", "purple", "orange", "cyan"]
    acceptableSizes = ["5", "7"] # these are strings so we can validate without causing casting errors. They get casted in the validateInt function
    
    inputValid = False
    while inputValid == False:
        printWelcomeMessage(acceptableColours, acceptableSizes)
        inputValid = True
        colours = []
        for x in range(0,3):
            colourInp = input("Please enter a colour: ").lower()
            if not validateString(acceptableColours, colourInp):
                inputValid = False
            colours.append(colourInp)
        size = input("Enter size: ")
        # validate number input
        sizeValid, sizeInt = validateInt(acceptableSizes, size)
        if not sizeValid:
            inputValid = False
        if not inputValid:
            print("One or more inputs you entered is invalid. Please re-enter them.")
        else:
            print("Inputs valid, generating pattern.")
        
    return colours, sizeInt


def validateString(validOptions, toValidate):
    if toValidate in validOptions:
        foundValid = True
    else:
        foundValid = False
    return foundValid

def validateInt(validOptions, toValidate):
    foundValid = False
    intToValidate = 0
    for each in validOptions:
        if each == toValidate:
            foundValid = True
            intToValidate = int(toValidate)
    return foundValid, intToValidate

def printWelcomeMessage(colours, sizes):
    """displays a welcome message to the program containing valid colours and sizes"""
    print("="*20)
    print("WELCOME TO PATCHES PROGRAM")
    print("-"*20)
    print("Acceptable Colours: "+formatArray(colours))
    print("Acceptable sizes: "+ formatArray(sizes))
    print("="*20)

def formatArray(arrayToFormat):
    """Builds string containing contents of array and returns it"""
    retStr = ""
    for each in arrayToFormat:
        retStr += each + ", "
    return retStr


def winInit(size):
    """Instantiate new GraphWin with dimension size and set background colour to white"""
    win = GraphWin("uo2108121 PATCH PROGRAM", size, size)
    win.setBackground("white")
    return win

def main():
    colours, size = getUserInput()
    size = size * 100 # increase size to 100 times input size so that its correct scale to pass into the GraphWin constructor and populateWindow() functions
    win = winInit(size)
    populateWindow(win, colours, size)
    win.getMouse() # ask about this line and if it should exist or not?


main()