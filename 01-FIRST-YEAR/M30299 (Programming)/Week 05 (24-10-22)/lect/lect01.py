from graphics import *
import random

# functions
def line():
    pass

def myCircle(win, centre, radius, colour):
    c = Circle(centre, radius)
    c.setFill(colour)
    c.draw(win)

def rectangle():
    pass

def fancyCirc():
    colours = ["blue", "pink", "orange", "brown", "red", "green"]
    win = GraphWin("", 500, 500)
    for i in range(0, random.randint(0,250)):
        radius = random.randint(0,50)
        centre = Point(random.randint(0,500), random.randint(0,500))
        col = colours[random.randint(0, len(colours)-1)]
        myCircle(win, centre, radius, col)
    input()

# entry point
def main():
    print("Live lectures coding")
    size = 700
    win = GraphWin("Live lectures coding", size, size)
    #radius = int(input("radius: "))
    #col = input("Colour: ")
    colours = ["blue", "red", "orange"]

    dimension = 100

    for i in range(3):
        x = dimension
        y = dimension * i + dimension
        centre = Point(x,y)
        colour = colours[i]
        myCircle(win, centre, dimension/2, colour)

    
    

    input()


# exec entry point
#main()
fancyCirc()


# the basis of this will be the basis of the coursework