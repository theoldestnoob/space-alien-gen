# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:37:09 2019

@author: willh
"""

import argparse
import aliengen.tables as tables


def parse_cmdline():

    c_chembasis = tables.ui_chemical_basis
    c_hab_type = tables.ui_hab_type
    c_habitat = tables.ui_habitat
    c_trophic = tables.ui_trophic_level
    c_loco_p = tables.ui_locomotion
    c_size_class = tables.ui_size_class
    c_symmetry = tables.ui_symmetry
    c_tail = tables.ui_tail_features
    c_skeleton = tables.ui_skeleton
    c_skintype = tables.ui_skin_type
    c_skin = tables.ui_skin
    c_breathing = tables.ui_breathing
    c_temp = tables.ui_temp
    c_growth = tables.ui_growth
    c_sexes = tables.ui_sexes
    c_gestation = tables.ui_gestation
    c_gest_special = tables.ui_gestation_special
    c_repro_strat = tables.ui_reproductive_strategy
    c_intelligence = tables.ui_intelligence
    c_mating = tables.ui_mating
    c_social = tables.ui_social

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
    parser.add_argument("-w", "--write", metavar="FILE",
                        help="Output to FILE")
    parser.add_argument("--csv", action="store_true",
                        help="Output in Semicolon Separated Variable format")
    parser.add_argument("--dir", help="Create a directory DIR in the current \
                        working directory and output a planet.txt file \
                        and a numbered .txt file for each alien generated. \
                        If --dir option is present, --csv and --write options \
                        are ignored.")
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
    parser.add_argument("--hab-type", choices=c_hab_type,
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
    parser.add_argument("--symmetry", choices=c_symmetry,
                        help="Species Symmetry")
    parser.add_argument("--sides", type=check_sides,
                        help="Species # of sides. Minimum 2. \
                              Automatically 2 if symmetry is bilateral \
                              and 3 if symmetry is trilateral.")
    parser.add_argument("--tail", choices=c_tail,
                        help="Species Tail Feature")
    parser.add_argument("--skeleton", choices=c_skeleton,
                        help="Species Skeleton Type")
    parser.add_argument("--skin-type", choices=c_skintype,
                        help="Species Skin Type (general)")
    parser.add_argument("--skin", choices=c_skin,
                        help="Species Skin Type (specific)")
    parser.add_argument("--breathing", choices=c_breathing,
                        help="Species Breathing Method")
    parser.add_argument("--temp", choices=c_temp,
                        help="Species Temperature Regulation")
    parser.add_argument("--growth", choices=c_growth,
                        help="Species Growth Pattern")
    parser.add_argument("--sexes", choices=c_sexes,
                        help="Species Sexes")
    parser.add_argument("--gestation", choices=c_gestation,
                        help="Species Gestation")
    parser.add_argument("--gest-special", choices=c_gest_special,
                        help="Species Special Gestation")
    parser.add_argument("--repro-strat", choices=c_repro_strat,
                        help="Species Reproductive Strategy")
    parser.add_argument("--intelligence", choices=c_intelligence,
                        help="Species Intelligence")
    parser.add_argument("--mating", choices=c_mating,
                        help="Species Mating Behavior")
    parser.add_argument("--social", choices=c_social,
                        help="Species Social Organization")
    parser.add_argument("--chauvinism", type=check_personality,
                        help="Species Chauvinism (-5 to 5)")
    parser.add_argument("--concentration", type=check_personality,
                        help="Species Concentration (-5 to 5)")
    parser.add_argument("--curiosity", type=check_personality,
                        help="Species Curiosity (-5 to 5)")
    parser.add_argument("--egoism", type=check_personality,
                        help="Species Egoism (-5 to 5)")
    parser.add_argument("--empathy", type=check_personality,
                        help="Species Empathy (-5 to 5)")
    parser.add_argument("--gregariousness", type=check_personality,
                        help="Species Gregariousness (-5 to 5)")
    parser.add_argument("--imagination", type=check_personality,
                        help="Species Imagination (-5 to 5)")
    parser.add_argument("--suspicion", type=check_personality,
                        help="Species Suspicion (-5 to 5)")
    parser.add_argument("--playfulness", type=check_personality,
                        help="Species Playfulness (-5 to 5)")

    # print(parser.parse_args())
    return parser.parse_args()


def check_sides(in_value):
    value = int(in_value)
    if value < 2:
        raise argparse.ArgumentTypeError("{} is an invalid number of sides".format(value))
    return value


def check_personality(in_value):
    value = int(in_value)
    if not -6 < value < 6:
        raise argparse.ArgumentTypeError("Personality trait value must be between -5 and 5!")
    return value
