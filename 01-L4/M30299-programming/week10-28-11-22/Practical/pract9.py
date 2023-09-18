# Practical Worksheet 9
# Thomas Boxall, 08-01-23

from graphics import *

def displayDate(day, month, year):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    print(str(day), months[month-1], str(year))

def wordLengths(words):
    for currentWord in words:
        print(currentWord, str(len(currentWord)))

def drawHexagon():
    points = []
    win = GraphWin()
    for loopCount in range(0,6):
        points.append(win.getMouse())
    p = Polygon(points)
    p.setFill("red")
    p.draw(win)
    win.getMouse()

def testMarks():
    marks = []
    continueEnter = True
    while continueEnter:
        marks.append(input("Enter a mark (or 'x' to finish): "))
        continueEnter = marks[-1]!= "x"
    for x in range (0,6):
        currentCount = marks.count(str(x))
        print(str(currentCount)+ " student(s) got "+str(x)+" marks")

def drawBarChart(data):
    # rowNumber = 1
    for rowNumber in range(1, max(data)+1):
        printString = ""
        for currentBar in data:
            if currentBar >= rowNumber:
                printString += "#"
            else:
                printString += " "
        print(printString)


### CALL FROM BELOW
#displayDate(14,2,2019)
#wordLengths(["bacon", "jam", "spam"])
#drawHexagon()
#testMarks()
drawBarChart([3,1,2])