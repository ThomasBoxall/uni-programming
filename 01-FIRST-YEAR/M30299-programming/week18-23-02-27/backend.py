class Manager:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def getItems(self):
        return self.items

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

    def updateAll(self, values):
        for i, item in enumerate(self.items):
            item.setValue(values[i])

    def __str__(self):
        return f"Manager items: {[str(item) for item in self.items]}"

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def __str__(self):
        return f"Key: {self.key}, Value: {self.value}"