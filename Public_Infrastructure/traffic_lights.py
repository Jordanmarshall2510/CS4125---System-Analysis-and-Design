class TrafficLight():
    def __init__(self,tLightID, totalElectricityUsage):
        self.tLightID =tLightID
        self.totalElectricityUsage = totalElectricityUsage

    def setLightID(self, newID):
        self.tLightID = newID

    def setTotalElectricityUsage(self,newValue):
        self.totalElectricityUsage = newValue
        