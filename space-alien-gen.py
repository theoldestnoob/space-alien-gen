# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:17:54 2019

@author: willh
"""

import ui.parser as parser
import ui.cmdline as cmdline
import ui.gui as gui

if __name__ == '__main__':

    args = parser.parse_cmdline()

    if args.textui:
        print("Call Text UI here!")
    elif args.gui:
        gui.run_gui()
    elif args.web:
        print("Call WebServer here!")
    else:
        cmdline.run_cmdline(args)
