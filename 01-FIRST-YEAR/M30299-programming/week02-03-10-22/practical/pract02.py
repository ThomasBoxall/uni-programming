# Week 02, Practical
# Thomas Boxall, up2108121
# 05-10-2022

import math

# ex01
def circumferenceOfCircle():
    radius = eval(input("Enter the radius of a circle: "))
    circumference = 2 * math.pi * radius
    print("For a circle with radius", radius, "the circumference is", circumference)

# ex02
def areaOfCircle():
    radius = eval(input("Please enter the radius of a circle: "))
    area = math.pi * (radius * radius)
    print("For a circle with radius", radius, "the area is", area)

# ex03
def costOfPizza():
    diam = eval(input("Enter the pizza's diameter (in cm): "))
    radius = diam/2
    area = math.pi * (radius * radius)
    cost = area / 1.5
    print("Your pizza's toppings will cost", cost, "pence")

# ex04
def slopeOfLine():
    x1, y1 = eval(input("Enter coord 1 as x1, y1: "))
    x2, y2 = eval(input("Enter coord 2 as x2, y2: "))
    slope = (y2-y1) / (x2-x1)
    print("The slope of the line is: ", slope)

# ex05
def distanceBetweenPoints():
    x1, y1 = eval(input("Enter coord 1 as x1, y1: "))
    x2, y2 = eval(input("Enter coord 2 as x2, y2: "))
    distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    print("The distance between points is:", distance)

# ex06
def travelStatistics():
    speed = eval(input("Enter the average speed of the journey: "))
    time = eval(input("Enter the time the journey took (in hours): "))
    distance = speed * time
    fuel = distance / 5
    print("The journey was", distance, "km and used", fuel, "L fuel.")

# ex07
def sumOfSquares():
    upperCount = int(input("Please enter the number to sum squares to: "))
    total = 0
    for current in range(1, upperCount + 1):
        total = total + (current ** 2)
    print(total)

# ex08
def averageOfNumbers():
    numbers = int(input("Enter the number of numbers you would like an average of: "))
    total = 0
    for x in range(0, numbers):
        uInput = eval(input("Enter a number: "))
        total = total + uInput
    average = total / numbers
    print("The average is:", average)

# ex09
def fibonacci():
    countTo = int(input("Enter the number of the fibonacci sequence you would like to count to: "))
    current = 0
    previousTerm = 0
    previousTerm1 = 1
    for x in range(1, countTo + 1):
        current = previousTerm + previousTerm1
        previousTerm1 = previousTerm
        previousTerm = current
    print(current)

# ex10
def selectCoins():
    money = int(input("Enter an amount of money in pence: "))
    
    twoHundredRemainder = money % 200
    twoHundred = (money - twoHundredRemainder) / 200
    print("£2.00 x", twoHundred)
    
    oneHundredRemainder = twoHundredRemainder % 100
    oneHundred = (twoHundredRemainder - oneHundredRemainder) / 100
    print("£1.00 x",oneHundred)

    fiftyRemainder = oneHundredRemainder % 50
    fifty = (oneHundredRemainder - fiftyRemainder) / 50
    print("£0.50 x", fifty)

    twentyRemainder = fiftyRemainder % 20
    twenty = (fiftyRemainder - twentyRemainder) / 20
    print("£0.20 x", twenty)

    tenRemainder = twentyRemainder % 10
    ten = (twentyRemainder - tenRemainder) / 10
    print("£0.10 x", ten)

    fiveRemainder = tenRemainder % 5
    five = (tenRemainder - fiveRemainder) / 5
    print("£0.05 x", five)

    twoRemainder = fiveRemainder % 2
    two = (fiveRemainder - twoRemainder) / 2
    print("£0.02 x", two)

    oneRemainder = twoRemainder % 1
    one = (twoRemainder - oneRemainder) / 1
    print("£0.01 x", one)

# ex10e - re-write selectCoins() to use a function which reduces the similar code repetitions
def coinCalc(prevRemainder, divVal):
    remainder = prevRemainder % divVal
    current = (prevRemainder - remainder) / divVal
    print(current, "x", divVal, "p")
    return remainder

def selectCoinsNew():
    money = int(input("Enter an amount of money in pence: "))
    twoH = coinCalc(money, 200)
    oneH = coinCalc(twoH, 100)
    fifty = coinCalc(oneH, 50)
    twenty = coinCalc(fifty, 20)
    ten = coinCalc(twenty, 10)
    five = coinCalc(ten, 5)
    two = coinCalc(five, 2)
    one = coinCalc(two, 1)


# MAIN PROGRAM BELOW
#circumferenceOfCircle()
#areaOfCircle()
#costOfPizza()
#slopeOfLine()
#distanceBetweenPoints()
#travelStatistics()
#sumOfSquares()
#averageOfNumbers()
#fibonacci()
#selectCoins()
selectCoinsNew()