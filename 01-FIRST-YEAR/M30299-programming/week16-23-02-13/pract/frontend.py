from tkinter import *
from tkinter import messagebox
from backend import *
from datetime import *

mainWin = Tk()
cart = ShoppingCart()


def setupCart():
    """
    Add some products to the cart.
    """
    cart.addLaptop("Apple", "MacBook Air", 999.99)
    cart.addLaptop("Razer", "Blade", 1799.99)
    cart.addLaptop("Microsoft", "Surface", 900.00)
    cart.addItem(GamingLaptop("Alienware", "m15", 1999.99)) 
    razer = GamingLaptop("Razer", "Blade", 2499.99) 
    razer.setGpu("AMD Radeon 12GB") 
    cart.addItem(razer)
    cart.addItem(GamingLaptop("MSI", "GS65", 1799.99))


def setupMainWin():
    """
    Setup `mainWin` to display the cart.
    Display a button that lists all products and a button that closes `mainWin`.
    """
    mainWin.title("Cart")
    mainWin.geometry("300x100")
    mainWin.resizable(False, False)
    # The first column (list of products) needs to be bigger than the other
    mainWin.columnconfigure(index=0, weight=4)

    listBtn = Button(mainWin, text="List all products", command=listProducts)
    listBtn.grid(row=0, column=0, padx=15, pady=10, sticky="w")

    quitBtn = Button(mainWin, text="Quit", command=mainWin.destroy)
    quitBtn.grid(row=0, column=1, padx=15, pady=10, sticky="e")

    cardBtn = Button(mainWin, text="Pay with Card", command=payWithCard)
    cardBtn.grid(row=50, column=0, padx=15, pady=10, sticky="w")

    voucherBtn = Button(mainWin, text="Pay with Voucher", command=payWithVoucher)
    voucherBtn.grid(row=50, column=1, padx=15, pady=10, sticky="e")

    mainWin.mainloop()

def payWithVoucher():
    voucherWin = Toplevel()
    voucherWin.geometry("250x100")
    voucherWin.resizable(False, False)

    headerLabel = Label(voucherWin, text="Pay with Voucher")
    headerLabel.grid(row=0, column=0, columnspan=2)
    headerLabel.configure(font=("TkDefaultFont", 12, "bold"))

    codeLabel = Label(voucherWin, text="Voucher Code")
    codeLabel.grid(row=1, column=0)

    codeEntry = Entry(voucherWin)
    codeEntry.grid(row=1, column=1)

    cancelButton = Button(voucherWin, text="Cancel", command=voucherWin.destroy)
    cancelButton.grid(row=2, column=0, sticky="w")

    def voucherCheck():
        if checkVoucher(codeEntry.get()):
            voucherWin.destroy()
            mainWin.destroy()
        else:
            messagebox.showerror("Invalid Voucher", "The voucher you entered is invalid. Please try again.")

    submitButton = Button(voucherWin, text="Submit", command=voucherCheck)
    submitButton.grid(row=2, column=1, sticky="e")

    voucherWin.mainloop()

def payWithCard():
    cardWin = Toplevel()
    cardWin.geometry("400x200")
    cardWin.resizable(False, False)

    headerLabel = Label(cardWin, text="Pay with Card")
    headerLabel.grid(row=0, column=0, columnspan=2)
    headerLabel.configure(font=("TkDefaultFont", 12, "bold"))

    holderLabel = Label(cardWin, text="Card Holder", anchor="w", width=20)
    holderLabel.grid(row=1, column=0, columnspan=2)
    
    holderEntry = Entry(cardWin)
    holderEntry.grid(row=2, column=0, columnspan=2)

    numberLabel = Label(cardWin, text="Card Number", anchor="w", width=20)
    numberLabel.grid(row=3, column=0, columnspan=2)

    numberEntry = Entry(cardWin)
    numberEntry.grid(row=4, column=0, columnspan=2)

    dateLabel = Label(cardWin, text="Expiry Date")
    dateLabel.grid(row=5, column=0)

    dateEntry = Entry(cardWin)
    dateEntry.grid(row=5, column=1)

    cvvLabel = Label(cardWin, text="CVV")
    cvvLabel.grid(row=6, column=0)

    cvvEntry = Entry(cardWin, show="#")
    cvvEntry.grid(row=6, column=1)

    cancelButton = Button(cardWin, text="Cancel", command=cardWin.destroy, anchor="w")
    cancelButton.grid(row=7, column=0)

    def cardCheck():
        number = numberEntry.get()
        date = dateEntry.get()
        cvv = cvvEntry.get()
        if checkCard(number, date, cvv):
            cardWin.destroy()
            mainWin.destroy()


    confirmButton = Button(cardWin, text="Confirm", anchor="e", command=cardCheck)
    confirmButton.grid(row=7, column=1)

    def checkCard(number, dateInput, cvv):
        today = date.today()
        todayDateString = "{}/{}".format(today.month, str(today.year)[-2:])
        providedDate = date(int("20"+str(dateInput)[-2:]), int(str(dateInput)[0:2]), 1)
        validInput = True

        if len(number)!= 16:
            validInput = False
            messagebox.showerror("Card Number", "The card number you entered is invalid. Please try again.")
        if today >= providedDate:
            validInput = False
            messagebox.showerror("Date", "The expiry date you entered is invalid. Please try again.")
        if len(cvv) != 3:
            validInput = False
            messagebox.showerror("CVV", "The CVV you entered is invalid. Please try again.")
        return validInput


def checkVoucher(providedCode):
    vouchers = ["C3BSE2JaAmhlc", "f3gdqwMvX3o84", "JLjAws3didoq6"]
    if providedCode in vouchers:
        return True
    else:
        return False


def listProducts():
    """
    For each product in `cart`, create a text and a button on the `mainWin`.
    The text contains the product's information.
    The button is used to configure the product.
    Also display the total price of the cart at the bottom of `mainWin`.
    """
    numberOfProds = cart.getCartLength()
    # 50px per product + 1 row of buttons + 1 row for the total + 1 row for the payment
    height = 50 * (numberOfProds + 3)
    mainWin.geometry("400x{}".format(height))

    for productIndex in range(numberOfProds):
        mainWin.rowconfigure(index=productIndex+1, weight=1)

        product = cart.getItemAt(productIndex)
        productTxt = Text(mainWin, height=2, width=50)
        productTxt.insert("1.0", str(product))
        # Add the text to row `productIndex` + 1 (first row is for the buttons)
        productTxt.grid(row=productIndex + 1, column=0,
                        padx=10, pady=5, sticky="w")

        def configCmd(i=productIndex):
            configWindow(i)

        configBtn = Button(mainWin, text="Configure", command=configCmd)
        configBtn.grid(row=productIndex + 1, column=1, padx=10, pady=5)

    totalLabel = Label(mainWin, text="Total: £{:.2f}".format(cart.getTotal()))
    totalLabel.grid(row=numberOfProds + 1, column=0,
                    padx=15, pady=10, sticky="w")
    totalLabel.config(font=("TkDefaultFont", 12, "bold"))


def configWindow(productIndex):
    """
    Create a new window to configure the product at `productIndex` of `cart`.
    The window will contain a text, showing the product's information,
    The window will also contain an entry to change the RAM capacity.
    When the change is submitted, the list of products in `mainWin` will update.
    """
    configWin = Toplevel()
    configWin.geometry("400x300")
    configWin.resizable(False, False)

    product = cart.getItemAt(productIndex)
    configWin.title("Configure {} {}".format(
        product.getBrand(), product.getModel()))

    prodTxt = Text(configWin, height=2, width=45)
    prodTxt.insert("1.0", "Configure {}".format(product))
    prodTxt.grid(row=0, column=0, padx=15, pady=5, columnspan=2)

    brandLabel = Label(configWin, text="Brand", anchor="e", width=30)
    brandLabel.grid(row=1, column=0, padx=10, pady=10)

    brandEntry = Entry(configWin)
    brandEntry.insert(0, str(product.getBrand()))
    brandEntry.configure(state=DISABLED)
    brandEntry.grid(row=1, column=1, padx=10, pady=10)

    modelLabel = Label(configWin, text="Model", anchor="e", width=30)
    modelLabel.grid(row=2, column=0)

    modelEntry = Entry(configWin)
    modelEntry.insert(0, str(product.getModel()))
    modelEntry.configure(state=DISABLED)
    modelEntry.grid(row=2, column=1, padx=10, pady=10)

    ramLabel = Label(configWin, text="Enter RAM capacity (GB):", anchor="e", width=30)
    ramLabel.grid(row=3, column=0, padx=10, pady=10)

    ramEntry = Entry(configWin)
    # Default value is the current RAM
    ramEntry.insert(0, str(product.getRam()))
    ramEntry.grid(row=3, column=1, padx=10, pady=10)

    if isinstance(product, GamingLaptop):
        gpuLabel = Label(configWin, text="GPU", anchor="e", width=30)
        gpuLabel.grid(row=4, column=0, padx=10, pady=10)

        gpuEntry=Entry(configWin)
        gpuEntry.grid(row=4, column=1, padx=10, pady=10)

    cancelBtn = Button(configWin, text="Cancel", command=configWin.destroy)
    cancelBtn.grid(row=5, column=0, padx=10, pady=10)

    def submitCmd():
        newRam = int(ramEntry.get())
        cart.setRamOfItem(productIndex, newRam)
        if isinstance(product, GamingLaptop):
            product.setGpu(gpuEntry.get())
        listProducts()  # Refresh the list of products
        configWin.destroy()  # Close the config window

    submitBtn = Button(configWin, text="Submit", command=submitCmd)
    submitBtn.grid(row=5, column=1, padx=10, pady=2)

    configWin.mainloop()  # Start the event loop for the config window


def main():
    setupCart()
    setupMainWin()
    print("Cart is closed, the total price is : £{:.2f}".format(
        cart.getTotal()))

main()