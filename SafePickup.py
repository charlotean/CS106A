from karel.stanfordkarel import *

"""
File: SafePickup.py
--------------------
When you finish writing this file, Karel should be able to
pick up a beeper from the current position if one is present
(but do nothing if no beepers are present).
"""

def main():
    # Karel picks up beepers that are present, and does nothing if none are present.
    safe_pickup()

def safe_pickup():
    if beepers_present():
        pick_beeper()
    else:
        pass

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('SafePickup1.w')
