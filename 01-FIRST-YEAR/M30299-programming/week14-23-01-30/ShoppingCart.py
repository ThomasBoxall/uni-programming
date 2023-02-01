from Laptop import *

class ShoppingCart():
    """
    A class to represent a shopping cart.
    A shopping cart has a list of items and a total price.
    The total price is the sum of the prices of the items.
    """

    def __init__(self):
        self.items = []
        self.total = 0

    def getItems(self):
        """
        Returns the items in the cart.
        """
        return self.items

    def getTotal(self):
        """
        Returns the total price of the items in the cart.
        """
        return self.total

    def addItem(self, item):
        """
        Adds the given item to the cart.
        """
        self.items.append(item)
        self.total = self.total + item.getPrice()
    
    def addLaptop(self, brand, model, price):
        laptop = Laptop(brand, model, price)
        self.addItem(laptop)

    def __str__(self):
        output = "Shopping cart contains:\n"
        for item in self.items:
            output += "{}\n".format(item)
        output += "Total: £{:.2f}".format(self.total)
        return output

    def setRamOfItem(self, index, newRam):
        self.total -= self.items[index].getPrice()
        self.items[index].setRram(newRam)
        self.total += self.items[index].getPrice()

    def setSsdOfItem(self, index, newSSD):
        self.total -= self.items[index].getPrice()
        self.items[index].setSSD(newSSD)
        self.total += self.items[index].getPrice()