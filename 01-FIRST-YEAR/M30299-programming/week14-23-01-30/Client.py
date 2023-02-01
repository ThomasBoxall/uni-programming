from Laptop import *
from GamingLaptop import *
from ShoppingCart import *


def testLaptop():
    """
    tests the Laptop class
    """
    laptop = Laptop("Dell", "XPS", 999.99)
    print("price: £{:.2f}".format(laptop.getPrice()))
    print(laptop)
    laptop.setRram(16)
    print(laptop, laptop.getPrice())
    print(laptop.getBrand())
    # laptop.setSSD("1TB")
    # print(laptop)
    laptop.setRram(32)
    print(laptop, laptop.getPrice())


def testShoppingCart():
    """
    tests the ShoppingCart class
    """
    cart = ShoppingCart()
    laptop1 = Laptop("Dell", "XPS", 999.99)
    laptop2 = Laptop("Lenovo", "ThinkPad", 799.99)
    laptop3 = Laptop("Apple", "MacBook Pro", 1299.99)
    cart.addItem(laptop1)
    cart.addItem(laptop2)
    cart.addItem(laptop3)
    print("total: £{:.2f}".format(cart.getTotal()))
    print(cart)
    items = cart.getItems()
    laptop = items[1]
    laptop.setRram(32)
    print(cart)
    cart.addLaptop("Apple", "Mac Book Pro", 1299.99)
    print(cart)
    cart.setRamOfItem(0, 32)
    print(cart)
    cart.setSsdOfItem(0, "1TB")
    print(cart)


def testGamingLaptop():
    """
    tests the GamingLaptop class
    """
    gamingLaptop = GamingLaptop("Alienware", "m15", 1999.99)
    print("price: £{:.2f}".format(gamingLaptop.getPrice()))
    print(gamingLaptop)
    gamingLaptop.setRram(32)
    print(gamingLaptop)
    gamingLaptop.setGpu("AMD Radeon 12GB")
    print(gamingLaptop)


testLaptop()
# testGamingLaptop()
# testShoppingCart()