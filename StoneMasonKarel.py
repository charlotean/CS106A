from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    # Pre-condition: Karel starts repairing arches from the bottom left and continues to do so by jumping 3 columns across each.
    # Post-condition: Karel stops until farthest right is reached. Program should work in any Karel world.
    while front_is_clear():
        repair_arch()
        return_position()
        for i in range(4):
            move()
    if front_is_blocked():
        repair_arch()
        return_position()

def repair_arch():
    turn_left()
    while front_is_clear():
        safe_repair()

def return_position():
    if front_is_blocked():
        turn_around()
        safe_repair()
    while front_is_clear():
        move()
    turn_left()

def safe_repair():
    if no_beepers_present():
        put_beeper()
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()

def turn_around():
    for i in range(2):
        turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('SampleQuad1.w')
