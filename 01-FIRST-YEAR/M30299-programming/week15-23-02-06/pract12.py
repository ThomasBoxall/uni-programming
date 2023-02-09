from tkinter import *
import tkinter.font as tkFont

loginDetails = {
    "YousefD": "VenterboSS",
    "SergeiT": "25Operyu",
    "YemiO ": "Idec704",
    "WernerS": "IAmMel12",
}

def centreWindowString(win, width, height):
    screenWidth = win.winfo_screenwidth()/2 - width/2
    screenHeight = win.winfo_screenheight()/2 - height / 2
    retString = ("{}x{}+{:.0f}+{:.0f}".format(width, height, screenWidth, screenHeight))
    return retString

def loginApp():
    """
    The function creates a window, and sets its title, size, and column widths.
    It then calls the createWidgets function to create the widgets on this window.
    Finally, it calls the mainloop method on the window to start the event loop.
    """
    win = Tk()
    win.title("Welcome")
    win.geometry(centreWindowString(win, 300, 150))
    win.resizable(width=False, height=False)
    win.columnconfigure(index=0, weight=1)
    win.columnconfigure(index=1, weight=2)
    win.rowconfigure(index=0, weight=1)
    win.rowconfigure(index=1, weight=1)
    win.rowconfigure(index=2, weight=1)
    win.rowconfigure(index=3, weight=1)
    win.rowconfigure(index=4, weight=1)
    createWidgets(win)
    win.mainloop()


def createWidgets(win):
    """
    Creates widgets on window passed as parameter.
    Configures widgets with actions.
    """
    outputText = Text(win, height=1, width=30)
    outputText.insert("1.0", "Please login to continue:")
    outputText.grid(row=0, column=0, columnspan=2)

    userNameLabel = Label(win, text="Username")
    userNameLabel.grid(row=1, column=0)

    passwordLabel = Label(win, text="Password")
    passwordLabel.grid(row=2, column=0)

    userNameEntry = Entry(win)
    userNameEntry.grid(row=1, column=1)

    passwordEntry = Entry(win, show="*")
    passwordEntry.grid(row=2, column=1)

    def signInCommand():
        signIn(userNameEntry, passwordEntry, outputText, win)

    def fontUpdate():
        changeFonts([userNameLabel, passwordLabel, userNameEntry, passwordEntry, signInButton, cancelButton, fontButton] , win)

    signInButton = Button(win, text="Sign in", command=signInCommand)
    signInButton.grid(row=3, column=1)

    cancelButton = Button(win, text="Cancel", command=win.destroy)
    cancelButton.grid(row=3, column=0)

    fontButton = Button(win, text="Change Font", command=fontUpdate)
    fontButton.grid(row=4, column=0, columnspan=2)

def signIn(userNameEntry, passwordEntry, outputText, win):
    """
    Gets what user has inputted into the userNameEntry and passwordEntry.
    Uses loginDetails to check if userName and password are valid.
    Updates outputText with result.
    """
    userName = userNameEntry.get()
    password = passwordEntry.get()
    outputText.delete("1.0", "2.0")
    if userName in loginDetails:
        if loginDetails[userName] == password:
            outputText.insert("1.0", "Welcome {}!".format(userName))
            win.configure(bg="#00ff00")
        else:
            outputText.insert("1.0", "Wrong password, try again.")
            win.configure(bg="#ff0000")
    else:
        outputText.insert("1.0", "Username not found, try again.")
        win.configure(bg="#ffff00")

def changeFonts(widgetList, win):
    helv36 = tkFont.Font(family='Helvetica', size=15, weight='bold')
    for current in widgetList:
        current.configure(font=helv36)
    

loginApp()