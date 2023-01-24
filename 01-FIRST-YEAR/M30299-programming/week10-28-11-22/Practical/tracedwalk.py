import random

def getInputs():
    squares = int(input("Enter the number of squares: "))
    return squares

def initialiseSquares(number):
    squares = []
    for i in range(0,number):
        squares.append(0)
    return squares

def walkEnd(currentSquare, numberOfSquares):
    if currentSquare >= numberOfSquares:
        return True
    elif currentSquare < 0:
        return True
    else:
        return False
def printWalk(squares):
    for current in range (0, len(squares)):
        print(str(current+1) + "  " + str(squares[current]))

def goForWalk(number, squares):
    currentSquare = random.randint(0,number-1)
    walkOver = False
    while walkOver == False:
        direction = random.randint(1,2)
        if direction == 1:
            # forwards (plus one)
            currentSquare += 1
            if not walkEnd(currentSquare, number):
                squares[currentSquare] += 1
            else:
                walkOver = True
        else:
            # backwards (minus one)
            currentSquare -= 1
            if not walkEnd(currentSquare, number):
                squares[currentSquare] += 1
            else:
                walkOver = True
    printWalk(squares)

def main():
    number = getInputs()
    squares = initialiseSquares(number)
    goForWalk(number, squares)

main()