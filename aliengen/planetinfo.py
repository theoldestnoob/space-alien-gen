'''
Created on Dec 14, 2018

@author: willh
'''

import random


class PlanetInfo(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.type = ""
        self.temp = -1
        self.climate_index = -1
        self.climate = ""
        self.hydro = -1
        self.gravity = -1

    def reroll(self):
        """
        Randomly generate all planet attributes except type,
        regardless of previous user input.
        """
        self.type = "Regular"
        self.temp = random.randint(260, 350)
        self.climate_index = 0
        self.climate_index, self.climate = self.gen_climate()
        self.hydro = random.randint(0, 100)
        self.gravity = round(random.uniform(0, 6), 3)

    def generate(self):
        """
        Randomly generate all planet attributes not previously entered by user.
        """
        if self.type == "":
            self.type = "Regular"
        if self.temp == -1:
            self.temp = random.randint(260, 350)
        if self.climate == "":
            self.climate_index, self.climate = self.gen_climate()
        if self.hydro == -1:
            self.hydro = random.randint(0, 100)
        if self.gravity == -1:
            self.gravity = round(random.uniform(0, 6), 3)

    def planetOutput(self):
        """
        Very basic text output of all planet attributes.
        """
        print("Planet Info:")
        print(" Type: {}".format(self.type))
        print(" Climate: {}".format(self.climate))
        print(" Temperature: {}K ({}F)".format(self.temp, self.get_temp_f()))
        print(" Hydrographic Coverage: {}%".format(self.hydro))
        print(" Gravity: {}G".format(self.gravity))

    def get_temp_f(self):
        return round((1.8 * self.temp) - 460, 2)

    def gen_climate(self):
        if self.temp < 244:
            return 0, "Frozen"
        elif self.temp < 256:
            return 1, "Very Cold"
        elif self.temp < 267:
            return 2, "Cold"
        elif self.temp < 279:
            return 3, "Chilly"
        elif self.temp < 290:
            return 4, "Cool"
        elif self.temp < 301:
            return 5, "Normal"
        elif self.temp < 312:
            return 6, "Warm"
        elif self.temp < 323:
            return 7, "Tropical"
        elif self.temp < 334:
            return 8, "Hot"
        elif self.temp < 345:
            return 9, "Very Hot"
        else:
            return 10, "Infernal"


if __name__ == '__main__':
    import planetinfo
    PLANET = planetinfo.PlanetInfo()
    PLANET.reroll()
    PLANET.planetOutput()
