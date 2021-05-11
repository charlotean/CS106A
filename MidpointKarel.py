from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    # Pre-condition: Karel draws a line to measure the world its in, then tries to find its way to the middle.
    # Post-condition: Karel ends up in the middle with a beeper, facing any direction.
    measure_world()
    find_midpoint()
    # Places beeper in the middle after finding the midpoint.
    put_beeper()

def measure_world():
    while front_is_clear():
        move()
        put_beeper()
    # Karel then turns around if the condition is false.
    turn_around()

def find_midpoint():
    while beepers_present():
        pick_beeper()
        move()
        while beepers_present():
            if front_is_clear():
                move()
        turn_around()
        move()

def turn_around():
    for i in range(2):
        turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
