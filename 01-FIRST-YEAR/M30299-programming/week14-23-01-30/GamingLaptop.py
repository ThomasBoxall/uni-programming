from Laptop import *

class GamingLaptop(Laptop):
    """
    A class to represent a gaming laptop.
    A gaming laptop has a brand, model, price, ram and gpu.
    The price is the base price plus the cost of the ram and the gpu.
    The ram is 8GB by default.
    The gpu is "NVIDIA GeForce 4GB" by default.
    """

    def __init__(self, brand, model, basePrice):
        super().__init__(brand, model, basePrice)
        self.gpu = "NVIDIA GeForce 4GB"

    def setGpu(self, gpu):
        """
        Sets the gpu of the laptop to the given value.
        If the value is not in the gpuOptions dictionary, the gpu is not changed.
        The price is updated to include the cost of the gpu.
        """
        if gpu in gpuOptions:
            self.gpu = gpu
            costOfGpu = gpuOptions[gpu]
            self.price = self.price + costOfGpu

    def __str__(self):
        output = super().__str__()
        output += " {}".format(self.gpu)
        output += " £{:.2f}".format(super().getPrice())
        return output