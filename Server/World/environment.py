#Coded by Jakub Pazej - 18260179
import random
import json
import os
import time

from World.clock import Clock
from World.weather import Weather

class environment:
    delay=0
    weather_change=0
    clock= Clock()
    weather= Weather()
    start=False

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__)).split(" World")[0] + "config.json"

        with open(path) as json_file:
            conf = json.load(json_file)
            self.delay=conf['world']['environment']['delay']
            self.weather_change=conf['world']['environment']['change']

    def getTime(self):
        return self.clock.getTime()

    def setTime(self, string):
        self.clock.setTime(string)
        date = time.localtime(self.clock.getTimeSeconds())
        if ((date.tm_mon>=3 and date.tm_mday>=20)or(date.tm_mon<=6 and date.tm_mday<21)):#spring
            self.weather.setSeason('spring')
        elif ((date.tm_mon>=6 and date.tm_mday>=21)or(date.tm_mon<=9 and date.tm_mday<22)):#summer
            self.weather.setSeason('summer')
        elif ((date.tm_mon>=9 and date.tm_mday>=22)or(date.tm_mon<=12 and date.tm_mday<21)):#autumn
            self.weather.setSeason('autumn')
        elif ((date.tm_mon>=12 and date.tm_mday>=21)or(date.tm_mon<=3 and date.tm_mday<20)):#winter
            self.weather.setSeason('winter')

    def getWeather(self):
        return self.weather.getWeather()

    def setWeather(self, string):
        self.weather.setWeather(string)

    def getSeason(self):
        return self.weather.getSeason()

    def start(self):
        self.start=True
        while (self.start == True):
            time.sleep(self.delay)
            date = time.localtime(self.clock.getTimeSeconds())
            if ((date.tm_mon>=3 and date.tm_mday>=20)or(date.tm_mon<=6 and date.tm_mday<21)):#spring
               self.weather.setSeason('spring')
            elif ((date.tm_mon>=6 and date.tm_mday>=21)or(date.tm_mon<=9 and date.tm_mday<22)):#summer
                self.weather.setSeason('summer')
            elif ((date.tm_mon>=9 and date.tm_mday>=22)or(date.tm_mon<=12 and date.tm_mday<21)):#autumn
                self.weather.setSeason('autumn')
            elif ((date.tm_mon>=12 and date.tm_mday>=21)or(date.tm_mon<=3 and date.tm_mday<20)):#winter
                self.weather.setSeason('winter')
            y=random.randint(0,100)
            if (y<self.weather_change):
                x=random.randint(0,100)
                if (self.weather.getSeason().lower()=='summer'):
                    if (x < 20):
                        self.weather.setWeather('rain')
                    elif (x < 50):
                        self.weather.setWeather('cloudy')
                    elif (x >= 50):
                        self.weather.setWeather('sunny')
                elif (self.weather.getSeason().lower()=='autumn'):
                    if (x < 5):
                        self.weather.setWeather('snow')
                    elif (x < 50):
                        self.weather.setWeather('rain')
                    elif (x < 90):
                        self.weather.setWeather('cloudy')
                    elif (x >= 90):
                        self.weather.setWeather('sunny')
                elif (self.weather.getSeason().lower()=='winter'):
                    if (x < 40):
                        self.weather.setWeather('snow')
                    elif (x < 50):
                        self.weather.setWeather('rain')
                    elif (x < 90):
                        self.weather.setWeather('cloudy')
                    elif (x >= 90):
                        self.weather.setWeather('sunny')
                elif (self.weather.getSeason().lower()=='spring'):
                    if (x < 5):
                        self.weather.setWeather('snow')
                    elif (x < 50):
                        self.weather.setWeather('rain')
                    elif (x < 90):
                        self.weather.setWeather('cloudy')
                    elif (x >= 90):
                        self.weather.setWeather('sunny')
            self.clock.setTimeSeconds(self.clock.getTimeSeconds()+3600)

    def stop(self):
        self.start=False

    def getDaylight(self):
        return self.clock.getDayLight()