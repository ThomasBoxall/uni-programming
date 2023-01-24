# tennis.py - top-down design


def main():
    prWinPt, numSets = getInputs()
    wins = simulateNSets(prWinPt, numSets)
    printSummary(wins, numSets)


def getInputs():
    prWinPt = float(input("Prob. of winning a point: "))
    numSets = int(input("Sets to simulate: "))
    return prWinPt, numSets


def simulateNSets(prWinPt, numSets):
    wins = 0
    pointsPl = 0
    pointsOp = 0
    for set in range(numSets):
        while not setOver(pointsPl, pointsOp):
            pointsPl, pointsOp = simulateGame(prWinPt)
        if pointsPl > pointsOp:
            wins = wins + 1
    return wins

def simulateGame(prWinPt):
    from random import random
    pointsPl, pointsOp = 0, 0
    while not gameOver(pointsPl, pointsOp):
        if random() < prWinPt:
            pointsPl = pointsPl + 1
        else:
            pointsOp = pointsOp + 1
    return pointsPl, pointsOp

def setOver(pointsP1, pointsOp):
    if pointsP1 + 2 >= pointsOp:
        return True
    elif pointsOp + 2>= pointsP1:
        return True
    else:
        return False

def gameOver(pointsPl, pointsOp):
    return (pointsPl >= 4 or pointsOp >= 4) and  \
              abs(pointsPl - pointsOp) >= 2


def printSummary(wins, numGames):
    proportion = wins / numGames
    print("Wins:", wins, end="  ")
    print("Proportion: {0:0.2f}".format(proportion))


main()
