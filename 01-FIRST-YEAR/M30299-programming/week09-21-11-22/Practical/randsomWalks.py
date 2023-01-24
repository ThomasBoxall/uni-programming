# assembled from document

def takeAWalk(numSteps):
    from random import random
    stepsForwardOfStart = 0
    for step in range(numSteps):
        if random() < 0.5:
            stepsForwardOfStart = stepsForwardOfStart - 1
        else:
            stepsForwardOfStart = stepsForwardOfStart + 1
    return abs(stepsForwardOfStart)

def getInputs():
    numWalks = int(input("How many random walks to take? "))
    numSteps = int(input("How many steps for each walk? "))
    return numWalks, numSteps

def printExpectedDistance(averageSteps):
    print("The expected number of steps away from the", end=" ")
    print("start point is", averageSteps)

def takeWalks(numWalks, numSteps):
    totalSteps = 0
    for walk in range(numWalks):
        stepsAway = takeAWalk(numSteps)
        totalSteps = totalSteps + stepsAway
    return totalSteps / numWalks


def main():
    numWalks, numSteps = getInputs()
    averageSteps = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageSteps)


main()