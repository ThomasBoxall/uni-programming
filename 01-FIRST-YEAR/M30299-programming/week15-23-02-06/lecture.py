from tkinter import *

def main():
    win = Tk()

    width = 400
    height = 100
    x = 300
    y = 400

    win.geometry("{}x{}+{}+{}".format(width, height, x, y))


    win.mainloop()

main()