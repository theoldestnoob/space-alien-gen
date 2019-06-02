# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:37:09 2019

@author: willh
"""

import argparse


def parse_cmdline():
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

    # TODO: delete scaffolding after command line parser is completed
    print(parser.parse_args())

    return parser.parse_args()
