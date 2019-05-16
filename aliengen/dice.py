'''
Created on Dec 14, 2018

@author: willh
'''

import random


def rolldie(num, sides):
    """
    Return random number simulating rolling num dice with sides sides.
    """
    total = 0
    while num > 0:
        total += random.randint(1, sides)
        num -= 1
    return total


def rolldie_zero(num, sides):
    """
    Return random number simulating rolling num dice with sides sides.
    Dice's lowest side is 0 instead of 1.
    """
    return rolldie(num, sides) - num


def roll_2d6_subtract():
    """
    Return random number simulating rolling two six-sided dice
    and subtracting one from the other.
    """
    return rolldie(1, 6) - rolldie(1, 6)
