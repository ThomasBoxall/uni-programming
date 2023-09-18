from graphics import *
import os
# wk04 ex01 function to take users name as input and output string, with correct punctuation and spacing.
def personalGreeting():
    uInput = input("Enter your name here: ")
    print("Hello " + uInput + ", nice to see you!")

#wk 04 ex02 function to take users first name followed by last name then output first letter of first name dot last name
def formalName():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    print(firstName[0] + ". " + lastName)

# wk04 ex03 modify kilos2pounds from wk01 example code so that it displays values to two decimal places.
def kilos2poundsMod():
    # here we use float since a non-whole number is an acceptable input
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("{0:0.2f} kilos is equal to {1:0.2f} pounds".format(kilos, pounds))

# wk04 ex04 construct email address such that it is first four letters of last name, dot, first letter of first name, dot, last two digits of year they entered the university, at, myport.ac.uk
def generateEmail():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    year = input("Enter the year you entered the university: ")
    email = lastName[0:4] + "." + firstName[0] + "." + year[2:5] + "@myport.ac.uk"
    print(email)

# wk04 ex05 use string indexing to output character based on input.
def gradeTest():
    grades = "FFFFCCBBAAA"
    marks = int(input("Enter the marks scored here: "))
    print("The grade is " + grades[marks])

# wk04 ex06 user inputs word then on graphics window allow user to display the words where they click
def graphicLetter():
    userWord = input("Enter your word here: ")
    win = GraphWin("Fancy Text Box", 700, 700)
    for x in userWord:
        mousePos = win.getMouse()
        newLetter = Text(mousePos, x)
        newLetter.setSize(30)
        newLetter.draw(win)
    input()

# wk04 ex07 user enters a word and number of repetitions, song is generated based on this
def singASong():
    userWord = input("Enter a word here: ")
    lines = int(input("How many lines would you like in the song? "))
    reps = int(input("How many repetitions of the word "+ userWord + ", would you like on each line? "))

    for x in range (1,lines+1):
        printString = ""
        for y in range(1, reps+1):
            printString = printString + userWord + " "
        print(printString)

# wk04 ex08 display euros to pounds exchange rate table, with fancy formatting
def exchangeTable():
    headerString = "{0:^5} | {1:^5}".format("e", "£")
    headerLength = len(headerString)
    print(headerString)
    print("-"*headerLength)
    for euro in range (0, 21):
        pounds = euro * 1.17
        print("{0:>5} | {1:>5.2f}".format(euro, pounds))

def makeInitialism():
    """takes multi-word string input and outputs initials as capitals only"""
    userString  = input("Enter the string here: ")
    userList = userString.split()
    outputString = ""
    for current in userList:
        toOutput = current[0].upper()
        outputString = outputString + toOutput
    print(outputString)

def nameToNumber():
    """user enters name, using each letter has corresponding numerical value calculate sum of all letters in name"""
    name = input("Enter your name here: ")
    name = name.upper()
    total = 0
    for current in name:
        total = total + (ord(current)-64)
    print(total)

def fileInCaps():
    """take use input of file name and display contents of file in capital letters"""
    fileName = input("Enter file name here: ")
    cwd = os.path.dirname(os.path.realpath(__file__)) + "\\" #from stack overflow - don't know why this works but it does!
    f = open(cwd+fileName, "r")
    contents = f.read()
    f.close()
    contents = contents.upper()
    print(contents)

def rainfallChart():
    """read in file and output vaguely graphical representation of it"""
    cwd = os.path.dirname(os.path.realpath(__file__)) + "\\"
    f = open(cwd + "rainfall.txt", "r")
    fileContents = f.read()
    f.close()
    fileContentsList = fileContents.split("\n")
    for current in fileContentsList:
        currentList = current.split(" ")
        #print(currentList[0], currentList[1])
        print("{0:>15} {1:<50}".format(currentList[0], (int(currentList[1])*"*")))

def rainFallChartGraphical():
    cwd = os.path.dirname(os.path.realpath(__file__)) + "\\"
    f = open(cwd + "rainfall.txt", "r")
    fileContents = f.read()
    f.close()
    fileContentsList = fileContents.split("\n")
    win = GraphWin("Dave", 800, 800)
    labelX = 50
    rectangleX = 100
    y = 50

    for current in fileContentsList:
        currentList = current.split(" ")
        label = Text(Point(labelX, y), currentList[0])
        label.draw(win)
        rect = Rectangle(Point(rectangleX, y), Point(rectangleX + int(currentList[1]), y+30))
        rect.draw(win)
        rect.setFill("pink")
        y+=50
    input()

def rainfallInches():
    """reads in cm and output inches to file"""
    cwd = os.path.dirname(os.path.realpath(__file__)) + "\\"
    f = open(cwd + "rainfall.txt", "r")
    fileContents = f.read()
    f.close()
    fWrite = open(cwd+"rainfallInches.txt", "w")
    fileContentsList = fileContents.split("\n")
    for current in fileContentsList:
        currentList = current.split(" ")
        inches = int(currentList[1]) / 25.4
        print("{0} {1:.2f}".format(currentList[0], inches), file=fWrite)
    fWrite.close()
    print("done")

def wc():
    """display number of words, characters and lines in a file"""
    cwd = os.path.dirname(os.path.realpath(__file__)) + "\\"
    fileName = input("enter file name: ")
    f = open(cwd + fileName, "r")
    fileContents = f.read()
    f.close()
    characters = len(fileContents)
    fLines = fileContents.split("\n")
    lines = len(fLines)
    fwords = fileContents.split(" ")
    words = len(fwords)
    print("Characters: "+str(characters))
    print("Lines: "+str(lines))
    print("Words: "+str(words))
    





########## MAIN PROGRAM BELOW #########
#personalGreeting()
#formalName()
#kilos2poundsMod()
#generateEmail()
#gradeTest()
#graphicLetter()
#singASong()
#exchangeTable()
#makeInitialism()
#nameToNumber()
#fileInCaps()
#rainfallChart()
rainFallChartGraphical()
#rainfallInches()
#wc()
