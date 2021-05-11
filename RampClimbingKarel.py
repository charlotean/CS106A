from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""


def main():
    put_beeper()
    while front_is_clear():
        draw_diagonal_line()

def draw_diagonal_line():
    # Pre-condition: Karel begins facing East at the bottom left.
    # Post-condition: Karel leaves a a diagonal line that works in any world.
    for i in range(2):
        move()
    turn_left()
    move()
    put_beeper()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('RampKarel1.w')
