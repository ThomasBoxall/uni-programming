from tkinter import *

class Manager:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, key):
        for item in self.items:
            if item.key == key:
                self.items.remove(item)
                break

    def findItem(self, key):
        for item in self.items:
            if item.key == key:
                return item
        return None

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def __str__(self):
        return "Key: {}, Value: {}".format(self.key, self.value)


def setUp():
    manager = Manager()
    item1 = Item(2, 3)
    item2 = Item(3, 678.6)
    item3 = Item(4, 55.67)
    manager.addItem(item1)
    manager.addItem(item2)
    manager.addItem(item3)
    return manager

def updateItemValue(item, value):
    item.setValue(float(value.get()))


def updateItemValue(item, value):
    item.setValue(float(value.get()))

def test():
    manager = setUp()

    root = Tk()
    for i in range(len(manager.items)):
        item = manager.items[i]

        key = Label(root, text=str(item.key))         
        key.grid(row=i, column=0)
        value = StringVar(value=str(item.value))
        valueEntry = Entry(root, textvariable=value)
        valueEntry.grid(row=i, column=1)
        updateButton = Button(root, text="Update", command=lambda item=item: updateItemValue(item, value))
        updateButton.grid(row=i, column=2)

    root.mainloop()


test()