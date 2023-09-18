class SmartMeter:
    def __init__(self):
        self.energyBalance = 1000
        self.solarPanels = False
    
    def useEnergy(self, energyNeeded):
        newEnergyBalance = self.energyBalance - energyNeeded
        if newEnergyBalance> 0 or newEnergyBalance >-500 and self.solarPanels == True:
            # enough energy 
            self.energyBalance  = newEnergyBalance
            print("energy use successful. you now have {} kWh left.".format(self.energyBalance))
        else:
            # not enough energy
            print("you have run out of energy. buy more or activate solar panels")

    def activateSolarPanels(self):
        self.solarPanels = True

def testSmartMeter():
    sm = SmartMeter()
    sm.useEnergy(430)
    sm.useEnergy(200)
    sm.useEnergy(400)
    sm.activateSolarPanels()
    sm.useEnergy(400)
    sm.useEnergy(500)


testSmartMeter()