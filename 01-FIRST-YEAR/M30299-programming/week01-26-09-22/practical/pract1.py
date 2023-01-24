# Practical Worksheet P1: Getting started with Python
# Thomas Boxall, up2108121


def sayHello():
    print("Hello world")


def count():
    for i in range(10):
        print(i)


def double():
    # here we use the built-in function int since we expect a whole number
    number = int(input("Enter a whole number: "))
    doubled = 2 * number
    print("If you double", number, "you get", doubled)


def kilos2pounds():
    # here we use float since a non-whole number is an acceptable input
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("The weight in pounds is", pounds)


# wk01 ex01
def sayName():
    print("My name is Thomas")

# wk01 ex02
def sayHello2():
    print("Hello")
    print("World")

# wk01 ex03
def euros2pounds():
    euros = eval(input("Enter an amount in euros to be converted to pounds: "))
    pounds = euros * 1.17
    print("Pounds: ", pounds)

# wk1 ex04
def sumDifference():
    numb1 = eval(input("Please enter number one: "))
    numb2 = eval(input("Please enter number two: "))
    sum = numb1 + numb2
    diff = numb1 - numb2
    print("The sum is: ", sum)
    print("The difference is: ", diff)

# wk01 ex05
def changeCounter():
    one = int(input("Enter the number of 1p you have: "))
    two = int(input("Enter the number ot 2p you have: "))
    five = int(input("Enter the number of 5p you have: "))
    oneTot = one
    twoTot = two * 2
    fiveTot = five * 5
    totalMoney = oneTot + twoTot + fiveTot
    print("The total amount of money you have (in pence) is: ", str(totalMoney) , "p")

# wk01 ex06
def tenHellos():
    for i in range(10):
        print("hello, world")

# wk01 ex07
def countTo():
    topNumb = int(input("Enter the number to count to: "))
    for i in range(1,topNumb+1):
        print(i)

# wk01 ex08
def zoomZoom():
    zoomTo = int(input("Enter a number to zoom to: "))
    for i in range(zoomTo):
        print("zoom", i+1)

# wk01 ex09
def weightsTable():
    print("Kilos  Pounds")
    for i in range(0, 110, 10):
        pound = 2.2 * i
        print(i, "\t", pound)

# wk01 ex10
def futureValue():
    invest = eval(input("Enter the amount you've invested: "))
    years = int(input("Enter the number of years you're investing for: "))
    value = invest
    for i in range(years):
        value = value * 1.035
    print("The total amount at the end of", years, "years is: ", value)


# wk01 challenge01
def multUseAdd():
    # a function which takes two integers and multiplies them through using addition only
    intOne = int(input("Enter integer 1: "))
    intTwo = int(input("Enter integer 2: "))
    total = 0
    for i in range(intTwo):
        total = total + intOne
    print(total)

# wk01 challenge02
def divideUseSubtract():
    # a function which takes two integers and divides intOne by intTwo using subtraction
    intOne = int(input("Enter integer 1: "))
    intTwo = int(input("Enter integer 2: "))
    remainder = intOne
    total = 0
    while(remainder >= intTwo):
        remainder -= intTwo
        total += 1
    print(total, "r", remainder)

# wk01 challenge03
def intToBin():
    # a function which takes in an integer then converts to 8-bit binary number
    integer = int(input("Enter an integer: "))
    leftToConvert = integer
    outputString = ""
    for i in range(7, -1, -1):
        currentPlace = 2**i
        if(leftToConvert >= currentPlace):
            outputString = outputString + "1"
            leftToConvert = leftToConvert - currentPlace
        else:
            outputString = outputString + "0"
    print(outputString)

# wk01 challenge04
def binToInt():
    # a function which takes a binary number and converts it to an integer
    binary = input("Enter a binary number (any length): ")
    binLength = len(binary)
    intTot = 0
    conValue = binLength
    for i in range(0, binLength, 1):
        conValue = conValue - 1
        if(binary[i] == "1"):
            intTot = intTot + (2**conValue)
    print("Integer: ", intTot)

#binToInt()
