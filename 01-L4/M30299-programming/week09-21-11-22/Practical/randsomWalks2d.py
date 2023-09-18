def takeAWalk(numSteps):
    from random import random
    stepsNSOfStart = 0
    stepsEWOfStart = 0
    for step in range(numSteps):
        rand = random()
        if rand <0.25:
            stepsNSOfStart = stepsNSOfStart - 1
        elif rand <0.5:
            stepsNSOfStart = stepsNSOfStart + 1
        elif rand < 0.75:
            stepsEWOfStart = stepsEWOfStart - 1
        else:
            stepsEWOfStart = stepsEWOfStart + 1
    return abs(stepsNSOfStart), abs(stepsEWOfStart)

def getInputs():
    numWalks = int(input("How many random walks to take? "))
    numSteps = int(input("How many steps for each walk? "))
    return numWalks, numSteps

def printExpectedDistance(averageSteps):
    print("The expected number of steps away from the", end=" ")
    print("start point is", averageSteps)

def takeWalks(numWalks, numSteps):
    dist = 0
    for walk in range(numWalks):
        stepsAwayNS, stepsAwayEW = takeAWalk(numSteps)
        dist = dist + distanceBetweenPoints(0, 0, stepsAwayNS, stepsAwayEW)
        
    return dist

def distanceBetweenPoints(x1, y1, x2, y2):
    import math
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))


def main():
    numWalks, numSteps = getInputs()
    averageSteps = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageSteps)


main()