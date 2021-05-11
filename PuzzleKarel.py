from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""


def main():
    pick_puzzle_piece()
    put_puzzle_piece()
    return_karel()

#I want to define pick_puzzle_piece, put_puzzle_piece and return_karel here
def pick_puzzle_piece():
    # Karel goes to the beeper and picks it
    # Pre-condition: Karel starts at the bottom left, facing East.
    # Post-condition: Karel moves to its next position where its headed towards the puzzle.
    for i in range(2):
        move()
    pick_beeper()

def put_puzzle_piece():
    # Pre: Karel goes to the puzzle and places its beeper.
    # Post: Karel turns around facing South.
    move()
    turn_left()
    for i in range(2):
        move()
    put_beeper()
    turn_around()

def return_karel():
    # Pre: Karel facing South.
    # Post: Karel makes it on its original position.
    for i in range(2):
        move()
    turn_right()
    for i in range(3):
        move()
    turn_around()

def turn_around():
    for i in range (2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('Puzzle.w')
