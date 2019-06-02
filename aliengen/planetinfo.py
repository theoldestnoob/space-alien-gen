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
        self.size = "Standard"
        self.type = "Garden"
        self.temp = random.randint(260, 340)
        self.climate_index = 0
        self.climate_index, self.climate = self.gen_climate()
        self.hydro = 70
        self.gravity = random.uniform(0, 6)

    def reroll(self):
        """
        Randomly generate all planet attributes,
        regardless of previous user input.
        """
        self.size = "Standard"
        self.type = "Garden"
        self.temp = random.randint(260, 340)
        self.climate_index = 0
        self.climate_index, self.climate = self.gen_climate()
        self.hydro = 70
        self.gravity = random.uniform(0, 6)

    def planetOutput(self):
        """
        Very basic unformatted text output of all planet attributes.
        """
        print(self.get_size())
        print(self.get_type())
        print(self.get_climate())
        print(self.get_temp_f())
        print(self.get_hydro())
        print(self.get_gravity())

    def get_temp_f(self):
        return ((1.8 * self.temp) - 460)

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
