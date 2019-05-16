# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:31:14 2019

@author: willh
"""

from aliengen import planetinfo as planetinfo
from aliengen import species as species
import time
import copy


def textui():

    start = time.process_time()

    print("Interactive Text Interface to space-alien-generator")
    print("")

    print("Random Planet:")
    planet = planetinfo.PlanetInfo()
    planet.planetOutput()
    print("")

    inspec = species.Species(planet)

    print("Input Species Parameters:")
    chembas = input("Chemical Basis: ")
    habtype = input("Habitat Type: ")
    inspec.chemical_basis = chembas
    inspec.habitat_type = habtype

    print("")
    print("Repeatedly Generating Species:")
    print("")
    for _ in range(500):
        outspec = copy.deepcopy(inspec)
        outspec.generate()
        '''outspec.output_text_basic()
        print("")
        print("======================")
        print("")'''
        print("{} - {}".format(outspec.habitat_type, outspec.habitat))

    end = time.process_time()
    elapsed = end - start

    print("That took ", end="")
    print(elapsed, end=" ")
    print("seconds!")


if __name__ == '__main__':

    textui()
