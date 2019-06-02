# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:37:09 2019

@author: willh
"""

import argparse
import itertools
import aliengen.tables as tables


def parse_cmdline():

    c_chembasis = set(tables.chemical_basis)
    c_habitat = set(tables.hab_land + tables.hab_water)
    c_trophic = set(tables.troph_sapient)
    c_loco_p = set(itertools.chain.from_iterable(tables.loco_primary.values()))
    c_size_class = ("Small", "Human-Scale", "Large", "Huge")

    parser = argparse.ArgumentParser(prog="space-alien-gen",
                                     description="Randomly Generate an Alien. \
                                     Use --textui, --gui, --web options for \
                                     other UIs, or use command line options. \
                                     Command line options will be ignored if \
                                     another UI option is used.")
    parser.add_argument("--textui", action="store_true",
                        help="Run interactive text UI, ignore other options")
    parser.add_argument("--gui", action="store_true",
                        help="Run Graphical UI, ignore other options")
    parser.add_argument("--web", action="store_true",
                        help="Run Local Webserver UI, ignore other options")
    parser.add_argument("-n", "--num", default=1, type=int,
                        help="Number of species to generate")
    parser.add_argument("--earthlike", action="store_true",
                        help="Generate Earthlike planet for species")
    parser.add_argument("--gasgiant", action="store_true",
                        help="Generate Gas Giant planet for species")
    parser.add_argument("--planet-temp", type=int,
                        help="Set Planet Temperature in Kelvin")
    parser.add_argument("--planet-hydro", type=int,
                        help="Set Planet Percentage Hydrographic Coverage")
    parser.add_argument("--planet-gravity", type=float,
                        help="Set Planet Gravity in Gs")
    parser.add_argument("--sapient", action="store_true",
                        help="Species generated will be sapient")
    parser.add_argument("--nonsapient", action="store_true",
                        help="Species generated will not be sapient. \
                              If neither sapient nor nonsapient, \
                              sapience will be randomly generated.")
    parser.add_argument("--personality-varied", action="store_true",
                        help="Species personality generation will be more \
                              varied. Otherwise, personality will be very \
                              dependent on biology.")
    parser.add_argument("--chem-basis", choices=c_chembasis,
                        help="Species Chemical Basis")
    parser.add_argument("--hab-type", choices=tables.hab_type,
                        help="Species Habitat Type")
    parser.add_argument("--habitat", choices=c_habitat,
                        help="Species Habitat")
    parser.add_argument("--trophic", choices=c_trophic,
                        help="Species Trophic Level")
    parser.add_argument("--loco-primary", choices=c_loco_p,
                        help="Species Primary Method of Locomotion")
    parser.add_argument("--size-class", choices=c_size_class,
                        help="Species Size Class")
    parser.add_argument("--size-volume", type=float,
                        help="Species Length on Longest Axis")
    parser.add_argument("--size-mass", type=float,
                        help="Species Mass")

    # TODO: delete scaffolding after command line parser is completed
    print(parser.parse_args())

    return parser.parse_args()
