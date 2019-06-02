# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:39:18 2019

@author: willh
"""

import copy

import aliengen.planetinfo as planetinfo
import aliengen.species as species


def run_cmdline(args):

    in_world = planetinfo.PlanetInfo()
    # TODO: parse user input for planet and apply to in_world
    in_species = species.Species(in_world)
    if args.sapient:
        in_species.sapient = True
    elif args.nonsapient:
        in_species.sapient = False
        in_species.possible_sapient = False

    print("================================================")
    for _ in range(0, args.num):
        alien = copy.deepcopy(in_species)
        alien.generate()
        alien.output_text_basic()
        print("================================================")
