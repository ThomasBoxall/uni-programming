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

def homeScreen():
    win = Tk()
    win.title("Home Screen")
    win.geometry(centreWindowString(win, 300, 150))
    win.resizable(width=False, height=False)
    win.columnconfigure(index=0, weight=1)
    win.columnconfigure(index=1, weight=1)
    win.rowconfigure(index=0, weight=1)
    win.rowconfigure(index=1, weight=1)
    win.rowconfigure(index=2, weight=1)

    def signin():
        win.destroy()
        loginApp()
    
    def signup():
        win.destroy()
        signUpToApp()

    siButton = Button(win, text="Sign In", command=signin)
    siButton.grid(row=1, column=0)

    suButton = Button(win, text="Sign Up", command=signup)
    suButton.grid(row=1, column=1)

    

    win.mainloop()

def signUpToApp():
    win = Tk()
    win.title("Welcome")
    win.geometry(centreWindowString(win, 300, 250))
    win.resizable(width=False, height=False)
    win.columnconfigure(index=0, weight=1)
    win.columnconfigure(index=1, weight=1)
    win.rowconfigure(index=0, weight=2)
    win.rowconfigure(index=1, weight=1)
    win.rowconfigure(index=2, weight=1)
    win.rowconfigure(index=3, weight=1)
    win.rowconfigure(index=4, weight=1)
    win.rowconfigure(index=5, weight=1)
    win.rowconfigure(index=6, weight=1)

    def cancelButton():
        win.destroy()
        homeScreen()
    
    # set state to be true, we then toggle this later
    state = True

    def showPasswordToggle():
        if state:
            lblPassword.configure(show="")
            lblConfirmPassword.configure(show="")
        state = not state

    lgFont = tkFont.Font(size=15, weight='bold')

    lblHeader = Label(win, text="Please Sign Up First", font=lgFont)
    lblHeader.grid(row=0, column=0, columnspan=2)

    lblUsefulInfo = Label(win)
    lblUsefulInfo.grid(row=1, column=0, columnspan=2)

    lblUsername = Label(win, text="Username")
    lblUsername.grid(row=2, column=0)

    entUsername = Entry(win)
    entUsername.grid(row=2, column=1)

    lblPassword = Label(win, text="Password")
    lblPassword.grid(row=3, column=0)

    entPassword = Entry(win, show="*")
    entPassword.grid(row=3, column=1)

    lblConfirmPassword = Label(win, text="Confirm Password")
    lblConfirmPassword.grid(row=4, column=0)

    entConfirmPassword = Entry(win, show="*")
    entConfirmPassword.grid(row=4, column=1)

    btnCancel = Button(win, text="Cancel", command=cancelButton)
    btnCancel.grid(row=6, column=0)

    btnSignUp = Button(win, text="Sign Up")
    btnSignUp.grid(row=6, column=1)#

    chkShowPassword = Checkbutton(win, text="Show Password", command=showPasswordToggle, variable=state)
    chkShowPassword.grid(row=5, column=0, columnspan=2)

    win.mainloop()

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
    

# loginApp()
homeScreen()