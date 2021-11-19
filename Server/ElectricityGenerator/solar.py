#Coded by Jakub Pazej - 18260179
import json
import os
import random
from ElectricityGenerator.electricitygenerator import ElectricityGenerator
from datetime import datetime

class Solar(ElectricityGenerator):
    wattage=0
    GeneratorID = 0

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split("ElectricityGenerator")[0] + "config.json"
        with open(path) as json_file:
            conf = json.load(json_file)
            self.wattage=conf["electricityGenerator"]["solar"]["output"]

    def setGeneratorID(self, newID):
        self.GeneratorID = newID

    def update(self, date):
        current_time = int(date.strftime("%H"))
        if(current_time<6 or current_time>20):
            return 0
        elif(current_time<=12):
            a=random.uniform(0,0.00014)
            b=random.uniform(0,0.0014)
            return (self.wattage+a)+(b*current_time)
        elif(current_time>12):
            a=random.uniform(0,0.00014)
            b=random.uniform(0,0.0014)
            return (self.wattage+a)+(b*(24-current_time))

    def getElectricityGenerated(self):
        return self.update()

    def generateGenerators(numberOfGenerators):
        generatedArray = []
        for x in range(numberOfGenerators):
            generator = Solar()
            generator.setGeneratorID(x + 1)
            generatedArray.append(generator)
        return generatedArray