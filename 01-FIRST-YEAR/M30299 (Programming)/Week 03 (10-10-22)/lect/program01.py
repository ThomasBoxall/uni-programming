from graphics import *

def main():
    # main code here
    print("Practical 3")

    title = "Dave"
    size = 500
    win = GraphWin(title, size, size)
    
    midX = win.getWidth()
    midY = win.getHeight()
    centre = Point(midX/2,midY/2)

    myCircle = Circle(centre, 150)
    myCircle.setFill("red")
    myCircle.draw(win)

    midCirc = Circle(centre, 100)
    midCirc.setFill("blue")
    midCirc.draw(win)

    smolCirc = Circle(centre, 50)
    smolCirc.setFill("green")
    smolCirc.draw(win)

    input()

main()