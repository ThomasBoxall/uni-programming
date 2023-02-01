ramOptions = {
    8: 0.00,
    16: 59.99,
    32: 92.50,
}

gpuOptions = {
    "NVIDIA GeForce 4GB": 0.00,
    "NVIDIA GeForce 8GB": 199.99,
    "AMD Radeon 12GB": 299.99,
}

ssdOptions = {
    "256GB": 0.00,
    "512GB": 30.00,
    "1TB": 100,
}

class Laptop():
    """
    A class to represent a laptop.
    A laptop has a brand, model, price and ram.
    The price is the base price plus the cost of the ram.
    The ram is 8GB by default.
    """

    def __init__(self, brand, model, basePrice):
        self.brand = brand
        self.model = model
        self.price = basePrice
        self.basePrice = self.price
        self.ram = 8
        self.ssd = "256GB"

    def getPrice(self):
        """
        Returns the price of the laptop.
        """
        return self.price

    def setRram(self, ram):
        """
        Sets the ram of the laptop to the given value.
        If the value is not in the ramOptions dictionary, the ram is not changed.
        The price is updated to include the cost of the ram.
        """
        if ram in ramOptions:
            self.ram = ram
            costOfRam = ramOptions[ram]
            self.price = self.basePrice+ costOfRam

    def setSSD(self, ssd):
        """
        Sets the ssd of the laptop to the given value.
        If the value is not in the ssdOptions dictionary, the ssd is not changed.
        The price is updated to include the cost of the ssd.
        """
        if ssd in ssdOptions:
            self.ssd = ssd
            costOfSSD = ssdOptions[ssd]
            self.price += costOfSSD

    def __str__(self):
        output = "{} {}".format(self.brand, self.model)
        output += " {}GB {}".format(self.ram, self.ssd)
        # output += " £{:.2f}".format(self.price)
        return output

    def getBrand(self):
        """
        Returns the brand of the laptop.
        """
        return self.brand