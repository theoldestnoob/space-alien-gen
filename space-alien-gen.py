# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:17:54 2019

@author: willh
"""

import ui.parser as parser
import ui.cmdline as cmdline


if __name__ == '__main__':

    args = parser.parse_cmdline()

    if args.textui:
        print("Call Text UI here!")
    elif args.gui:
        print("Call GUI here!")
    elif args.web:
        print("Call WebServer here!")
    else:
        cmdline.run_cmdline(args)
