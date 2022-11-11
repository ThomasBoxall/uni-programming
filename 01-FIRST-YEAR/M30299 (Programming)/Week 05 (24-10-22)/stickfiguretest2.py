from graphics import *

def footballPlayer():
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    arm1 = Line(Point(200, 90), Point(160, 100))
    arm1.draw(win)
    arm2 = Line(Point(200, 90), Point(240, 100))
    arm2.draw(win)
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)

    # my below
    floor = Line(Point(0,170), Point(300,170))
    floor.draw(win)

    football = Circle(Point(160,165), 5)
    football.setFill("blue")
    football.draw(win)

    goal = Rectangle(Point(50,170), Point(60,20))
    goal.setFill("black")
    goal.draw(win)

    # step 2
    txt = Text(Point(100, 30), "")
    txt.draw(win)
    fullTxt = ["G", "Go", "Goa", "Goal", "Goal!"]
    for x in range(0,5):
        win.getMouse()
        txt.setText(fullTxt[x])
        football.move(-25, 0)


    win.getMouse() #ensures window stays in final state until program execution stopped

footballPlayer()