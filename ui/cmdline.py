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
    in_world.gravity = args.planet_gravity
    in_world.hydro = args.planet_hydro
    in_world.temp = args.planet_temp
    in_world.generate()

    in_species = species.Species(in_world)
    if args.sapient:
        in_species.sapient = True
    elif args.nonsapient:
        in_species.sapient = False
        in_species.possible_sapient = False
    if args.personality_varied:
        in_species.p_more_variation = True
    else:
        in_species.p_more_variation = False

    print("================================================")
    in_world.planetOutput()
    print("================================================")
    for _ in range(0, args.num):
        alien = copy.deepcopy(in_species)
        alien.generate()
        alien.output_text_basic()
        print("================================================")
