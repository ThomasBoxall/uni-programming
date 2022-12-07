# ITEM 3 COURSEWORK - up2108121
from graphics import *
import time

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


def drawLine(win, point1, point2, colour, thickness=1):
    """Draws line on screen and returns line object"""
    l = Line(point1, point2)
    l.setOutline(colour)
    l.setWidth(thickness)
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
    circ = drawCircle(win, centre, radius, colour)
    return circ

# DRAW SINGLE PATCH FUNCTIONS
def drawCirclePatch(win, colour, tl, patchArray):
    """Draws single square then calls drawFourSmallCircles() to draw alternating colour circles in that rectangle"""
    patchSize = 100
    increment = 20
    altFlag = True # this is used to alternate colours as we have to alternate between user defined colour and white
    for y in range(int(tl.getY()), int(tl.getY())+patchSize, increment):
        for x in range(int(tl.getX()), int(tl.getX())+patchSize, increment):
            currentTopLeft = Point(x, y)
            if altFlag:
                # use the user inputted colour
                patchArray[int(tl.getY()/100)][int(tl.getX()/100)].append(drawRectangle(win, currentTopLeft, getBrPoint(currentTopLeft, increment, increment), colour))
            else:
                # use colour as white
                patchArray[int(tl.getY()/100)][int(tl.getX()/100)].append(drawRectangle(win, currentTopLeft, getBrPoint(currentTopLeft, increment, increment), "white"))
            # now draw the four smaller circles inside the square
            drawFourSmallCircles(win, colour, currentTopLeft, altFlag, patchArray, tl)
            altFlag = not altFlag # switch the flag so we use the other colours on the next iteration

def drawFourSmallCircles(win, colour, tl, altFlag, patchArray, paTL):
    """Draws four little circles in a 20x20 space, based from TopLeft (tl) point of specified colour or white if altFlag=True"""
    # all circles have radius 5
    for y in range(int(tl.getY()), int(tl.getY()+20), 10):
        for x in range(int(tl.getX()), int(tl.getX()+20), 10):
            currentTopLeft = Point(x, y)
            if altFlag:
                # use colour as white
                patchArray[int(paTL.getY()/100)][int(paTL.getX()/100)].append(drawCirclefromTL(win, currentTopLeft, 5, "white"))
            else:
                # use colour as use inputted colour
                patchArray[int(paTL.getY()/100)][int(paTL.getX()/100)].append(drawCirclefromTL(win, currentTopLeft, 5, colour))


def drawLinePatch(win, colour, tl, patchArray):
    """Draw a single 'line' patch with TopLeft point tl"""
    # we add 100 as this moves to the other side of the patch
    # we add 10 as this is the gap between the lines
    # in each iteration we draw one line from each 'half' of the patch (line one is top right side and line two is bottom left side)
    for offset in range(0, 100,10):
        # define start and end points for line one
        startOne = Point(offset + tl.getX(), tl.getY())
        endOne = Point(tl.getX()+100, offset + tl.getY() + 10)
        patchArray[int(tl.getY()/100)][int(tl.getX()/100)].append(drawLine(win, startOne, endOne, colour)) # draw line one
        # define start and end points of line two
        startTwo = Point(tl.getX(), tl.getY()+offset)
        endTwo = Point(offset + tl.getX() + 10, tl.getY()+100)
        patchArray[int(tl.getY()/100)][int(tl.getX()/100)].append(drawLine(win, startTwo, endTwo, colour)) # draw line two

def drawPlainPatch(win, colour, tl, patchArray):
    """Draw a plain patch of specified colour"""
    patchArray[int(tl.getY()/100)][int(tl.getX()/100)].append(drawRectangle(win, tl, getBrPoint(tl, 100, 100), colour))


def populateWindow(win, colours, dimension, patchArray):
    for y in range(0,dimension,100):
        patchArray.append([])
        for x in range(0,dimension,100):
            patchArray[int(y/100)].append([])
            topLeft = Point(x,y)
            if x >= 100 and y >= 100 and x<dimension-100 and y<dimension-100:
                #we actually need to draw a patch now
                if x == y or x+y == dimension - 100:
                    drawLinePatch(win, getColour(colours, topLeft, dimension), topLeft, patchArray)
                else:
                    drawCirclePatch(win, getColour(colours, topLeft, dimension), topLeft, patchArray)
            else:
                drawPlainPatch(win, getColour(colours, topLeft, dimension), topLeft, patchArray)

def getColour(colours, tl, dimension):
    """takes colours (list), top left (point) and dimension (int) then returns colour (str) for correct location on grid"""
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
    """prompts user to enter three colours then an integer then validates against valid options stored in this function. Returns a list for colours and a int for size with validated user inputs in it"""
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
    print("="*30)
    print("| WELCOME TO PATCHES PROGRAM |")
    print("="*30)
    print("Acceptable Colours: "+formatArray(colours))
    print("Acceptable sizes: "+ formatArray(sizes) + "\n")
    # print("-")

def formatArray(arrayToFormat):
    """Builds string containing contents of array and returns it"""
    retStr = ""
    for each in arrayToFormat:
        if each == arrayToFormat[-1]:
            retStr += each
        else: 
            retStr += each + ", "
    return retStr


def winInit(size):
    """Instantiate new GraphWin with dimension size and set background colour to white then return GraphWin object"""
    win = GraphWin("up2108121 PATCH PROGRAM", size, size)
    win.setBackground("white")
    return win

def getPatch(clickPos):
    # will take input like Point(233,434) and need to return Point(200,400)
    x = clickPos.getX()
    y = clickPos.getY()
    xCoord = x // 100
    yCoord = y // 100
    return Point(xCoord * 100, yCoord * 100), xCoord, yCoord

def drawBorder(win, patchPos):
    border = []
    border.append(drawLine(win, Point(patchPos.getX(), patchPos.getY()), Point(patchPos.getX()+100, patchPos.getY()), "black", 4))
    border.append(drawLine(win, Point(patchPos.getX(), patchPos.getY()), Point(patchPos.getX(), patchPos.getY()+100), "black", 4))
    border.append(drawLine(win, Point(patchPos.getX()+100, patchPos.getY()), Point(patchPos.getX()+100, patchPos.getY()+100), "black", 4))
    border.append(drawLine(win, Point(patchPos.getX(), patchPos.getY()+100), Point(patchPos.getX()+100, patchPos.getY()+100), "black", 4))
    return border

def undrawBorder(border):
    for each in border:
        print(type(each))
        each.undraw()
    border.clear()

def borderFix(border, win, patchPos):
    undrawBorder(border)
    return drawBorder(win, patchPos)

def challenge(win, patchArray, size, colours):
    """Challenge feature"""    
     # ask about this line and if it should exist or not?
    # print(patchArray[int(pos.getY()/100)][int(pos.getX()/100)])
    # for each in patchArray[int(pos.getY()/100)][int(pos.getX()/100)]:
    #     # patchArray.remove(each)
    #     each.undraw()
    # patchArray[int(pos.getY()/100)][int(pos.getX()/100)].clear()
    # print("x", patchArray[int(pos.getY()/100)][int(pos.getX()/100)])

    doChallenge = True
    patchSelected = False
    while doChallenge:
        if not patchSelected:
            pos = win.getMouse()
            selectedPoint, selectedX, selectedY = getPatch(pos) 
            border = drawBorder(win, selectedPoint)
            patchSelected = True
        keySelect = win.getKey()
        if keySelect == "Escape":
            undrawBorder(border)
            patchSelected = False
            print("esc")
        elif keySelect == "d":
            for each in patchArray[int(selectedY)][int(selectedX)]:
                each.undraw()
            patchArray[int(selectedY)][int(selectedX)].clear()
            print(patchArray[int(selectedY)][int(selectedX)])
        if patchArray[int(selectedY)][int(selectedX)] == []:
            if keySelect == "1":
                drawPlainPatch(win, colours[0], selectedPoint, patchArray)
                border = borderFix(border, win, selectedPoint)
            elif keySelect == "2":
                drawPlainPatch(win, colours[1], selectedPoint, patchArray)
                border = borderFix(border, win, selectedPoint)
            elif keySelect == "3":
                drawPlainPatch(win, colours[2], selectedPoint, patchArray)
                border = borderFix(border, win, selectedPoint)
            elif keySelect == "4":
                drawCirclePatch(win, colours[0], selectedPoint, patchArray)
                border = borderFix(border, win, selectedPoint)
            elif keySelect == "5":
                drawCirclePatch(win, colours[1], selectedPoint, patchArray)
                border = borderFix(border, win, selectedPoint)
            elif keySelect == "6":
                drawCirclePatch(win, colours[2], selectedPoint, patchArray)
                border = borderFix(border, win, selectedPoint)
            elif keySelect == "7":
                drawLinePatch(win, colours[0], selectedPoint, patchArray)
                border = borderFix(border, win, selectedPoint)
            elif keySelect == "8":
                drawLinePatch(win, colours[1], selectedPoint, patchArray)
                border = borderFix(border, win, selectedPoint)
            elif keySelect == "9":
                drawLinePatch(win, colours[2], selectedPoint, patchArray)
                border = borderFix(border, win, selectedPoint)
        if keySelect == "Up":
            if patchArray[int(selectedY)-1][int(selectedX)] == []:
                patchArray[int(selectedY)-1][int(selectedX)] = patchArray[int(selectedY)][int(selectedX)] # set new index to be old index
                for each in patchArray[int(selectedY)-1][int(selectedX)]:
                    # move each object in the patch one by one to the new location
                    for x in range (0,5):
                        time.sleep(0.01)
                        each.move(0,-20)
                patchArray[int(selectedY)][int(selectedX)] = [] # empty the old index
        elif keySelect == "Down":
            if patchArray[int(selectedY)+1][int(selectedX)] == []:
                patchArray[int(selectedY)+1][int(selectedX)] = patchArray[int(selectedY)][int(selectedX)] # set new index to be old index
                for each in patchArray[int(selectedY)+1][int(selectedX)]:
                    # move each object in the patch one by one to the new location
                    for x in range (0,5):
                        time.sleep(0.01)
                        each.move(0,+20)
                patchArray[int(selectedY)][int(selectedX)] = [] # empty the old index
        elif keySelect == "Right":
            if patchArray[int(selectedY)][int(selectedX)+1] == []:
                patchArray[int(selectedY)][int(selectedX)+1] = patchArray[int(selectedY)][int(selectedX)] # set new index to be old index
                for each in patchArray[int(selectedY)][int(selectedX)+1]:
                    # move each object in the patch one by one to the new location
                    for x in range (0,5):
                        time.sleep(0.01)
                        each.move(+20,0)
                patchArray[int(selectedY)][int(selectedX)] = [] # empty the old index
        elif keySelect == "Left":
            if patchArray[int(selectedY)][int(selectedX)-1] == []:
                patchArray[int(selectedY)][int(selectedX)-1] = patchArray[int(selectedY)][int(selectedX)] # set new index to be old index
                for each in patchArray[int(selectedY)][int(selectedX)-1]:
                    # move each object in the patch one by one to the new location
                    for x in range (0,5):
                        time.sleep(0.01)
                        each.move(-20,0)
                patchArray[int(selectedY)][int(selectedX)] = [] # empty the old index

    # border = drawBorder(win, selectedPoint)


def main():
    colours, size = getUserInput()
    # at this point the user inputs are valid and can be manipulated
    size = size * 100 # increase size to 100 times input size so that its correct scale to pass into the GraphWin constructor and populateWindow() functions
    win = winInit(size)
    patchArray = []
    populateWindow(win, colours, size, patchArray)
    # while True:
    #     print(getPatch(win.getMouse()))
    #challenge(win, patchArray, size)
    challenge(win, patchArray, size, colours)

    win.getMouse()

main()