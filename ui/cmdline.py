# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:39:18 2019

@author: willh
"""

import copy
import csv
import sys
import os

import aliengen.planetinfo as planetinfo
import aliengen.species as species
import aliengen.tables as tables
import aliengen.dice as dice


def run_cmdline(args):

    # TODO: Holy crap this is ugly as sin, make it less so
    in_world = planetinfo.PlanetInfo()
    if args.earthlike:
        in_world.generate_earthlike()
    else:
        if args.gasgiant:
            in_world.type = "Gas Giant"
        in_world.gravity = args.planet_gravity
        in_world.hydro = args.planet_hydro
        in_world.temp = args.planet_temp
        in_world.generate()

    in_species = species.Species(in_world)
    if args.sapient:
        in_species.sapient = True
        in_species.intelligence = "Sapient"
    elif args.nonsapient:
        in_species.sapient = False
        in_species.possible_sapient = False
    if args.personality_varied:
        in_species.p_more_variation = True
    else:
        in_species.p_more_variation = False
    in_species.chemical_basis = args.chem_basis
    in_species.habitat_type = args.hab_type
    in_species.habitat = args.habitat
    if in_species.habitat is not None:
        if in_species.habitat in tables.hab_land:
            in_species.habitat_type = "Land"
        elif in_species.habitat in tables.hab_water:
            in_species.habitat_type = "Water"
    in_species.trophic_level = args.trophic
    if args.loco_primary is not None:
        in_species.locomotion = [args.loco_primary]
    in_species.size_class = args.size_class
    in_species.size_volume = args.size_volume
    in_species.size_mass = args.size_mass
    in_species.symmetry = args.symmetry
    if args.symmetry == "Bilateral":
        in_species.sides = 2
    elif args.symmetry == "Trilateral":
        in_species.sides = 3
    else:
        in_species.sides = args.sides
    in_species.tail = args.tail
    in_species.skeleton = args.skeleton
    in_species.skin_type = args.skin_type
    if args.skin is not None:
        in_species.skin = tables.ui_skin_map[args.skin]
    if args.breathing is not None:
        in_species.breathing = tables.ui_lungs_map[args.breathing]
    if args.temp is not None:
        in_species.temperature_regulation = tables.ui_temp_map[args.temp]
    in_species.growth_pattern = args.growth
    if in_species.growth_pattern == "Unusual":
        in_species.growth_pattern = "Unusual Growth Pattern (adding segments, branching, etc.)"
    in_species.sexes = args.sexes
    in_species.gestation = args.gestation
    if args.gest_special is not None:
        in_species.gestation_special = tables.ui_gest_special_map[args.gest_special]
    in_species.reproductive_strat = args.repro_strat
    in_species.sense_primary = args.sense_primary
    if args.sense_vision is not None:
        in_species.sense_roll["Vision"] = tables.ui_sense_vision_map[args.sense_vision]
    if args.sense_hearing is not None:
        in_species.sense_roll["Hearing"] = tables.ui_sense_hearing_map[args.sense_hearing]
    if args.sense_touch is not None:
        in_species.sense_roll["Touch"] = tables.ui_sense_touch_map[args.sense_touch]
    if args.sense_tastesmell is not None:
        in_species.sense_roll["Taste/Smell"] = tables.ui_sense_tastesmell_map[args.sense_tastesmell]
    in_species.sense_specials = args.sense_special
    if args.sense_special is not None:
        for sense in args.sense_special:
            if sense in ["Ultravision", "Detect (Heat)",
                         "Detect (Electric Fields)", "Scanning Sense (Radar)"]:
                in_species.sense_roll[sense] = dice.rolldie(2, 6)
    if args.intelligence is not None:
        in_species.intelligence = tables.ui_intel_map[args.intelligence]
    if args.intelligence == "Sapient":
        in_species.sapient = True
    if args.mating is not None:
        in_species.mating = tables.ui_mating_map[args.mating]
    if args.mating == "Hive":
        args.social = "Hive"
    elif args.social == "Hive":
        in_species.mating = "Hive"
    if args.social is not None:
        in_species.social_organization = tables.ui_social_map[args.social]
    in_species.p_chauvinism = args.chauvinism
    in_species.p_concentration = args.concentration
    in_species.p_curiosity = args.curiosity
    in_species.p_egoism = args.egoism
    in_species.p_empathy = args.empathy
    in_species.p_gregariousness = args.gregariousness
    in_species.p_imagination = args.imagination
    in_species.p_suspicion = args.suspicion
    in_species.p_playfulness = args.playfulness

    lead_z = len(str(args.num - 1))
    if args.dir is not None:
        print("Directory: {} but not CSV!".format(args.dir))
        cwd = os.getcwd()
        out_dir = os.path.join(cwd, args.dir)
        print("Full path: {}".format(out_dir))
        if not os.path.exists(out_dir):
            print("Directory does not exist! making it!")
            os.mkdir(out_dir)
        os.chdir(out_dir)
        with open("planet.txt", "w") as file:
            file.write(in_world.planet_output())
        for k in range(0, args.num):
            outfile = "".join([str(k).zfill(lead_z), ".txt"])
            alien = copy.deepcopy(in_species)
            alien.generate()
            with open(outfile, "w") as file:
                file.write(alien.output_text_basic())
    else:
        if not args.csv and args.write is None:
            print("=" * 40)
            print("Planet Info:")
            print(in_world.planet_output())
            print("=" * 40)
            for k in range(0, args.num):
                alien = copy.deepcopy(in_species)
                alien.generate()
                print("Species {}:".format(str(k).zfill(lead_z)))
                print(alien.output_text_basic())
                print("=" * 40)
        elif not args.csv and args.write is not None:
            with open(args.write, "w") as file:
                file.write("=" * 40)
                file.write("\n")
                file.write("Planet Info:\n")
                file.write(in_world.planet_output())
                file.write("\n")
                file.write("=" * 40)
                file.write("\n")
                for k in range(0, args.num):
                    alien = copy.deepcopy(in_species)
                    alien.generate()
                    file.write("Species #{}:\n".format(str(k).zfill(lead_z)))
                    file.write(alien.output_text_basic())
                    file.write("\n")
                    file.write("=" * 40)
                    file.write("\n")
        elif args.csv and args.write is None:
            print("=" * 40)
            print(in_world.planet_output())
            print("=" * 40)
            writer = csv.DictWriter(sys.stdout, fieldnames=tables.csv_fields,
                                    delimiter=";")
            writer.writeheader()
            for _ in range(0, args.num):
                alien = copy.deepcopy(in_species)
                alien.generate()
                out_row = vars(alien)
                for key in tables.csv_unused:
                    out_row.pop(key, None)
                writer.writerow(out_row)
        else:
            with open(args.write, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=tables.csv_fields,
                                        delimiter=";")
                writer.writeheader()
                for _ in range(0, args.num):
                    alien = copy.deepcopy(in_species)
                    alien.generate()
                    out_row = vars(alien)
                    for key in tables.csv_unused:
                        out_row.pop(key, None)
                    writer.writerow(out_row)
