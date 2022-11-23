import random

def getInputs():
    numbTimesToFlip = int(input("Enter the number of times which you would like the coin to be flipped: "))
    return numbTimesToFlip

def simulateFlips(numbTimesToFlip):
    heads = 0
    tails = 0
    for i in range(0,numbTimesToFlip, 1):
        coin = random.randint(1, 2)
        if coin == 1:
            heads += 1
        else:
            tails += 1
    return heads, tails

def displayResults(heads, tails):
    headsPrint = heads/100
    tailsPrint = tails/100
    print("Heads {0:0.2f}, Tails {1:0.2f}".format(headsPrint, tailsPrint))

def main():
    heads, tails = simulateFlips(getInputs())
    displayResults(heads, tails)

main()