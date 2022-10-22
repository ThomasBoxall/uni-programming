from graphics import *

def main():
    secretWord = "DanteAlighieri"
    character = int(input("Which character do you want? "))
    index = character - 1
    print(secretWord[index])    

def mainOne():
    word = "DanteAlighieri"

    print(len(word))

    for letter in word:
        print(letter)

def format():
    pi = 3.1415926535897932384626433
    pi2 = 3.34534534534
    print("My values are {:0.3f} and {:.2f}".format(pi,pi2))


def graphicsFinally():
    win = GraphWin("Dave", 500, 500)
    sentence = "can you see what is going on"
    size = len(sentence)
    offset = 10
    for i in range(size):
        x = offset + i*15
        y = offset + i*15
        point = Point(x,y)
        text = Text(point, sentence[i])
        text.draw(win)



    input()


#main()
#mainOne()
#format()
graphicsFinally()