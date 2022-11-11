# Practical Worksheet 6: if statements and for loops
# Thomas Boxall, up2108121


from graphics import *
import math
import random

def distanceBetweenPoints(p1, p2):
    return math.sqrt(((p2.getX()-p1.getX())**2) + (p2.getY()-p1.getY())**2)


# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)




# ex01 fast food delivery costs

def fastFoodOrderPrice():
    basePrice = eval(input("Enter the price of the order: "))
    if(basePrice < 10):
        basePrice = basePrice + 1.5
    print("The total price of your order is £{0:0.2f}".format(basePrice))

# ex02 tells the user something to do based on the input they give
def whatToDoToday():
    temp = eval(input("Enter the temperature: "))
    if(temp>25):
        print("Swim in the sea")
    elif(temp>=10 and temp <= 25):
        print("Go waste money at Gunwharf Quays")
    elif (temp < 10):
        print("Stay at home and watch a film")

# ex03 displays square roots between two ints as params of function
def displaySquareRoots(start, end):
    for x in range(start, end+1):
        print("The square root of {0:2} is {1:0.3f}".format(x, math.sqrt(x)))

# ex04 return a grade or X based on param
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

# ex05 draw peas in a box
def peasInAPod():
    peaNumb = int(input("Enter the number of peas you want: "))
    podWidth = peaNumb * 100
    win = GraphWin("Pea Pod", podWidth, 100)
    for x in range(0, peaNumb+1):
        pea = Circle(Point(x*100+50, 50), 50)
        pea.setFill(color_rgb(0, 255, 0))
        pea.setOutline(color_rgb(0,255,0))
        pea.draw(win)
    win.getMouse()

# ex06 ticekt pricing

def ticketPrice(distance, age):
    base = 3
    cost = 0.15 * distance
    cost  = cost + base
    if(age <= 15 or age >= 60):
        cost = cost * 0.6
    return(cost)

# ex07 print suqare of numbers
def numberSquared(n):
    for i in range(n, 0, -1):
        printStr = ""
        for j in range(0, n, 1):
            printStr = printStr + str(i+j) + " "
        print(printStr)

# For exercise 8
def drawColouredEye(win, centre, radius, colourEye):
    colour = ["white", "", "black"]
    colour[1] = colourEye
    for x in range(0, len(colour)):
        drawCircle(win, centre, radius, colour[x])
        radius = radius / 2

def eyePicker():
    x = eval(input("Enter x: "))
    y = eval(input("Enter y: "))
    radius = int(input("Enter radius: "))
    col = input("Enter colour: ")
    if(col == "blue" or col == "grey" or col == "green" or col == "brown"):
        win = GraphWin()
        drawColouredEye(win, Point(x,y), radius, col)
    else:
        print("not a valid eye colour")
    
# ex09 20 lines
def drawPatchWindow():
    win = GraphWin()
    for x in range(0,10, 1):
        ln = Line(Point(0,x*10), Point((x+1)*10, 100))
        ln.draw(win)
        ln.setFill(color_rgb(255, 0, 0))
    for y in range(0, 10, 1):
        ln = Line(Point(y*10, 0), Point(100, (y+1)*10))
        ln.draw(win)
        ln.setFill(color_rgb(255, 0, 0))
    win.getMouse()

#ex 10 same as above but different
def drawPatch(win, x, y, col):
    for i in range(0, 10, 1):
        ln = Line(Point(x, y+ (i*10)), Point((i+1)*10, y*100))
        ln.draw(win)
        ln.setFill(col)
        ln2 = Line(Point(x+ (i*10), y), Point(x*100, (i+1)*10))
        ln2.draw(win)
        ln2.setFill(col)

def betterPatch(win, x, y, col):
    for i in range(1, 11, 1):
        line1 = Line(Point(x, y+(i*10)), Point((i*10) + x, y+100))
        line1.draw(win)
        line1.setFill(col)
        line2 = Line(Point((i*10)+x,y), Point((x+100), (i*10)+y))
        line2.draw(win)
        line2.setFill(col)

def drawPatchwork():
    win = GraphWin("Patchwork", 300, 200)
    colour = color_rgb(0, 0, 255)
    betterPatch(win, 0, 0, colour)
    betterPatch(win, 0, 100, colour)
    betterPatch(win, 100, 0, colour)
    betterPatch(win, 100, 100, colour)
    betterPatch(win, 200, 0, colour)
    betterPatch(win, 200, 100, colour)
    win.getMouse()


def eyesAllAround():
    win = GraphWin("Eyes", 500, 500)
    colourArray = ["blue", "grey", "green", "brown"]
    colCount = 0
    for x in range (0, 30, 1):
        drawColouredEye(win, win.getMouse(), 30, colourArray[colCount])
        if colCount == 3:
            colCount = 0
        else:
            colCount += 1

# ex12, archery game with fluctuating atmospheric conditions
def archeryGame():
    # start by drawing the target, use arrays 
    targetColours = ["blue", "red", "yellow"]
    targetSize = [150, 100, 50]
    x = 600
    y = 600
    win = GraphWin("Archery Game", x, y)

    for current in range(0, len(targetColours)):
        drawCircle(win, Point(x/2, y/2), targetSize[current], targetColours[current])
    
    # now we have a target, lets allow the use to click 5 times
    score = 0
    for i in range(0,5,1):
        pos = win.getMouse()
        posX = pos.getX()
        posY = pos.getY()
        fluctX = random.randint(1,5)
        fluctY = random.randint(1,5)
        fluctPosNeg = random.randint(1,2)
        if(fluctPosNeg == 1):
            posX += fluctX
            posY += fluctY
        elif(fluctPosNeg == 2):
            posX -= fluctX
            posY -= fluctY
        fluctPoint = Point(posX, posY)
        dist = distanceBetweenPoints(fluctPoint, Point(x/2, y/2))
        if (dist <= targetSize[2]):
            score += 10
        elif (dist > targetSize[2] and dist <= targetSize[1]):
            score += 5
        elif(dist > targetSize[1] and dist<= targetSize[0]):
            score += 2
        drawCircle(win, fluctPoint, 5, "black")
        #print(score)
    finalScore = Text(Point(x/2, 60), "Final Score: " + str(score))
    finalScore.setSize(15)
    finalScore.draw(win)
    win.getMouse()





#fastFoodOrderPrice()
#whatToDoToday()
#displaySquareRoots(2, 4)
#print(calculateGrade(6))
#peasInAPod()
#print(ticketPrice(100, 43))
#numberSquared(4)
#eyePicker()
#drawPatchWindow()
#drawPatchwork()
#eyesAllAround()
archeryGame()