from graphics import *
import time
from oldPract import *
import random

def getName():
    prompt = "Enter Name: "
    name = input(prompt)
    while name.isalpha() != True:
        print("Enter a valid name.")
        name = input(prompt)
    return name

def trafficLights():
    black = color_rgb(0,0,0)
    white = color_rgb(255,255,255)
    red = color_rgb(255,0,0)
    amber = color_rgb(255,194,0)
    green = color_rgb(26,173,12)

    win = GraphWin("TL", 100, 300)
    win.setBackground(black)
    r = Circle(Point(50,50), 50)
    r.draw(win)
    r.setFill(black)
    r.setOutline(white)
    a = Circle(Point(50,150), 50)
    a.draw(win)
    a.setFill(black)
    a.setOutline(white)
    g = Circle(Point(50,250), 50)
    g.draw(win)
    g.setFill(black)
    g.setOutline(white)

    while True:
        r.setFill(red)
        time.sleep(5)
        a.setFill(amber)
        time.sleep(5)
        r.setFill(black)
        a.setFill(black)
        g.setFill(green)
        time.sleep(2)
        g.setFill(black)
        a.setFill(amber)
        time.sleep(5)
        a.setFill(black)

def gradeCoursework():
    prompt = "Input Mark: "
    mark = int(input(prompt))
    while mark <0 and mark >20:
        print("Invalid")
        mark = int(input(prompt))
    print("The pupil achieved a grade of " + calculateGrade(mark))

def orderPrice():
    total = 0
    promptUnit = "Enter the unit price of a product: "
    promptQty = "Enter the quantity of the product: "
    promptCont = "Enter y to add another product: "
    cont = "y"
    while cont == "y":
        unit = float(input(promptUnit))
        qty = int(input(promptQty))
        total += (unit*qty)
        cont = input(promptCont)
    print("The total price is £{0:0.2f}".format(total))
    
def clickableEye():
    win = GraphWin("Click Eye", 200, 250)
    cent = Point(100,100)
    drawBrownEye(win, cent, 100)
    exit = False
    txt = ""
    t = Text(Point(100, 225), txt)
    t.draw(win)
    while exit == False:
        txt = ""
        mousePos = win.getMouse()
        dist = distanceBetweenPoints(mousePos, cent)
        if dist > 100:
            exit = True
        elif dist > 50:
            txt = "white bit"
        elif dist > 25:
            txt = "iris"
        else:
            txt = "pupil"
        t.setText(txt)        

def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def temperatureConverter():
    choice = "y"
    while choice != "e":
        print("Celsius to Fahrenheit (cf)")
        print("Fahrenheit to Celsius (fc)")
        print("Exit (e)")
        choice = input("Enter choice: ")
        if choice == "cf":
            print(celsius2Fahrenheit(int(input("Enter celsius value: "))))
        elif choice == "fc":
            print(fahrenheit2Celsius(int(input("Enter Fahrenheit value: "))))

def guessTheNumber():
    toGuess = random.randint(1,100)
    guessed = False
    numbGuesses = 0
    while guessed != True and numbGuesses <7:
        numbGuesses += 1
        uInput = int(input("Enter your guess: "))
        if uInput == toGuess:
            guessed = True
        elif uInput > toGuess:
            print("Too high")
        elif uInput < toGuess:
            print("Too low")
    if guessed == True:
        print("Well done, you win!")
    else:
        print("You loose! The number was "+str(toGuess))

def tableTennisScorer():
    x = 800
    y = 400
    win = GraphWin("Table Tennis Scorer", x, y)
    ln = Line(Point(x/2, 0), Point(x/2, y))
    ln.setWidth(4)
    ln.setFill("green")
    ln.draw(win)
    winner = False
    p1Text = Text(Point(x/4, y/4), "0")
    p1Text.draw(win)
    p2Text = Text(Point((x/4)*3, y/4), "0")
    p2Text.draw(win)
    p1 = 0
    p2 = 0
    while winner == False:
        clickPos = win.getMouse()
        if clickPos.getX() > x/2:
            p2 += 1
            p2Text.setText(str(p2))
        else:
            p1 += 1
            p1Text.setText(str(p1))
        if(p1>=11 and p1>=(p2+2)):
            winner = True
            winText = Text(Point(x/4, (y/4)*3), "wins")
            winText.draw(win)
            win.getMouse()
        if(p2>=11 and p2>=(p1+2)):
            winner = True
            winText = Text(Point((x/4)*3, (y/4)*3), "wins")
            winText.draw(win)
            win.getMouse()
        

def clickableBoxOfEyes(rows, columns):
    winX = (columns * 100) + 100
    winY = (rows * 100) + 100
    win = GraphWin("Click an Eye", winX, winY)
    border = Rectangle(Point(50,50), Point(winX-50, winY-50))
    border.draw(win)
    border.setOutline("black")
    border.setWidth(4)
    caption = Text(Point(winX/2, winY-30), "")
    caption.setSize(15)
    caption.draw(win)
    for i in range(100, (100 * rows+1), 100):
        for j in range (100, (100 * columns+1), 100):
            drawColEye(win, Point(j, i), 50, "cornflower blue")
    # get mouse click from the user and do different things based on where it is
    exit = False
    while exit == False:
        clickPos = win.getMouse()
        # draw little black circle where user clicks
        c = Circle(clickPos, 3)
        c.setFill("black")
        c.setOutline("black")
        c.draw(win)
        # first check if we need to exit
        cpX = clickPos.getX()
        cpY = clickPos.getY()
        if (cpX < 50 or cpX > winX -50 or cpY < 50 or cpY > winY-50):
            exit = True
        else:
            # now iterate all possible locations for centre of eye and see if we clicked on any of them
            foundEye = False
            for i in range(100, (100 * rows+1), 100):
                for j in range (100, (100 * columns+1), 100):
                    currentCentre = Point(j,i)
                    if(distanceBetweenPoints(currentCentre, clickPos)<50):
                        outString = "Eye at row {0:0.0f}, column {1:0.0f}.".format(j/100, i/100)
                        caption.setText(outString)
                        foundEye = True
            if foundEye == False:
                # execute if we didn't click on any of the eyes
                caption.setText("Between eyes")
                    
def findTheCircle():
    win = GraphWin("Find The Circle", 600, 600)
    radius = 30
    continueGame = True
    score = 0
    while continueGame == True:
        guessesLeft = 10
        centre = Point(random.randint(0,600), random.randint(0,600))
        c = Circle(centre, radius)
        #c.draw(win)
        won = False
        prevPos = Point(0,0)
        clickPos = Point(0,0)
        while guessesLeft >0 and won == False:
            prevPos = clickPos
            clickPos = win.getMouse()
            guessesLeft -= 1
            dist = distanceBetweenPoints(clickPos, centre)
            if (dist < radius):
                #found the circle
                won = True
                score += 1
                radius = radius * 0.9
            else:
                if(guessesLeft < 9):
                    #display message based on prev location
                    if (distanceBetweenPoints(clickPos, prevPos) > dist):
                        print("further")
                    elif (distanceBetweenPoints(clickPos, prevPos) < dist):
                        print("Closer")
                if guessesLeft < 1:
                    continueGame = False


def betterFindTheCircle():
    win = GraphWin("Find the Circle", 600, 600)
    radius = 30
    continueGame = True
    score = 0
    while continueGame == True:
        # loop through here while player hasn't lost, will break from this loop if the player looses
        # initialise an individual game here
        guessesLeft = 10
        centre = Point(random.randint(0, 600), random.randint(0,600))
        c =  Circle(centre, radius)
        c.draw(win) # debug line to display circle on screen
        won = False # used to break out of the current game and trigger this code to run again
        prevPos = Point(0,0) # initialise this here
        clickPos = Point(0,0) # initialise this here
        while guessesLeft >= 1 and won == False:
            # this loop allows user to have 10 guesses and can break out if the user wins it
            guessesLeft -= 1
            prevPos = clickPos
            clickPos = win.getMouse()
            dist = distanceBetweenPoints(clickPos, centre)
            if dist < radius:
                # found circle
                won = True
                score += 1
                radius = radius * 0.9 # reduce radius by 10% ready for next game
                # inner while loop won't run again, this will allow game to start a new level from outer while loop
            else:
                if guessesLeft < 9:
                    # not the first click so can use prevPos to find if further or closer to the circle
                    print("DIST: ", dist, "DBP: ", distanceBetweenPoints(clickPos, prevPos))
                    if distanceBetweenPoints(clickPos, prevPos) > dist:
                        print("further")
                    else:
                        print("closer")
                if guessesLeft <= 0:
                    # lost game :( break from outer while loop
                    continueGame = False






######### MAIN PROGRAM ############
#print(getName())
#trafficLights()
#gradeCoursework()
#orderPrice()
#clickableEye()
#temperatureConverter()
#guessTheNumber()
#tableTennisScorer()
#clickableBoxOfEyes(6,10)
#findTheCircle()
betterFindTheCircle()