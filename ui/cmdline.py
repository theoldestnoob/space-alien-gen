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
    in_species.skeleton = args.skeleton
    in_species.skin = args.skin
    if args.breathing is not None:
        if args.breathing == "Lungs":
            in_species.breathing = "Lungs"
        elif args.breathing == "Gills":
            in_species.breathing = "Doesn't Breathe (Gills)"
        elif args.breathing == "Lungs Storage":
            in_species.breathing = "Lungs (air-breathing), Doesn't Breathe (Oxygen Storage)"
        elif args.breathing == "Gills Other":
            in_species.breathing = "Doesn't Breathe (Gills), Lungs (or convertable organ)"
    if args.temp is not None:
        if args.temp == "Cold-blooded-":
            in_species.temperature_regulation = "Cold-blooded (with disadvantage)"
        elif args.temp == "Cold-blooded":
            in_species.temperature_regulation = "Cold-blooded (no disadvantage)"
        elif args.temp == "Partial":
            in_species.temperature_regulation = "Partial regulation (temperature varies within limits)"
        elif args.temp == "Warm-blooded":
            in_species.temperature_regulation = "Warm-blooded"
        elif args.temp == "Warm-blooded+":
            in_species.temperature_regulation = "Warm-blooded (with Metabolism Control 2)"
    in_species.growth_pattern = args.growth
    if in_species.growth_pattern == "Unusual":
        in_species.growth_pattern = "Unusual Growth Pattern (adding segments, branching, etc.)"
    in_species.sexes = args.sexes
    in_species.gestation = args.gestation
    if args.gest_special is not None:
        if args.gest_special == "Brood Parasite":
            in_species.gestation_special = "Brood Parasite (raised by another species)"
        elif args.gest_special == "Parasitic Young":
            in_species.gestation_special = "Parasitic Young (implanted in a host)"
        elif args.gest_special == "Cannibalistic Young Fatal":
            in_species.gestation_special = "Cannibalistic Young (fatal to parent)"
        elif args.gest_special == "Cannibalistic Young":
            in_species.gestation_special = "Cannibalistic Young (consume each other)"

    lead_z = len(str(args.num))
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
            print("========================================")
            print("Planet Info:")
            print(in_world.planet_output())
            print("========================================")
            for k in range(0, args.num):
                alien = copy.deepcopy(in_species)
                alien.generate()
                print("Species {}:".format(str(k).zfill(lead_z)))
                print(alien.output_text_basic())
                print("========================================")
        elif not args.csv and args.write is not None:
            with open(args.write, "w") as file:
                file.write("========================================\n")
                file.write("Planet Info:\n")
                file.write(in_world.planet_output())
                file.write("\n========================================\n")
                for k in range(0, args.num):
                    alien = copy.deepcopy(in_species)
                    alien.generate()
                    file.write("Species #{}:\n".format(str(k).zfill(lead_z)))
                    file.write(alien.output_text_basic())
                    file.write("\n========================================\n")
        elif args.csv and args.write is None:
            print("========================================")
            print(in_world.planet_output())
            print("========================================")
            writer = csv.DictWriter(sys.stdout, fieldnames=tables.fieldnames,
                                    delimiter=";")
            writer.writeheader()
            for _ in range(0, args.num):
                alien = copy.deepcopy(in_species)
                alien.generate()
                out_row = vars(alien)
                for key in tables.nocsv:
                    out_row.pop(key, None)
                writer.writerow(out_row)
        else:
            with open(args.write, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=tables.fieldnames,
                                        delimiter=";")
                writer.writeheader()
                for _ in range(0, args.num):
                    alien = copy.deepcopy(in_species)
                    alien.generate()
                    out_row = vars(alien)
                    for key in tables.nocsv:
                        out_row.pop(key, None)
                    writer.writerow(out_row)
